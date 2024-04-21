import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components
import pandas_ta as pta
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from fpdf import FPDF
import base64
from tempfile import NamedTemporaryFile
from yahoo_fin import stock_info as si
from streamlit_option_menu import option_menu

base="light"

def main():
    st.sidebar.title("İletişim Bilgileri")
    st.sidebar.subheader("Yazar:")
    st.sidebar.write("Serkan Polat")

    # İletişim bilgilerini sidebar içinde görüntüledim
    st.sidebar.subheader("E-posta:")
    st.sidebar.write("itsonlydatahustle@gmail.com")
    st.sidebar.subheader("Github:")
    st.sidebar.write("https://github.com/serkannpolatt")
    st.sidebar.subheader("Kaggle:")
    st.sidebar.write("https://www.kaggle.com/serkanp")
    st.sidebar.subheader("Daha fazlası için:")
    st.sidebar.write("https://bento.me/serkan-polat")

if __name__ == "__main__":
    main()



figs=[]

st.markdown(""" ## Hisse Senedi Fiyat Analizi ve Tahmini  """,unsafe_allow_html=True)
st.markdown(""" 
### Tüm stok ihtiyaçlarınızı tek bir yerde bulun
Hisse senedi hareketini daha iyi anlamak için sadece birkaç teknik gösterge sağlamakla kalmıyor, aynı zamanda gelecekteki fiyatı tahmin etmek için bir Sinir Ağ modelimiz var.""",unsafe_allow_html=True)

# Kullanıcıdan hisse senedi simgesini al
ticker = st.text_input("Hisse Senedi Göstergesi")

# Eğer bir simge girilmemişse, varsayılan olarak "EREGL" olarak ayarladım
if ticker == "":
    ticker = "XU100.IS"
# Girilen simgeyi görüntüle
st.write("BIST 100 için örnek sembol girişi: **PGSUS.IS**, **DOAS.IS** vb.")
st.write("S&P500 için örnek sembol girişi: **^GSPC**, **NVDA**, **TSLA**, **AMZN** vb.")

# Finansal API'den (Örn: Yahoo Finance) simgeye ait hisse verilerini aldım
df = si.get_data(ticker)
df["date"] = df.index

# Hisse DataFrame'inden gerekli verileri çıkardım
open_prices = df['open']
close_prices = df['close']
volumes = df['volume']
high_prices = df['high']
low_prices = df['low']
dates = df['date']
DATA_LEN = 300


# Her veri sütunu için son DATA_LEN sayısı kadar veri noktasını aldım
dates = dates[-DATA_LEN:].to_list()
close_prices = close_prices[-DATA_LEN:].to_list()
open_prices = open_prices[-DATA_LEN:].to_list()
volumes = volumes[-DATA_LEN:].to_list()
high_prices = high_prices[-DATA_LEN:].to_list()
low_prices = low_prices[-DATA_LEN:].to_list()

# İleriki hesaplamalar için 'close' sütununu seçtim
close_for_calc = df['close'][-DATA_LEN:]


st.text("");st.text("");st.text("")



st.markdown("## Teknik Göstergeler")

# Kapanış Fiyatı Görselleştirme
fig = plt.figure()
plt.title(f"{ticker} için kapanış fiyatları: {ticker} şu anda {round(close_prices[len(close_prices) - 1], 2)}", fontsize=15,color="black")
plt.xlabel("Gün Sonrası", fontsize=12,color="black")
plt.ylabel("Fiyat", fontsize=12,color="black")
plt.plot(close_prices, label='Kapanış Fiyatı')
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)
st.markdown("***")



# RSI 
relative_strength_indexs = pta.rsi(close_for_calc, length=14)
relative_strength_indexs = relative_strength_indexs.to_list()


fig = plt.figure()
plt.plot(relative_strength_indexs, label='RSI Değeri')
plt.title(f"14 günlük RSI ", fontsize=17, color="black")
plt.xlabel("Gün Sonrası", fontsize=15, color="black")
plt.ylabel("RSI Değeri", fontsize=15, color="black")
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)


