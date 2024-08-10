import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
from sentiment_predictor import analyze_market_sentiment

# Sayfa yapılandırma
st.set_page_config(
    page_title="FİNANS WEB UYGULAMASI",
    page_icon="💲",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sayfa başlığı
st.title("💲 FİNANS WEB UYGULAMASI")

# Kenar çubuğu
with st.sidebar:
    st.header("Tarih Seçimi")
    di = st.date_input("Başlangıç Tarihi", datetime.date(2020, 1, 1))
    df = st.date_input("Bitiş Tarihi", datetime.date(2024, 1, 1))

    if di >= df:
        st.error("Bitiş tarihi başlangıç tarihinden büyük olmalıdır ❌")

    st.header("Hisse Seçimi")
    secili_hisse = st.text_input("Bir hisse senedi yazın", "AAPL")

# Ana sayfa
st.header("📈 Hisse Senedi Verileri ve Grafikleri")

st.subheader("Güncel Fiyat")
hisse_verisi = yf.Ticker(secili_hisse)
son_fiyat = hisse_verisi.history(period="1d")["Close"].iloc[-1]
son_fiyat_yuvarlanmis = round(son_fiyat, 2)
st.markdown(
    f"<span style='color:green; font-size:24px;'>**{secili_hisse}** için güncel fiyat: <b>{son_fiyat_yuvarlanmis} $</b></span>",
    unsafe_allow_html=True,
)

st.subheader("Tarihsel Veriler")
hisse_verileri = yf.download(secili_hisse, start=di, end=df)
df_hisse = pd.DataFrame(hisse_verileri)
df_hisse = df_hisse.drop(columns=["Adj Close"])
st.dataframe(df_hisse, use_container_width=True)

st.divider()

st.header("📊 Grafik Görselleştirme")
st.line_chart(df_hisse[["High", "Low"]], use_container_width=True)

st.header("📑 Finansal Tablolar")
tab1, tab2, tab3 = st.tabs(["Bilanço", "Gelir Tablosu", "Nakit Akışı"])

sirket = yf.Ticker(secili_hisse)
with tab1:
    st.subheader("Bilanço")
    st.dataframe(sirket.balance_sheet, use_container_width=True, height=500)

    st.subheader("Piyasa Duyarlılığı Analizi")
    market_sentiment = analyze_market_sentiment(secili_hisse)

    if market_sentiment is not None:
        st.markdown(
            f"**{secili_hisse}** için ortalama piyasa duyarlılığı: **{market_sentiment}**"
        )
        if market_sentiment < -0.4:
            st.write("***:red[Güçlü Satış]***")
        elif market_sentiment > 0.4:
            st.markdown("***:green[Güçlü Alış]***")
        elif market_sentiment < 0:
            st.write("***:red[Satış]***")
        elif market_sentiment > 0:
            st.write("***:green[Alış]***")
    else:
        st.write(
            f"{secili_hisse} için piyasa duyarlılığını analiz etmek üzere haber bulunamadı"
        )

with tab2:
    st.subheader("Gelir Tablosu")
    st.dataframe(sirket.financials, use_container_width=True, height=500)

with tab3:
    st.subheader("Nakit Akışı")
    st.dataframe(sirket.cashflow, use_container_width=True, height=500)

# Alt bilgi
st.markdown("---")
st.caption(
    "Bu uygulama finansal verileri görselleştirmek ve piyasa duyarlılığını analiz etmek için geliştirilmiştir."
)
