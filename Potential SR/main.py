import pandas as pd
import pandas_ta as ta
import ssl
from urllib import request
import requests
from scipy.signal import argrelextrema
import numpy as np
import matplotlib.pyplot as plt

def Hisse_Temel_Veriler():
    url1="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/Temel-Degerler-Ve-Oranlar.aspx#page-1"
    context = ssl._create_unverified_context()
    response = request.urlopen(url1, context=context)
    url1 = response.read()
    df = pd.read_html(url1,decimal=',', thousands='.')                         #Tüm Hisselerin Tablolarını Aktar
    df=df[6]
    Hisseler=df['Kod'].values.tolist()
    return Hisseler

def Stock_Prices(Hisse,period=120,Bar=100):
    url = f"https://www.isyatirim.com.tr/_Layouts/15/IsYatirim.Website/Common/ChartData.aspx/IntradayDelay?period={period}&code={Hisse}.E.BIST&last={Bar}"
    r1 = requests.get(url).json()
    data = pd.DataFrame.from_dict(r1)
    data[['Volume', 'Close']] = pd.DataFrame(data['data'].tolist(), index=data.index)
    data.drop(columns=['data'], inplace=True)
    return data

def Support_and_Resistance(data, order=45,pct=2):
    df = data.copy()
    hh_pairs_indices = argrelextrema(df['Close'].values, comparator=np.greater, order=order)[0]
    hh_pairs = [hh_pairs_indices[i:i+2] for i in range(len(hh_pairs_indices) - 1)]

    ll_pairs_indices = argrelextrema(df['Close'].values, comparator=np.less, order=order)[0]
    ll_pairs = [ll_pairs_indices[i:i+2] for i in range(len(ll_pairs_indices) - 1)]

    for pair in hh_pairs:
        df.loc[pair[0], 'HH_Pairs'] = df.loc[pair[1], 'Close']

    for pair in ll_pairs:
        df.loc[pair[0], 'LL_Pairs'] = df.loc[pair[1], 'Close']

    hh_df = df[df['HH_Pairs'].notna()]
    ll_df = df[df['LL_Pairs'].notna()]
    hh_df_sorted = pd.DataFrame(hh_df.sort_values(by='HH_Pairs').reset_index(drop=True)['HH_Pairs'])
    ll_df_sorted = pd.DataFrame(ll_df.sort_values(by='LL_Pairs').reset_index(drop=True)['LL_Pairs'])
   
    hh_df_mean_list = []
    Iterative_df = hh_df_sorted.copy()  # Create a copy to iterate without modifying the original DataFrame
    first_value = Iterative_df['HH_Pairs'].iloc[0]
    pct_range = first_value * 1.1
    hh_near_values = Iterative_df[Iterative_df['HH_Pairs'] <= pct_range]
    while not hh_near_values.empty:
        hh_df_mean = hh_near_values['HH_Pairs'].mean()
        hh_df_mean_list.append(hh_df_mean)
        Iterative_df = Iterative_df.drop(hh_near_values.index)
        if not Iterative_df.empty:  # Check if Iterative_df is not empty after dropping rows
            first_value = Iterative_df['HH_Pairs'].iloc[0]
            pct_range = first_value * 1.05
            hh_near_values = Iterative_df[Iterative_df['HH_Pairs'] <= pct_range]
        else:
            break  # Exit the loop if Iterative_df is empty
       
    ll_df_mean_list = []
    Iterative_df = ll_df_sorted.copy()
    first_value = Iterative_df['LL_Pairs'].iloc[0]
    pct_range = first_value * 1.1
    ll_near_values = Iterative_df[Iterative_df['LL_Pairs'] <= pct_range]    
    while not ll_near_values.empty:
        ll_df_mean = ll_near_values['LL_Pairs'].mean()
        ll_df_mean_list.append(ll_df_mean)
        Iterative_df = Iterative_df.drop(ll_near_values.index)
        if not Iterative_df.empty:  # Check if Iterative_df is not empty after dropping rows
            first_value = Iterative_df['LL_Pairs'].iloc[0]
            pct_range = first_value * 1.05
            ll_near_values = Iterative_df[Iterative_df['LL_Pairs'] <= pct_range]
        else:
            break  # Exit the loop if Iterative_df is empty
    pos=0
    last_Close_value = df['Close'].iloc[-1]
    previous_Close_value =df['Close'].iloc[-2]
    Closest_hh_values = sorted(hh_df_mean_list, key=lambda x: abs(x - last_Close_value))[:3]
    Closest_ll_values = sorted(ll_df_mean_list, key=lambda x: abs(x - last_Close_value))[:3]

    hh_distances = [abs(value - last_Close_value) for value in Closest_hh_values]
    hh_distances = (min(hh_distances)/last_Close_value)*100
    ll_distances = [abs(value - last_Close_value) for value in Closest_ll_values]
    ll_distances = (min(ll_distances)/last_Close_value)*100
    pos=0
    if hh_distances < pct and (last_Close_value>previous_Close_value):
        print('Potential Resistance detected')
        pos=-1
    
    if ll_distances < pct and(last_Close_value<previous_Close_value):
        print('Potential Support Detected')
        pos=1

    return  pos,Closest_hh_values,Closest_ll_values

def Plot_SR(Hisse,data,Closest_hh_values,Closest_ll_values,n):
    df=data.copy()
    # Plotting the 'Close' values
    last_SR_value = df['Close'].iloc[-n]
    last_value = df['Close'].iloc[-1]
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Close'], label='Close')

    # Adding horizontal lines for Closest_hh_values
    for hh_value in Closest_hh_values:
        plt.axhline(y=hh_value, color='r', linestyle='--', label=f'Yakın Direnç: {hh_value:.2f}')

    # Adding horizontal lines for Closest_ll_values
    for ll_value in Closest_ll_values:
        plt.axhline(y=ll_value, color='g', linestyle='--', label=f'Yakın Destek: {ll_value:.2f}')
    plt.scatter(df.index[-n], last_SR_value, color='b', marker='o', label=f'Last SR Close: {last_SR_value:.2f}')
    plt.scatter(df.index[-n], last_SR_value, color='b', marker='o', label=f'Last Close: {last_value:.2f}')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(f'{Hisse} Support and Resistance Levels')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{Hisse}_Destek_Direnç.png', bbox_inches='tight', dpi=200)

Hisseler=Hisse_Temel_Veriler()

Titles=['Hisse Adı','SR Durumu','SR Açıklama']
df_signals=pd.DataFrame(columns=Titles)

for i in range(0,len(Hisseler)):
    print(Hisseler[i])
    try:
        P=120
        B=1000
        n=5
        data=Stock_Prices(Hisseler[i],period=P,Bar=B)
        SRPos,Closest_hh,Closest_ll = Support_and_Resistance(data.iloc[:-n],45,1)
        Comment=0
        if SRPos ==-1:
            Comment='Potensiyel Dirençe Yakın'
        if SRPos == 1:
            Comment='Potensiyel Desteğe Yakın'     
        L=[Hisseler[i],SRPos,Comment]
        df_signals.loc[len(df_signals)] = L

        if SRPos!=0:
            Plot_SR(Hisseler[i],data,Closest_hh,Closest_ll,n)
    except:
        pass

filtered_df = df_signals[df_signals['SR Durumu'] != 0]
print(filtered_df.to_string())
