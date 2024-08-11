import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import datetime

# Uygulama başlığı
st.title("📈 Hisse Senedi Trend Tahmincisi")

# Hisse sembolü giriş
hisse_sembolu = st.text_input("Hisse Sembolü Giriniz", "EREGL.IS")
baslangic = st.date_input("Başlangıç Tarihi", datetime.date(2021, 1, 1))
bitis = st.date_input("Bitiş Tarihi", datetime.date(2024, 1, 1))
sat_threshold = float(st.text_input("Satış Eşiği Giriniz", "0.1"))
al_threshold = float(st.text_input("Alış Eşiği Giriniz", "0.9"))

# Veri indirme ve hazırlama
veri = yf.download(hisse_sembolu, start=baslangic, end=bitis)
veri = veri.reset_index()

st.subheader(f"📅 {baslangic} - {bitis} Tarihleri Arasındaki Veri")
st.write(veri)

st.subheader("📊 Kapanış Fiyatı vs Zaman Grafiği")

# EMA hesaplamaları
ema_donemler = [5, 25, 50, 99, 200]
renkler = ["#FF6347", "#4682B4", "#32CD32", "#FFD700", "#8A2BE2"]
for donem in ema_donemler:
    kolon_adi = f"EMA_{donem}"
    veri[kolon_adi] = veri["Adj Close"].ewm(span=donem, adjust=False).mean()

for i in ["5", "25", "50", "99", "200"]:
    veri[f"fiyat_ema{i}_uzaklik"] = (
        (veri["Adj Close"] - veri[f"EMA_{i}"]) / veri["Adj Close"]
    ) * 100

fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(
    veri.index, veri["Adj Close"], label="Kapanış Fiyatı", color="#1f77b4", linewidth=2
)

# EMA grafiklerini ekle
for i, donem in enumerate(ema_donemler):
    kolon_adi = f"EMA_{donem}"
    ax.plot(
        veri.index,
        veri[kolon_adi],
        label=f"EMA {donem}",
        color=renkler[i],
        linestyle="--",
    )

ax.set_title(f"{hisse_sembolu} Fiyatı ve Üssel Hareketli Ortalamalar", fontsize=16)
ax.set_xlabel("Tarih", fontsize=12)
ax.set_ylabel("Fiyat", fontsize=12)
ax.legend()
ax.grid(True, linestyle="--", alpha=0.7)
st.pyplot(fig)

# Ekstra özelliklerin hesaplanması
veri["Fiyat_Hareketi"] = ((veri["Close"] - veri["Open"]) / veri["Open"]) * 100
veri["Normalize_Fiyat_Hareketi"] = (veri["Close"] - veri["Low"].min()) / (
    veri["High"].max() - veri["Low"].min()
)


def rsi_hesapla(veri, donem=14):
    kapanis_fiyatlari = veri["Adj Close"]
    fiyat_farki = kapanis_fiyatlari.diff(1)
    kazanc = fiyat_farki.where(fiyat_farki > 0, 0)
    kayip = -fiyat_farki.where(fiyat_farki < 0, 0)
    ort_kazanc = kazanc.rolling(window=donem).mean()
    ort_kayip = kayip.rolling(window=donem).mean()
    goreceli_guc = ort_kazanc / ort_kayip
    rsi = 100 - (100 / (1 + goreceli_guc))
    return rsi


veri["RSI"] = rsi_hesapla(veri)


def macd_hesapla(veri, kisa_donem=12, uzun_donem=26, sinyal_donemi=9):
    kisa_ema = veri["Adj Close"].ewm(span=kisa_donem, adjust=False).mean()
    uzun_ema = veri["Adj Close"].ewm(span=uzun_donem, adjust=False).mean()
    macd = kisa_ema - uzun_ema
    sinyal = macd.ewm(span=sinyal_donemi, adjust=False).mean()
    return macd, sinyal


veri["MACD"], veri["Sinyal"] = macd_hesapla(veri)


