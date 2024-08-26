import pandas as pd
import pandas_ta as ta
import numpy as np
import matplotlib.pyplot as plt
from tvDatafeed import TvDatafeed, Interval
from backtesting import Backtest, Strategy
from tradingview_screener import get_all_symbols
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def MOST(data, percent, n1):
    df = data.copy()  # Working with a copy to avoid modifying the original DataFrame
    percent = percent / 100
    df['EMA'] = ta.ema(df['Close'], length=n1)  # Calculate EMA
    df['tempema'] = 0.0  # Initialize temporary EMA
    df['trend'] = -1  # Initialize trend
    df['MOST'] = 0.0  # Initialize MOST indicator
    df = df.dropna()
    df = df.reset_index()

    for i in range(1, len(df)):
        if df['trend'][i - 1] == 1:
            df.loc[i, 'tempema'] = max(df['tempema'][i - 1], df['EMA'][i])
        elif df['trend'][i - 1] == -1:
            df.loc[i, 'tempema'] = min(df['tempema'][i - 1], df['EMA'][i])

        if df['EMA'][i] >= df['MOST'][i - 1] and df['trend'][i - 1] == 1:
            df.loc[i, 'trend'] = 1
            df.loc[i, 'MOST'] = df['tempema'][i] * (1 - percent)
        elif df['EMA'][i] <= df['MOST'][i - 1] and df['trend'][i - 1] == -1:
            df.loc[i, 'trend'] = -1
            df.loc[i, 'MOST'] = df['tempema'][i] * (1 + percent)
        elif df['EMA'][i] >= df['MOST'][i - 1] and df['trend'][i - 1] == -1:
            df.loc[i, 'trend'] = 1
            df.loc[i, 'MOST'] = df['tempema'][i] * (1 - percent)
        elif df['EMA'][i] <= df['MOST'][i - 1] and df['trend'][i - 1] == 1:
            df.loc[i, 'trend'] = -1
            df.loc[i, 'MOST'] = df['tempema'][i] * (1 + percent)

    df['Entry'] = df['trend']==1
    df['Exit'] = df['trend']==-1
    return df

tv = TvDatafeed()
Hisseler = get_all_symbols(market='turkey')
Hisseler = [symbol.replace('BIST:', '') for symbol in Hisseler]
Hisseler = sorted(Hisseler)

#Raporlama için kullanılacak başlıklar
Titles = ['Hisse Adı', 'Son Fiyat','MOST Değeri' ,'Kazanma Oranı','Giriş Sinyali', 'Çıkış Sinyali']

df_signals = pd.DataFrame(columns=Titles)

#Backtest için gerekli class yapısı
class MacdStrategy(Strategy):
    def init(self):
        pass
    def next(self):
        if self.data['Entry'] == True and not self.position:
            self.buy()

        elif self.data['Exit'] == True:
            self.position.close()

for i in range(0,len(Hisseler)):
    #print(Hisseler[i])
    try: 
        data = tv.get_hist(symbol=Hisseler[i], exchange='BIST', interval=Interval.in_1_hour, n_bars=500)
        data.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'}, inplace=True)
        data = data.reset_index() 
        MostTrend=MOST(data,2,14)
        MostTrend['datetime'] = pd.to_datetime(MostTrend['datetime'])  # Assuming 'Date' is the name of your datetime column
        MostTrend.set_index('datetime', inplace=True)
        bt = Backtest(MostTrend, MacdStrategy, cash=100000, commission=0.002)
        Stats = bt.run()
        Buy=False
        Sell=False
        Signals = MostTrend.tail(2)
        Signals = Signals.reset_index()
        Buy = Signals.loc[0, 'Entry'] == False and Signals.loc[1, 'Entry'] ==True
        Sell = Signals.loc[0, 'Exit'] == False and Signals.loc[1, 'Exit'] == True
        Last_Price = Signals.loc[1, 'Close']
        L1 = [Hisseler[i],Last_Price,round(Signals.loc[1,'MOST'],2) ,round(Stats.loc['Win Rate [%]'], 2), str(Buy), str(Sell)]
        df_signals.loc[len(df_signals)] = L1
        print(L1)
    except:
        pass

df_True = df_signals[(df_signals['Giriş Sinyali'] == 'True')]
print(df_True)
