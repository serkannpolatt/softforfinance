import numpy as np
import pandas as pd
import pandas_ta as ta
import yfinance as yf
import vectorbt as vbt
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from tvDatafeed import TvDatafeed, Interval
import warnings
warnings.filterwarnings('ignore')
tv = TvDatafeed()
BIST100_Hisseler=pd.DataFrame()
Column_Names=['Hisse Adı','Al-Sat Sayısı','Kazanma Oranı [%]','Toplam Kâr [%]','Ortalama Kazanma Oranı [%]']

Hisse=['AEFES','AGHOL','AHGAZ','AKBNK','AKCNS','AKFGY','AKSA ','AKSEN','ALARK','ALBRK','ALFAS','ARCLK','ASELS','ASTOR','ASUZU','AYDEM','BAGFS','BERA ','BIMAS',
    'BIOEN','BRSAN','BRYAT','BUCIM','CANTE','CCOLA','CEMTS','CIMSA','DOAS','DOHOL','ECILC','ECZYT','EGEEN','EKGYO','ENJSA','ENKAI','EREGL',
    'EUREN','FROTO','GARAN','GENIL','GESAN','GLYHO','GSDHO','GUBRF','GWIND','HALKB','HEKTS','IPEKE','ISCTR','ISDMR','ISGYO','ISMEN','IZMDC',
    'KARSN','KCAER','KCHOL','KMPUR','KONTR','KONYA','KORDS','KOZAA','KOZAL','KRDMD','KZBGY','MAVI ','MGROS','ODAS ','OTKAR','OYAKC','PENTA',
    'PETKM','PGSUS','PSGYO','QUAGR','SAHOL','SASA ','SELEC','SISE ','SKBNK','SMRTG','SNGYO','SOKM ','TAVHL','TCELL','THYAO','TKFEN','TKNSA',
    'TOASO','TSKB','TTKOM','TTRAK','TUKAS','TUPRS','ULKER','VAKBN','VESBE','VESTL','YKBNK','YYLGD','ZOREN']

def get_adx(high, low, close, n2):
    plus_dm = high.diff()
    minus_dm = low.diff()
    plus_dm[plus_dm < 0] = 0
    minus_dm[minus_dm > 0] = 0
    tr1 = pd.DataFrame(high - low)
    tr2 = pd.DataFrame(abs(high - close.shift(1)))
    tr3 = pd.DataFrame(abs(low - close.shift(1)))
    frames = [tr1, tr2, tr3]
    tr = pd.concat(frames, axis = 1, join = 'inner').max(axis = 1)
    atr = tr.rolling(n2).mean()
    plus_di = 100 * (plus_dm.ewm(alpha = 1/n2).mean() / atr)
    minus_di = abs(100 * (minus_dm.ewm(alpha = 1/n2).mean() / atr))
    dx = (abs(plus_di - minus_di) / abs(plus_di + minus_di)) * 100
    adx = ((dx.shift(1) * (n2 - 1)) + dx) / n2
    adx_smooth = adx.ewm(alpha = 1/n2).mean()
    return plus_di, minus_di, adx_smooth

def WT_Cross(df,n1,n2):
    WT_Data=pd.DataFrame()
    ap=ta.hlc3(df['High'],df['Low'],df['Close'])
    esa = ta.ema(ap, n1)
    d = ta.ema(abs(ap - esa).dropna(), n1)
    ci = (ap - esa) / (0.015 * d)
    tci = ta.ema(ci.dropna(), n2)
    WT_Data['tci1'] = tci
    WT_Data['tci2'] = ta.sma(WT_Data['tci1'],4)
    return WT_Data

def TillsonT3(Close, high, low, vf, length):
    ema_first_input = (high + low + 2 * Close) / 4
    e1 = ta.ema(ema_first_input, length)
    e2 = ta.ema(e1, length)
    e3 = ta.ema(e2, length)
    e4 = ta.ema(e3, length)
    e5 = ta.ema(e4, length)
    e6 = ta.ema(e5, length)

    c1 = -1 * vf * vf * vf
    c2 = 3 * vf * vf + 3 * vf * vf * vf
    c3 = -6 * vf * vf - 3 * vf - 3 * vf * vf * vf
    c4 = 1 + 3 * vf + vf * vf * vf + 3 * vf * vf
    T3 = c1 * e6 + c2 * e5 + c3 * e4 + c4 * e3
    return T3