st.text("")
st.markdown("Verilen grafikte, RSI > 70 aşırı alım hissesini ve RSI < 30 aşırı satım hissesini gösterir.")
st.markdown("***")


# Bollinger Bantları
# Kapanış fiyatlarının 5 günlük hareketli ortalamasını hesapladım
close_avg = close_for_calc.rolling(5).mean().to_list()

# Kapanış fiyatlarının 5 günlük hareketli standart sapmasını hesapladım
standard_deviations = close_for_calc.rolling(5).std().to_list()

upper_bollinger_band = []
lower_bollinger_band = []

# Her veri noktası için üst ve alt Bollinger Bantlarını hesapladım
for i in range(len(standard_deviations)):
    # Üst sınırı, kapanış ortalaması artı iki kat standart sapma olarak hesapladım
    upper_bound = close_avg[i] + (standard_deviations[i] * 2)

    # Alt sınırı, kapanış ortalamasından iki kat standart sapma çıkartarak hesapladım
    lower_bound = close_avg[i] - (standard_deviations[i] * 2)

    upper_bollinger_band.append(upper_bound)
    lower_bollinger_band.append(lower_bound)



fig = plt.figure()
plt.plot(close_avg, label='Basit Hareketli Ortalama',color="black")
plt.plot(upper_bollinger_band, label='Üst Bant')
plt.plot(lower_bollinger_band, label='Alt Bant')
plt.plot(close_prices, 'r', label='Kapanış Fiyatı')
plt.title("2 std'li Bollinger Bantları", fontsize=17,color="black")
plt.xlabel("Sonraki gün sayısı", fontsize=15,color="black")
plt.ylabel("Fiyat", fontsize=15,color="black")
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)
st.markdown("***")



# OBV 
on_balance_volumes = []
obv = 0

on_balance_volumes.append(obv)

# Her veri noktası için On-Balance Volume (OBV) değerini hesapladım
for i in range(1, len(volumes)):
    if close_prices[i] > close_prices[i - 1]:
        obv += volumes[i]
        on_balance_volumes.append(obv)

    elif close_prices[i] < close_prices[i - 1]:
        obv -= volumes[i]
        on_balance_volumes.append(obv)

    else:
        obv += 0
        on_balance_volumes.append(obv)


NUM_OF_DAYS_2 = 5
obv_df = pd.DataFrame(on_balance_volumes)
obv_sma = obv_df.rolling(NUM_OF_DAYS_2).mean()



fig = plt.figure()
plt.plot(on_balance_volumes, label='OBV')
plt.plot(obv_sma, label=' OBV için Basit Hareketli Ortalama')
plt.title("OBV (On Balance Volume)  Bakiye Hacmi", fontsize=17,color="black")
plt.xlabel("Sonraki gün sayısı", fontsize=15,color="black")
plt.ylabel("OBV", fontsize=15,color="black")
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)

st.markdown("***")


# MACD
ema12 = close_for_calc.ewm(span=12, adjust=False).mean()
ema26 = close_for_calc.ewm(span=26, adjust=False).mean()

macd = ema12 - ema26

signal = macd.ewm(span=9, adjust=False).mean()

fig = plt.figure()
plt.plot(macd.to_list(), label='MACD')
plt.plot(signal.to_list(), label='Signal')
plt.title("Hareketli Ortalama Yakınsama Farklılığı", fontsize=17,color="black")
plt.ylabel("MACD", fontsize=15,color="black")
plt.xlabel("Gün Sonrası", fontsize=15,color="black")
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)

st.markdown("***")



# Momentum
MOMENTUM_PERIOD = 10

momentum_values = []

# Her veri noktası için momentum değerlerini hesapladım
for i in range(MOMENTUM_PERIOD, len(close_prices)):
    curr_close_price = close_prices[i]
    period_start_close_price = close_prices[i - MOMENTUM_PERIOD]

    # Momentumu, mevcut kapanış fiyatı ile dönem başından itibaren fiyat arasındaki fark olarak hesapladım
    momentum_values.append(curr_close_price - period_start_close_price)