def stochrsi_hesapla(veri, donem=14, stoch_donem=14, smooth_k=3, smooth_d=3):
    rsi = rsi_hesapla(veri, donem)
    stochrsi = (rsi - rsi.rolling(window=stoch_donem).min()) / (
        rsi.rolling(window=stoch_donem).max() - rsi.rolling(window=stoch_donem).min()
    )
    stoch_k = stochrsi.rolling(window=smooth_k).mean()
    stoch_d = stoch_k.rolling(window=smooth_d).mean()
    return stoch_k, stoch_d


veri["StochRSI_K"], veri["StochRSI_D"] = stochrsi_hesapla(veri)
veri.dropna(inplace=True)


def yerel_ekstremumlari_bul(
    Tarih,
    Normalize_Fiyat_Hareketi,
    Fiyat,
    RSI,
    MACD,
    Sinyal,
    fiyat_ema5_uzaklik,
    fiyat_ema25_uzaklik,
    fiyat_ema50_uzaklik,
    fiyat_ema99_uzaklik,
    fiyat_ema200_uzaklik,
    pencere_boyutu=3,
):
    n = len(Fiyat)
    yerel_ekstremumlar = []
    for i in range(pencere_boyutu, n - pencere_boyutu):
        if all(
            Normalize_Fiyat_Hareketi[i - j] < Normalize_Fiyat_Hareketi[i]
            for j in range(1, pencere_boyutu + 1)
        ) and all(
            Normalize_Fiyat_Hareketi[i] > Normalize_Fiyat_Hareketi[i + k]
            for k in range(1, pencere_boyutu + 1)
        ):
            yerel_ekstremumlar.append(
                (
                    Tarih[i],
                    Normalize_Fiyat_Hareketi[i],
                    Fiyat[i],
                    RSI[i],
                    MACD[i],
                    Sinyal[i],
                    fiyat_ema5_uzaklik[i],
                    fiyat_ema25_uzaklik[i],
                    fiyat_ema50_uzaklik[i],
                    fiyat_ema99_uzaklik[i],
                    fiyat_ema200_uzaklik[i],
                    1,
                )
            )
    for i in range(pencere_boyutu, n - pencere_boyutu):
        if all(
            Normalize_Fiyat_Hareketi[i - j] > Normalize_Fiyat_Hareketi[i]
            for j in range(1, pencere_boyutu + 1)
        ) and all(
            Normalize_Fiyat_Hareketi[i] < Normalize_Fiyat_Hareketi[i + k]
            for k in range(1, pencere_boyutu + 1)
        ):
            yerel_ekstremumlar.append(
                (
                    Tarih[i],
                    Normalize_Fiyat_Hareketi[i],
                    Fiyat[i],
                    RSI[i],
                    MACD[i],
                    Sinyal[i],
                    fiyat_ema5_uzaklik[i],
                    fiyat_ema25_uzaklik[i],
                    fiyat_ema50_uzaklik[i],
                    fiyat_ema99_uzaklik[i],
                    fiyat_ema200_uzaklik[i],
                    0,
                )
            )
    return yerel_ekstremumlar


Tarih = veri.index.tolist()
Fiyat = veri["Adj Close"].tolist()
RSI = veri["RSI"].tolist()
MACD = veri["MACD"].tolist()
Sinyal = veri["Sinyal"].tolist()
Normalize_Fiyat_Hareketi = veri["Normalize_Fiyat_Hareketi"].tolist()
fiyat_ema5_uzaklik = veri["fiyat_ema5_uzaklik"].tolist()
fiyat_ema25_uzaklik = veri["fiyat_ema25_uzaklik"].tolist()
fiyat_ema50_uzaklik = veri["fiyat_ema50_uzaklik"].tolist()
fiyat_ema99_uzaklik = veri["fiyat_ema99_uzaklik"].tolist()
fiyat_ema200_uzaklik = veri["fiyat_ema200_uzaklik"].tolist()

hisse_ekstremumlar = yerel_ekstremumlari_bul(
    Tarih,
    Normalize_Fiyat_Hareketi,
    Fiyat,
    RSI,
    MACD,
    Sinyal,
    fiyat_ema5_uzaklik,
    fiyat_ema25_uzaklik,
    fiyat_ema50_uzaklik,
    fiyat_ema99_uzaklik,
    fiyat_ema200_uzaklik,
)