def OTT(df,prt,prc):
    pds = prt
    percent = prc
    alpha = 2 / (pds + 1)

    df['ud1'] = np.where(df['Close'] > df['Close'].shift(1), (df['Close'] - df['Close'].shift()) , 0)
    df['dd1'] = np.where(df['Close'] < df['Close'].shift(1), (df['Close'].shift() - df['Close']) , 0)
    df['UD'] = df['ud1'].rolling(9).sum()
    df['DD'] = df['dd1'].rolling(9).sum()
    df['CMO'] = ((df['UD'] - df['DD']) / (df['UD'] + df['DD'])).fillna(0).abs()

    df['Var'] = 0.0
    for i in range(pds, len(df)):
        df['Var'].iat[i] = (alpha * df['CMO'].iat[i] * df['Close'].iat[i]) + (1 - alpha * df['CMO'].iat[i]) * df['Var'].iat[i-1]

    df['fark'] = df['Var'] * percent * 0.01
    df['newlongstop'] = df['Var'] - df['fark']
    df['newshortstop'] = df['Var'] + df['fark']
    df['longstop'] = 0.0
    df['shortstop'] = 999999999999999999
    # df['dir'] = 1
    for i in df['UD']:

        def maxlongstop():
            df.loc[(df['newlongstop'] > df['longstop'].shift(1)) , 'longstop'] = df['newlongstop']
            df.loc[(df['longstop'].shift(1) > df['newlongstop']), 'longstop'] = df['longstop'].shift(1) 

            return df['longstop']

        def minshortstop():
            df.loc[(df['newshortstop'] < df['shortstop'].shift(1)), 'shortstop'] = df['newshortstop']
            df.loc[(df['shortstop'].shift(1) < df['newshortstop']), 'shortstop'] = df['shortstop'].shift(1)

            return df['shortstop']

        df['longstop']= np.where (((df['Var'] > df['longstop'].shift(1))),maxlongstop(),df['newlongstop'])
        df['shortstop'] = np.where(((df['Var'] < df['shortstop'].shift(1))), minshortstop(), df['newshortstop'])

    #get xover

    df['xlongstop'] = np.where (((df['Var'].shift(1) > df['longstop'].shift(1)) & (df['Var'] < df['longstop'].shift(1))), 1,0)
    df['xshortstop'] =np.where(((df['Var'].shift(1) < df['shortstop'].shift(1)) & (df['Var'] > df['shortstop'].shift(1))), 1,0)

    df['trend']=0
    df['dir'] = 0

    for i in df['UD']:
            df['trend'] = np.where(((df['xshortstop'] == 1)),1, (np.where((df['xlongstop'] == 1),-1,df['trend'].shift(1))))
            df['dir'] = np.where(((df['xshortstop'] == 1)),1, (np.where((df['xlongstop'] == 1),-1,df['dir'].shift(1).fillna(1))))


    df['MT'] = np.where(df['dir'] == 1, df['longstop'], df['shortstop'])
    df['OTT'] = np.where(df['Var'] > df['MT'], (df['MT'] * (200 + percent) / 200), (df['MT'] * (200 - percent) / 200))
    # round the numeric columns
    df = df.round(2)
    
    #this OTT2 column now is to be shifted by 2 prev values
    df['OTT2'] = df['OTT'].shift(2)
    df['OTT3'] = df['OTT'].shift(3)
    
    return df

def Strategy(Hisse_Adı,Lenght_1,vf,prt,prc):
    
    data = tv.get_hist(symbol=Hisse_Adı,exchange='BIST',interval=Interval.in_daily,n_bars=500)
    data.rename(columns = {'open':'Open', 'high':'High','low':'Low','close':'Close','volume':'Volume'}, inplace = True)
    #data = yf.download(Hisse_Adı+'.IS',start='2023-01-01',interval='1d',progress=False)
    OTT_Signal=OTT(data.copy(deep=True),prt,prc)
    Tillson=TillsonT3(data['Close'],data['High'],data['Low'],vf,Lenght_1)
    Zscore=ta.zscore(data['Close'],21,1)
    Zsma=ta.sma(Zscore)
    data['OTT']=OTT_Signal['OTT']
    data['Var']=OTT_Signal['Var']
    data['Tillson']=Tillson
    data['Zscore']=Zscore
    data['ZSMA']=Zsma

    #True Condition
    
    data['OTT_Signal']=(data['Var'])>OTT_Signal['OTT3']
    data['Zscore_Signal']=data['Zscore']>0.85
    #True Condition
    data['Entry']=(data['OTT_Signal'] & data['Zscore_Signal']) 
    data['Exit']=False
    for i in range(1,len(data['Entry'])-1):
        t3_prev = data['Tillson'][i-1]
        t3_now = data['Tillson'][i]

        if  t3_now < t3_prev:
            data['Exit'][i]=True
    return data

Lenght_1=6
vf = 0.8
prt=2
prc=1.2

for i in range(len(Hisse)):
    data = Strategy(Hisse[i], Lenght_1, vf, prt, prc)
    psettings = {'init_cash': 100, 'freq': 'D', 'direction': 'longonly', 'accumulate': True}
    Entry = data.ta.tsignals(data['Entry'], asbool=True, append=False)
    Exit = data.ta.tsignals(data['Exit'], asbool=True, append=False)
    pf = vbt.Portfolio.from_signals(data['Close'], entries=Entry['TS_Entries'], exits=Exit['TS_Exits'], **psettings)
    Stats = pf.stats()
    L1 = [Hisse[i], Stats.loc['Total Trades'], Stats.loc['Win Rate [%]'], Stats.loc['Total Return [%]'], Stats.loc['Avg Winning Trade [%]']]
    Results = pd.DataFrame([L1], columns=Column_Names)
    BIST100_Hisseler = pd.concat([BIST100_Hisseler, Results], ignore_index=True)
    print(Results)