momentum_sum = 0

# Momentum değerlerinin toplamını hesapladım
for i in range(len(momentum_values)):
    momentum_sum += momentum_values[i]

# Ortalama momentumu hesapladım
avg_momentum = momentum_sum / len(momentum_values)

fig = plt.figure()
plt.plot(momentum_values, label='Momentum Values')
plt.title(f"{MOMENTUM_PERIOD} gün boyunca hisse senedinin ivmesi ", fontsize=17,color="black")
plt.ylabel("Momentum", fontsize=15,color="black")
plt.xlabel("Gün Sonrası", fontsize=15,color="black")
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)




pivot_points = []
# Her veri noktası için pivot noktalarını hesapladım
for i in range(len(close_for_calc)):
    if i == 0:
        pivot_points.append(float("nan"))  # İlk pivot noktasını NaN olarak ayarladım
    else:
        prev_high = high_prices[i - 1]
        prev_low = low_prices[i - 1]
        prev_close = close_prices[i - 1]

        # Pivot noktasını önceki yüksek, düşük ve kapanış fiyatlarının ortalaması olarak hesapladım
        pivot_point = (prev_high + prev_low + prev_close) / 3
        pivot_points.append(pivot_point)



resistance_1 = []
support_1 = []
resistance_2 = []
support_2 = []


# Pivot noktalarına göre destek ve direnç seviyelerini hesapladım
for i in range(len(pivot_points)):
    if i == 0:
        resistance_1.append(float("nan"))  # İlk direnç seviyesini NaN olarak ayarladım
        support_1.append(float("nan"))  # İlk destek seviyesini NaN olarak ayarladım
    else:
        prev_high = high_prices[i - 1]
        prev_low = low_prices[i - 1]

        # Birinci direnç ve destek seviyelerini hesapladım
        r1 = (2 * pivot_points[i]) - prev_low
        s1 = (2 * pivot_points[i]) - prev_high

        # İkinci direnç ve destek seviyelerini hesapla
        r2 = pivot_points[i] + (prev_high - prev_low)
        s2 = pivot_points[i] - (prev_high - prev_low)

        resistance_1.append(r1)
        support_1.append(s1)
        resistance_2.append(r2)
        support_2.append(s2)


fig = plt.figure()
plt.plot(close_prices, label='Kapanış Fiyatı')
plt.plot(resistance_1, label='Direnç (birinci)')
plt.plot(support_1, label='Destek (birinci)')
plt.plot(resistance_2, label='Direnç (ikinci)')
plt.plot(support_2, label='Destek (ikinci)')
plt.title("Destek ve Direnç", fontsize=17, color="black")
plt.xlabel("Gün Sonrası", fontsize=15, color="black")
plt.ylabel("Fiyat", fontsize=15, color="black")
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)



st.text("")
st.markdown("Destek ve dirençleri daha iyi görmek için lütfen grafiği yakınlaştırın.")
st.markdown("***")



st.markdown("## Gelecek Fiyat Tahminleri")

# Veri kümesini hazırla
dataset = close_prices

dataset = np.array(dataset)
training = len(dataset)
dataset = np.reshape(dataset, (dataset.shape[0], 1))

# Veri kümesini ölçeklendir
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

train_data = scaled_data[0:int(training), :]

# Özellikleri ve etiketleri hazırla
x_train = []
y_train = []
prediction_days = 60

for i in range(prediction_days, len(train_data)):
    x_train.append(train_data[i-prediction_days:i, 0])
    y_train.append(train_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)

# Handle missing values in X (replace NaN with mean)
x_train = np.nan_to_num(x_train, nan=np.nanmean(x_train))
# Handle missing values in y (replace NaN with mean)
y_train = np.nan_to_num(y_train, nan=np.nanmean(y_train))

# Doğrusal Regresyon modelini eğit
reg = LinearRegression().fit(x_train, y_train)