ekstremum_df = pd.DataFrame(
    hisse_ekstremumlar,
    columns=[
        "Tarih",
        "Normalize_Fiyat_Hareketi",
        "Fiyat",
        "RSI",
        "MACD",
        "Sinyal",
        "Fiyat_EMA5_Uzaklik",
        "Fiyat_EMA25_Uzaklik",
        "Fiyat_EMA50_Uzaklik",
        "Fiyat_EMA99_Uzaklik",
        "Fiyat_EMA200_Uzaklik",
        "Tür",
    ],
)

ekstremum_df.set_index("Tarih", inplace=True)

X = ekstremum_df[
    [
        "Normalize_Fiyat_Hareketi",
        "Fiyat",
        "RSI",
        "MACD",
        "Sinyal",
        "Fiyat_EMA5_Uzaklik",
        "Fiyat_EMA25_Uzaklik",
        "Fiyat_EMA50_Uzaklik",
        "Fiyat_EMA99_Uzaklik",
        "Fiyat_EMA200_Uzaklik",
    ]
]
y = ekstremum_df["Tür"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

model = pickle.load(open("Hisse Senedi Trend/Butcher_Model.sav", "rb"))
model.fit(X_train, y_train)

y_proba = model.predict_proba(X_test)

esik_degerler = {"Sat": sat_threshold, "Al": al_threshold}
sonuclar = {}

for etiket, esik in esik_degerler.items():
    y_pred = (y_proba[:, 1] > esik).astype(int)
    cm = confusion_matrix(y_test, y_pred)
    rapor = classification_report(y_test.values, y_pred, output_dict=True)
    sonuclar[etiket] = {"karisik_matrisi": cm, "sınıflandırma_raporu": rapor}

st.subheader("🔍 Sınıflandırma Raporu")
for etiket, bilgi in sonuclar.items():
    st.write(f"\n### {etiket} için Sonuçlar")
    fig = plt.figure(figsize=(6, 4))
    sns.set(font_scale=1)
    sns.heatmap(
        bilgi["karisik_matrisi"],
        annot=True,
        annot_kws={"size": 10},
        fmt="g",
        cmap="Blues",
    )
    plt.xlabel("Tahmin Edilen Etiketler", fontsize=10)
    plt.ylabel("Gerçek Etiketler", fontsize=10)
    plt.title("Karışıklık Matrisi", fontsize=12)
    st.pyplot(fig)
    st.write("#### Sınıflandırma Raporu:")
    st.dataframe(pd.DataFrame(bilgi["sınıflandırma_raporu"]).transpose())

st.subheader("📉 Tahmin Grafiği")

y_tahmin_etiketleri = []
for proba in y_proba:
    if proba[1] >= esik_degerler["Al"]:
        y_tahmin_etiketleri.append("Al")
    elif proba[1] <= esik_degerler["Sat"]:
        y_tahmin_etiketleri.append("Sat")
    else:
        y_tahmin_etiketleri.append("Tut")

fiyatlar = X_test["Fiyat"]
indeksler = X_test.index

fig = plt.figure(figsize=(14, 7))
plt.plot(veri.index, veri["Adj Close"], color="#1f77b4", linewidth=2)

for i, etiket in enumerate(y_tahmin_etiketleri):
    if etiket == "Al":
        plt.scatter(
            indeksler[i],
            fiyatlar.iloc[i],
            color="green",
            label="Al" if i == 0 else "",
            s=100,
            edgecolors="k",
            alpha=0.7,
        )
    elif etiket == "Sat":
        plt.scatter(
            indeksler[i],
            fiyatlar.iloc[i],
            color="red",
            label="Sat" if i == 0 else "",
            s=100,
            edgecolors="k",
            alpha=0.7,
        )

plt.title(f"{hisse_sembolu} Tahmin Sonuçları", fontsize=16)
plt.xlabel("Tarih", fontsize=12)
plt.ylabel("Fiyat", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
st.pyplot(fig)
