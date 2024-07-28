import warnings
import pandas as pd 
import numpy as np
import pandas_ta as ta
from scipy.signal import argrelextrema
from scipy import stats
import vectorbt as vbt
from urllib import request
import ssl
import os
import matplotlib.pyplot as plt
import mplcyberpunk
import requests
warnings.simplefilter(action='ignore', category=FutureWarning)

def Hisse_Temel_Veriler():
    url1="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/Temel-Degerler-Ve-Oranlar.aspx#page-1"
    context = ssl._create_unverified_context()
    response = request.urlopen(url1, context=context)
    url1 = response.read()

    df = pd.read_html(url1,decimal=',', thousands='.')                         #Tüm Hisselerin Tablolarını Aktar
    df2=df[6]
    return df2

def Stock_Prices(Hisse,period=120,Bar=1000):
    url = f"https://www.isyatirim.com.tr/_Layouts/15/IsYatirim.Website/Common/ChartData.aspx/IntradayDelay?period={period}&code={Hisse}.E.BIST&last={Bar}"
    r1 = requests.get(url).json()
    data = pd.DataFrame.from_dict(r1)
    data[['Volume', 'Close']] = pd.DataFrame(data['data'].tolist(), index=data.index)
    data.drop(columns=['data'], inplace=True)
    return data

def rsi_divergence(data, window, order):
    df=data.copy()   
    #calculating RSI with talib
    df['RSI']=ta.rsi(df['Close'], window)
    hh_pairs=argrelextrema(df['Close'].values, comparator=np.greater, order=order)[0]
    hh_pairs=[hh_pairs[i:i+2] for i in range(len(hh_pairs)-1)]
    ll_pairs=argrelextrema(df['Close'].values, comparator=np.less, order=order)[0]
    ll_pairs=[ll_pairs[i:i+2] for i in range(len(ll_pairs)-1)]
    
    bear_div=[]
    bull_div=[]
    
    for p in hh_pairs:
        x_price=p
        y_price=[df['Close'].iloc[p[0]], df['Close'].iloc[p[1]]]
        slope_price=stats.linregress(x_price, y_price).slope
        x_rsi=p
        y_rsi=[df['RSI'].iloc[p[0]], df['RSI'].iloc[p[1]]]
        slope_rsi=stats.linregress(x_rsi, y_rsi).slope
        
        if slope_price>0:
            if np.sign(slope_price)!=np.sign(slope_rsi):
                bear_div.append(p)
       
    for p in ll_pairs:
        x_price=p
        y_price=[df['Close'].iloc[p[0]], df['Close'].iloc[p[1]]]
        slope_price=stats.linregress(x_price, y_price).slope
        x_rsi=p
        y_rsi=[df['RSI'].iloc[p[0]], df['RSI'].iloc[p[1]]]
        slope_rsi=stats.linregress(x_rsi, y_rsi).slope
        
        if slope_price<0:
            if np.sign(slope_price)!=np.sign(slope_rsi):
                bull_div.append(p)    
    
    bear_points=[df.index[a[1]] for a in bear_div]
    bull_points=[df.index[a[1]] for a in bull_div]
    pos=[]
    
    for idx in df.index:
        if idx in bear_points:
            pos.append(-1)
        elif idx in bull_points:
            pos.append(1)
        else:
            pos.append(0)
    
    df['position']=pos
    df['position']=df['position'].replace(0, method='ffill')  
    return df

Hisse_Ozet=Hisse_Temel_Veriler()
Hisseler=Hisse_Ozet['Kod'].values.tolist()

Titles=['Hisse Adı','Kazanma Oranı[%]','Sharpe Oranı','Ort. Kazanma Oranı [%]','Ort Kazanma Süresi','Ort. Kayıp Oranı [%]','Ort Kayıp Süresi','Giriş Sinyali','Çıkış Sinyali']
df_signals=pd.DataFrame(columns=Titles)

for i in range(0,len(Hisseler)):
    try:
        P=120
        B=1000
        data=Stock_Prices(Hisseler[i],period=P,Bar=B)
        Hisse=rsi_divergence(data,14,order=3)
        Hisse['Entry'] = (Hisse['position'] == 1) & (Hisse['RSI']<40)
        Hisse['Exit'] = (Hisse['position'] == -1)
        psettings = {'init_cash': 100,'freq': 'H', 'direction': 'longonly', 'accumulate': True}
        pf = vbt.Portfolio.from_signals(Hisse['Close'], entries=Hisse['Entry'], exits=Hisse['Exit'],**psettings)
        Stats=pf.stats()
        
        Buy=False
        Sell=False
        Signals = Hisse.tail(5)
        Signals = Signals.reset_index()
        any_entry = Signals['Entry'].any()
        all_entry = Signals['Entry'].all()
        
        any_exit = Signals['Exit'].any()
        all_exit = Signals['Exit'].all()

        Buy = any_entry and not all_entry
        Sell = any_exit and not all_exit

        L1=[Hisseler[i],round(Stats.loc['Win Rate [%]'],2),round(Stats.loc['Sharpe Ratio'],2),
            round(Stats.loc['Avg Winning Trade [%]'],2),str(Stats.loc['Avg Winning Trade Duration']),
            round(Stats.loc['Avg Losing Trade [%]'],2),str(Stats.loc['Avg Losing Trade Duration']),
            str(Buy),str(Sell)]

        print(L1)
        df_signals.loc[len(df_signals)] = L1
        if Buy==True and float(L1[1])>80.0:
            pf.plot(subplots = ['orders','trades','drawdowns','trade_pnl','cum_returns']).write_image((Hisseler[i]+"_Backtest.png"))
    except:
        pass

df_True = df_signals[(df_signals['Giriş Sinyali'] == 'True') & (df_signals['Kazanma Oranı[%]'] > 80.0)]
print(df_True.to_string())