x_tomm = close_prices[len(close_prices) - prediction_days:len(close_prices)]
x_tomm = np.array(x_tomm)
x_tomm_reshaped = x_tomm.reshape(-1, 1)

# Yeniden şekillendirilmiş veriyi ölçeklendir
x_tomm_scaled = scaler.transform(x_tomm_reshaped)

# Ölçeklenmiş veriyi tekrar (1, n_features) şekline getir
x_tomm_scaled_reshaped = x_tomm_scaled.reshape(1, -1)

# Handle missing values in future predictions (replace NaN with mean)
x_tomm_scaled_reshaped = np.nan_to_num(x_tomm_scaled_reshaped, nan=np.nanmean(x_tomm_scaled_reshaped))

# Tahmin yap
prediction = reg.predict(x_tomm_scaled_reshaped)
prediction = scaler.inverse_transform(prediction.reshape(1, -1))

# Tahmini göster
st.markdown(f"#### Yarının tahmini için: {ticker} = {round(prediction[0][0], 2)}")

st.markdown("***")

# Kullanıcıdan gelecek gün sayısı girişi (20'yi geçmemesi önerilir)
FUTURE_DAYS = st.text_input("Gelecek gün sayısını girin (20'yi geçmemesi önerilir)")

try:
    FUTURE_DAYS = int(FUTURE_DAYS)
except:
    FUTURE_DAYS = 10

predicted_prices = []
tot_prices = list(close_prices)

# Belirtilen gün sayısı için gelecekteki fiyatları tahmin et
for i in range(FUTURE_DAYS):
    x_prices = tot_prices[len(tot_prices) - prediction_days: len(tot_prices)]
    x_prices_reshaped = np.array(x_prices).reshape(1, -1)
    
    x_prices_scaled = np.zeros_like(x_prices_reshaped)
    for j in range(x_prices_reshaped.shape[1]):
        feature = x_prices_reshaped[:, j]
        feature_scaled = scaler.transform(feature.reshape(-1, 1))
        x_prices_scaled[:, j] = feature_scaled.flatten()
    
    # Handle missing values in future predictions (replace NaN with mean)
    x_prices_scaled = np.nan_to_num(x_prices_scaled, nan=np.nanmean(x_prices_scaled))
    
    prediction = reg.predict(x_prices_scaled)
    
    prediction_inverse_scaled = scaler.inverse_transform(prediction.reshape(-1, 1))
    
    tot_prices = np.concatenate((tot_prices, prediction_inverse_scaled.flatten()))
    predicted_prices.append(prediction_inverse_scaled)

tot_prices = np.array(tot_prices)
predicted_prices = np.array(predicted_prices)

tot_prices = np.reshape(tot_prices, (tot_prices.shape[0]))
predicted_prices = np.reshape(predicted_prices, (predicted_prices.shape[0]))

print(len(close_prices))
print(len(tot_prices))


fig = plt.figure()
plt.plot(tot_prices, label='Tahmin Edilen Gelecek Fiyatlar')
plt.plot(close_prices, label='Şimdiki fiyatlar')
plt.xlabel("Gün Sonrası", fontsize=15, color="black")
plt.ylabel("Fiyat", fontsize=15, color="black")
plt.title("Gelecek Fiyat Tahminleri", fontsize=17, color="black")
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)




# PDF İndirme İşlevselliği
def create_download_link(val, filename):
    b64 = base64.b64encode(val)  
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Dosyayı indir</a>'

st.text("")
export_as_pdf = st.button("Raporu PDF Olarak Dışa Aktar")

FONT_FAMILY = "Arial"
WIDTH = 210
HEIGHT = 297
name = ""

if export_as_pdf:
    # Yeni bir PDF örneği oluştur
    pdf = FPDF()
    pdf.add_page()

    # Ana başlık için yazı tipini ve boyutunu ayarla
    pdf.set_font(FONT_FAMILY, size=30)
    pdf.ln(40)
    pdf.multi_cell(w=0, h=15, txt=f"Hisse senedi analizi: {ticker}", align='C')  # 'C' parametresi ile metni ortala
    pdf.ln(60)

    # Giriş için yeni bir sayfa ekle
    pdf.ln(40)
    pdf.add_page()
    pdf.set_font(FONT_FAMILY, size=30)
    pdf.cell(0, txt="Giris")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=15)
    pdf.multi_cell(w=0, h=7, txt=f"Bu rapor, {ticker} hissesini cesitli teknik gostergeleri ve diger teknikleri kullanarak analiz edecek ve verilen hissenin gelecekteki egilimleri hakkinda fikir verecektir.")
    pdf.ln(50)
    pdf.ln(50)

    # Kullanılan göstergeler için yeni bir sayfa ekle
    pdf.set_font(FONT_FAMILY, size=30)
    pdf.cell(0, txt="Kullanilan Gostergeler")
    pdf.ln(30)

    # Göstergelerin bir listesini tanımla
    indicators = ["RSI", 
                "Bollinger Bantlari", 
                "OBV", 
                "MACD", 
                "Momentum"]

    pdf.set_font(FONT_FAMILY, size=20)

    for i in range(len(indicators)):
        pdf.cell(0, txt=f"{i + 1}. {indicators[i]}")
        pdf.ln(10)  # Her gösterge başlığından sonra 6 birim yüksekliğinde bir boşluk bırakır


    pdf.add_page()
    pdf.ln(5)
    pdf.set_font(FONT_FAMILY, size=30)
    pdf.cell(0, txt="RSI")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=12)
    pdf.multi_cell(w=0, h=7,
                   txt=f"RSI veya Goreceli Güc Endeksi, bir hissenin asiri alim veya asiri satim durumunu gosterir. RSI >= 70, bir hissenin asiri alindigini ve fiyatda bir dusus olabilecegini gosterirken, RSI <= 30, bir hissenin asiri satildigini ve yakin bir gelecekte boga egilimi gosterebilecegini gosterir.")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=20)
    pdf.multi_cell(w=0, h=10, txt=f"RSI grafigi, {ticker} icin bir yil boyunca asagida verilmistir:")
    pdf.ln(8)

    # RSI grafiğini geçici bir resim dosyası olarak kaydet
    with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        figs[1].savefig(tmpfile.name)
        name = tmpfile.name

    pdf.image(name, 12, 100, WIDTH - 20, 100)
    name = ""
    pdf.ln(115)
    pdf.set_font(FONT_FAMILY, size=12)

    curr_rsi = relative_strength_indexs[len(relative_strength_indexs) - 1]
    rsi_mean = pd.Series(relative_strength_indexs).mean()

    rsi_state_rel = f"high" if curr_rsi > rsi_mean + 2.5 else f"low"
    rsi_state_abs = f"low" if curr_rsi < 45 else (f"medium" if curr_rsi < 60 else f"high")
    sell_state = f"selling" if rsi_state_abs == "low" else f"buying"
    price_action_dir = f"upward" if sell_state == "selling" else f"downward"

    pdf.multi_cell(w=0, h=7,    
                   txt=f"Mevcut RSInin {round(curr_rsi, 2)} oldugu goruluyor ki bu, bir yil suren hisse senedi egilimine gore {rsi_state_rel} olarak kabul edilir. Normal bir senaryoda boyle bir RSI, {rsi_state_abs} olarak kabul edilir. Bu nedenle bu, daha fazla {sell_state} oldugunu ve yakin bir gelecekte {price_action_dir} bir egilim olabilecegini gosterir. Unutmayin ki bu, sirket veya sirketin genel performansi veya karliligi hakkindaki insanlarin duygularini dikkate almayan yalnizca bir teknik gosterge oldugu icin bu stratejiyi kullanmanin bir riski vardir. Bu, sadece bu gosterge icin degil, bundan sonraki tum diger gostergeler icin de gecerlidir.")
    pdf.add_page()
    pdf.ln(5)
    pdf.set_font(FONT_FAMILY, size=30)
    pdf.cell(0, txt="Bollinger Bantlari")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=12)
    pdf.multi_cell(w=0, h=7,
                   txt=f"Bollinger bantlarini kullanarak borsadaki oynaklik ve hareket halindeki onemli trendlerin olup olmadigi hakkinda fikir edinilebilir. Bollinger bantlari RSI ile desteklendiginde bize hisse senedinin durumu hakkinda cok net bir resim veriyor.")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=12)
    pdf.multi_cell(
        w=0, h=7, txt=f"Bollinger bantlari kullanarak hisse senedi piyasasinin volatilitesi hakkinda bir fikir edinmek mumkun ve herhangi bir buyuk trendin olup olmadigini takip etmek mumkun. RSI ile birlestirildiginde, bir hissenin durumu hakkinda cok net bir resim elde edebiliriz.")
    pdf.ln(10)
    with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        figs[2].savefig(tmpfile.name)
        name = tmpfile.name

    pdf.image(name,
              12, 90, WIDTH - 20, 100)
    name = ""
    pdf.ln(100)
    pdf.set_font(FONT_FAMILY, size=12)

    close_price_sma_status = "above" if close_prices[len(close_prices) - 1] > close_avg[len(close_avg) - 1] else "below"
    close_sma_stat_msg = "bu, hisse senedinin 5 gunluk SMA donemi uzerinde boga egilimi gosterdigi anlamina gelir." if close_price_sma_status == "uzerinde" else "bu, hisse senedinin yakin gecmiste veya 5 gunluk SMA donemi boyunca dusus gosterdigi anlamina gelir." if close_price_sma_status == "above" else "bu, hisse senedinin yakin zamanda veya SMA donemi boyunca dusus egilimi gosterdigi anlamina gelir"
    pdf.ln(20)
    pdf.multi_cell(w=0, h=7,
                   txt=f"Bu durumda, mevcut kapanis fiyatinin 5 gunluk bir donem uzerinde oldugunu gorebiliriz. {close_sma_stat_msg}")
    
    pdf.ln(20)

    closer_band = "upper band" if abs(
        upper_bollinger_band[len(upper_bollinger_band) - 1] - close_prices[len(close_prices) - 1]) < abs(
        lower_bollinger_band[len(lower_bollinger_band) - 1] - close_prices[len(close_prices) - 1]) else "lower band"

    print(abs(upper_bollinger_band[len(upper_bollinger_band) - 1] - close_prices[len(close_prices) - 1]))
    print(abs(lower_bollinger_band[len(
        lower_bollinger_band) - 1] - close_prices[len(close_prices) - 1]))

    pdf.multi_cell(w=0, h=7,
                   txt=f"Artik devam edip ust ve alt bollinger bantlarina bakabiliriz. Sectigimiz hisse senedinin {closer_band} bandina daha yakin oldugunu gorebiliriz. Buna bakarak hisse senedinin egilimini ve gucunu tespit edebiliriz. Boylece bu, RSI gostergemizi cok sorunsuz bir sekilde tamamliyor.")

    pdf.add_page()
    pdf.ln(5)
    pdf.set_font(FONT_FAMILY, size=30)
    pdf.cell(0, txt="OBV")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=12)
    pdf.multi_cell(w=0, h=7,
                   txt=f"OBV veya On Balance Volume, bir varligin toplam islem hacmi hakkinda bir fikir edinmek ve hareket edip etmedigini takip etmek icin kullanilabilir. Bir hissenin OBV'sindeki herhangi buyuk hareketler, buyuk kurumsal yatirimcilar tarafindan yapilan herhangi hareketleri takip etmek icin kullanilabilir.")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=20)
    pdf.multi_cell(
        w=0, h=10, txt=f"{ticker} icin bir yil boyunca OBV'nin bir gorsellestirmesi:")
    pdf.ln(3)
    with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        figs[3].savefig(tmpfile.name)
        name = tmpfile.name

    pdf.image(name,
              12, 90, WIDTH - 20, 100)
    name = ""
    pdf.ln(120)
    pdf.set_font(FONT_FAMILY, size=12)
    pdf.ln(30)
    pdf.multi_cell(w=0, h=7,
                   txt=f'Bu durumda, son OBV trendine bakarsak, buyuk kurumsal yatirimcilarla sadece siradan yatirimcilar arasindaki genel gorunum hakkinda iyi bir fikir edinebiliriz. Ayrica, OBV gostergesi herhangi baska ayrinti gerektirmez.')

    pdf.add_page()
    pdf.ln(5)
    pdf.set_font(FONT_FAMILY, size=30)
    pdf.cell(0, txt="MACD")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=12)
    pdf.multi_cell(w=0, h=7,
                   txt="MACD gostergesi bize hisse senedinin trendi hakkinda iyi bir fikir veriyor. MACD degerindeki artis sunu gosterir: "
                       "Fiyatin gosterdigi ve muhtemelen isaretin artan bir egilim gosterdigini varsayarsak, bunun tersi de dogrudur. Ayrica "
                       "MACD ile sinyal cizgisinin kesismesinin yeni bir trendin baslangicini gosterdigine dikkat edilmelidir.")

    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=20)
    pdf.multi_cell(
        w=0, h=10, txt=f"{ticker} icin bir yil boyunca Momentum'un bir gorsellestirmesi:")
    pdf.ln(3)
    with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        figs[4].savefig(tmpfile.name)
        name = tmpfile.name

    pdf.image(name,
              11, 100, WIDTH - 20, 100)
    name = ""

    pdf.add_page()
    pdf.ln(5)
    pdf.set_font(FONT_FAMILY, size=30)
    pdf.cell(0, txt="Momentum")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=12)
    pdf.multi_cell(w=0, h=7,
                   txt=f"Adi gibi Momentum gostergesi bize bir hisse senedinin momentumu, yani bir hisse senedinin sahip oldugu trendin gucu hakkinda fikir verir. Momentuma bakarak bir alim, satim, yukselis veya dusus egiliminin ne kadar sure devam edecegini belirleyebiliriz.")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=20)
    pdf.multi_cell(
        w=0, h=10, txt=f"{ticker} icin bir yil boyunca OBVnin bir gorsellestirmesi:")
    pdf.ln(3)
    with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        figs[5].savefig(tmpfile.name)
        name = tmpfile.name

    pdf.image(name,
              12, 90, WIDTH - 20, 100)
    name = ""
    pdf.ln(110)
    pdf.set_font(FONT_FAMILY, size=12)

    momentum_over_0 = "over zero" if momentum_values[len(momentum_values) - 1] > 0 else "below zero"
    curr_momentum = momentum_values[len(momentum_values) - 1]
    pdf.ln(30)
    pdf.multi_cell(
        w=0, h=7,
        txt=f"Son momentum degerlerine baktigimizda, hissenin momentumunu kolayca cikarabiliriz. Hissenin mevcut momentumu {round(curr_momentum, 2)} ve yil boyunca ortalama momentumu {round(avg_momentum, 2)}.")


    pdf.add_page()
    pdf.ln(5)
    pdf.set_font(FONT_FAMILY, size=30)
    pdf.cell(0, txt="Gelecek Fiyat Tahmini")
    pdf.ln(30)
    pdf.set_font(FONT_FAMILY, size=20)
    pdf.multi_cell(
        w=0, h=10, txt=f"Makine Ogrenimi modelimizin {FUTURE_DAYS} gun boyunca {ticker} ile ilgili tahmini:")
    pdf.ln(10)
    with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        figs[7].savefig(tmpfile.name)
        name = tmpfile.name

    pdf.image(name,
              12, 70, WIDTH - 20, 100)
    name = ""
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), f"{ticker} analizi")
    st.markdown(html, unsafe_allow_html=True)
    st.text("")
    
