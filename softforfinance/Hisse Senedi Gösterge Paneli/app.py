import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

# ============= SAYFA AYARLARI =============
st.set_page_config(
    page_title="Hisse Senedi Gösterge Paneli", page_icon="🧊", layout="centered"
)

# ============ CSS STİLLERİ ==============
st.markdown(
    '<style>h3{font-size:1.65rem;opacity:0.3;}div.block-container{padding:1rem auto;} div.element-container{margin: 0rem; padding: 0rem;}div[role="tablist"]{justify-content: space-between;}button[role="tab"]{padding: 1rem; border-radius: 10px;}button[role="tab"][aria-selected="true"]{background: #E0FBE2;}button[role="tab"] p, summary{color:#333333; font-weight:600;} summary:hover span{color:#ACE1AF; font-weight:bold;} div[role="presentation"]{background:none;} div[role="alert"]{padding:1.2rem 2.2rem;background:#F6F5F250;color:#333333;line-height: 1.7;} a{color:rgb(49, 51, 63) !important; text-decoration:none;} a:hover{color:#ACE1AF !important; text-decoration:none;} div[data-baseweb="select"]>div{border-color: #D2E9E9 !important; box-shadow: rgba(0, 0, 0, 0.04) 0px 3px 5px;}div[data-testid="stTable"]{padding: 7px 0 0 0;}table{font-family:"Source Sans Pro", sans-serif;text-align:left;border-radius: 10px;}.no-data{padding: 1.75rem 0;text-align: left; color: rgb(49, 51, 63); font-weight: bold;} .tab-num{font-size: 2.25rem; color: rgb(49, 51, 63);}</style>',
    unsafe_allow_html=True,
)

# Başlık #
st.header("Hisse Senedi Gösterge Paneli")

# Başlangıç ayarları
today = datetime.now().date()
ticker = ""
company = ""

col1, col2 = st.columns((2))
with col1:
    ticker_name_list = pd.read_csv("Hisse Senedi Gösterge Paneli/ticker_names.txt")
    ticker = st.selectbox("Bir Hisse Seçin", ticker_name_list)

# ============ Şirket Verileri ============
company = yf.Ticker(ticker)

# ============ Şirket Bilgileri ============
infos = company.info

# Güncel Fiyat #
col2.metric("Güncel Fiyat", f"$ {infos.get('currentPrice', '')}")

# Şirket adı #
st.title(infos.get("longName", ""))

# Alt Başlık - Performans #
st.subheader("Performans")

# Sekmeler #
one_day, one_week, one_month, one_year, max = st.tabs(
    ["2 Gün", " 1 Hafta", " 1 Ay", " 1 Yıl", "Max"]
)


def get_past_date(value, units):
    if units == "days":
        past_date = today - timedelta(days=value)
    elif units == "weeks":
        past_date = today - timedelta(weeks=value)
    elif units == "months":
        past_date = today - relativedelta(months=value)
    elif units == "years":
        past_date = today - relativedelta(years=value)
    else:
        past_date = today - timedelta(days=value)
    return past_date


def update_axis_names(fig, x_axis_name, y_axis_name):
    fig.update_layout(xaxis_title=x_axis_name, yaxis_title=y_axis_name)
    return fig


with one_day:
    ticker = company.history(period="5d", start=get_past_date(5, "days"), end=today)
    if ticker.empty:
        st.markdown("<p class='no-data'>Veri bulunamadı</p>", unsafe_allow_html=True)
    else:
        fig = px.line(ticker, x=ticker.index, y=ticker["Close"], title="2 Gün")
        update_axis_names(fig, "Saat", "Kapanış Fiyatı")
        st.plotly_chart(fig, use_container_width=True)

with one_week:
    ticker = company.history(interval="1d", start=get_past_date(1, "weeks"), end=today)
    if ticker.empty:
        st.markdown("<p class='no-data'>Veri bulunamadı</p>", unsafe_allow_html=True)
    else:
        fig = px.line(ticker, x=ticker.index, y=ticker["Close"], title="1 Hafta")
        update_axis_names(fig, "Tarih", "Kapanış Fiyatı")
        st.plotly_chart(fig, use_container_width=True)

with one_month:
    ticker = company.history(interval="1d", start=get_past_date(1, "months"), end=today)
    if ticker.empty:
        st.markdown("<p class='no-data'>Veri bulunamadı</p>", unsafe_allow_html=True)
    else:
        fig = px.line(ticker, x=ticker.index, y=ticker["Close"], title="1 Ay")
        update_axis_names(fig, "Tarih", "Kapanış Fiyatı")
        st.plotly_chart(fig, use_container_width=True)

with one_year:
    ticker = company.history(interval="1mo", start=get_past_date(1, "years"), end=today)
    if ticker.empty:
        st.markdown("<p class='no-data'>Veri bulunamadı</p>", unsafe_allow_html=True)
    else:
        fig = px.line(ticker, x=ticker.index, y=ticker["Close"], title="1 Yıl")
        update_axis_names(fig, "Ay", "Kapanış Fiyatı")
        st.plotly_chart(fig, use_container_width=True)

with max:
    ticker = company.history(period="max", interval="3mo")
    if ticker.empty:
        st.markdown("<p class='no-data'>Veri bulunamadı</p>", unsafe_allow_html=True)
    else:
        fig = px.line(ticker, x=ticker.index, y=ticker["Close"], title="Max")
        update_axis_names(fig, "Yıl", "Kapanış Fiyatı")
        st.plotly_chart(fig, use_container_width=True)

st.divider()

# Sekmeler #
custom_period, day_high, day_low, fiftyTwo_high, fiftyTwo_low = st.tabs(
    [
        "Özel Dönem",
        "Günlük Yüksek",
        " Günlük Düşük",
        "52 Hafta Yüksek",
        "52 Hafta Düşük",
    ]
)
with custom_period:
    col1, col2, col3 = st.columns((3))
    with col1:
        min_date = (
            ticker.index.min().date()
            if not ticker.empty
            else date(date.today().year, 1, 1)
        )
        start_date = pd.to_datetime(
            st.date_input(
                "Başlangıç Tarihi", date(date.today().year, 1, 1), min_value=min_date
            )
        )
    with col2:
        end_date = pd.to_datetime(st.date_input("Bitiş Tarihi", date.today()))
    with col3:
        interval = st.selectbox("Aralık", ["1 Gün", "5 Gün", "1 Hafta", "1 Ay", "3 Ay"])

    def switch_inter(value):
        if value == "1 Gün":
            return "1d"
        elif value == "5 Gün":
            return "5d"
        elif value == "1 Hafta":
            return "1wk"
        elif value == "1 Ay":
            return "1mo"
        elif value == "3 Ay":
            return "3mo"
        else:
            return "1d"

    ticker = company.history(
        period="max", interval=switch_inter(interval), start=start_date, end=end_date
    )

    if ticker.empty:
        st.markdown("<p class='no-data'>Veri bulunamadı</p>", unsafe_allow_html=True)
    else:
        fig = px.line(
            ticker, x=ticker.index, y=ticker["Close"], title=company.info["longName"]
        )
        update_axis_names(fig, "Gün", "Kapanış Fiyatı")
        st.plotly_chart(fig, use_container_width=True)

with day_high:
    if "dayHigh" in infos:
        dayHigh = round(float(infos["dayHigh"]), 3)
        st.markdown(
            f"<p class='tab-num' style='width:40%; text-align:right;'>$ {dayHigh}</p>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown("<p class='no-data'>Veri bulunamadı</p>", unsafe_allow_html=True)

with day_low:
    if "dayLow" in infos:
        dayLow = round(float(infos["dayLow"]), 3)
        st.markdown(
            f"<p class='tab-num' style='width:60%; text-align:right;'>$ {dayLow}</p>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown("<p class='no-data'>Veri bulunamadı</p>", unsafe_allow_html=True)

with fiftyTwo_high:
    if "fiftyTwoWeekHigh" in infos:
        fiftyTwoWeekHigh = round(float(infos["fiftyTwoWeekHigh"]), 3)
        st.markdown(
            f"<p class='tab-num' style='width:70%; text-align:right;'>$ {fiftyTwoWeekHigh}</p>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown("<p class='no-data'>Veri bulunamadı</p>", unsafe_allow_html=True)

with fiftyTwo_low:
    if "fiftyTwoWeekLow" in infos:
        fiftyTwoWeekLow = round(float(infos["fiftyTwoWeekLow"]), 3)
        st.markdown(
            f"<p class='tab-num' style='width:70%; text-align:right;'>$ {fiftyTwoWeekLow}</p>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown("<p class='no-data'>Veri bulunamadı</p>", unsafe_allow_html=True)

# Bölücü çizgi #
st.divider()

# Alt Başlık - Şirket Bilgileri #
st.subheader("Şirket Bilgileri")

if infos.get("longName") is not None:
    st.markdown(f"**Şirket Adı:** {infos.get('longName', '')}")
if infos.get("sector") is not None:
    st.markdown(f"**Sektör:** {infos.get('sector', '')}")
if infos.get("website") is not None and infos.get("irWebsite") is None:
    st.markdown(f"**Web Sitesi:** [Şirket Web Sitesi]({infos.get('website', '')})")
if infos.get("website") is not None and infos.get("irWebsite") is not None:
    st.markdown(
        f"**Web Siteleri:** [Şirket Web Sitesi]({infos.get('website', '')}) | [Yatırımcı İlişkileri Web Sitesi]({infos.get('irWebsite', '')})"
    )
if infos.get("address1") is not None:
    st.markdown(
        "<p style='margin-bottom:0;font-weight:600;'>Adres:</p>", unsafe_allow_html=True
    )
st.markdown(
    f"<span>{infos.get('address1', '')}<br/> {infos.get('city', '')}<br/> {infos.get('state', '')}  {infos.get('zip', '')}  {infos.get('country', '')}</span>",
    unsafe_allow_html=True,
)
if infos.get("longBusinessSummary") is not None:
    st.markdown(
        "<p style='margin-bottom:3px;font-weight:600;'>Açıklama:</p>",
        unsafe_allow_html=True,
    )
    with st.expander("Daha fazla oku"):
        st.info(infos.get("longBusinessSummary", ""))

# Şirket logosunu göster #
if "logo_url" in company.info:
    st.image(company.info["logo_url"])

# Bölücü çizgi #
st.divider()

# ============== Şirket Finansal Verileri ==============
financials = company.financials
# cashflow = company.cashflow
# =========================================

# Alt Başlık - Temel Göstergeler #
st.subheader("Temel Göstergeler")

if ticker.empty:
    st.markdown("<p class='no-data'>Veri bulunamadı</p>", unsafe_allow_html=True)
else:
    col4, col5 = st.columns((2))

    with col4:
        if infos.get("marketCap") is not None:
            st.metric(label="Pazar Değeri", value=f"$ {infos.get('marketCap', ''):,}")
        if infos.get("freeCashflow") is not None:
            st.metric(
                label="Serbest Nakit Akışı",
                value=f"$ {infos.get('freeCashflow', ''):,}",
            )
        if infos.get("totalRevenue") is not None:
            st.metric(
                label="Toplam Gelir", value=f"$ {infos.get('totalRevenue', ''):,}"
            )

    with col5:
        if infos.get("ebitda") is not None:
            st.metric(label="EBITDA", value=f"$ {infos.get('ebitda', ''):,}")
        if infos.get("operatingCashflow") is not None:
            st.metric(
                label="Faaliyet Nakit Akışı",
                value=f"$ {infos.get('operatingCashflow', ''):,}",
            )
        if infos.get("netIncomeToCommon") is not None:
            st.metric(
                label="Net Kar", value=f"$ {infos.get('netIncomeToCommon', ''):,}"
            )

    # Bölücü çizgi #
    st.divider()

    col6, col7, col8 = st.columns((3))
    with col6:
        if infos.get("profitMargins") is not None:
            profitMargins = round((infos.get("profitMargins", "") * 100), 2)
            st.metric(label="Kar Marjları", value=f"{profitMargins} %")
        if infos.get("grossMargins") is not None:
            grossMargins = round((infos.get("grossMargins", "") * 100), 2)
            st.metric(label="Brüt Marjlar", value=f"{grossMargins} %")
        if (
            infos.get("lastDividendValue") is not None
            and infos.get("lastDividendDate") is not None
        ):
            lastDividendDate = datetime.utcfromtimestamp(
                infos.get("lastDividendDate")
            ).date()
            lastDividendValue = round((infos.get("lastDividendValue", "")), 2)
            st.metric(
                label=f"Son Temettü {lastDividendDate}", value=f"$ {lastDividendValue}"
            )

    with col7:
        if infos.get("ebitdaMargins") is not None:
            ebitdaMargins = round((infos.get("ebitdaMargins", "") * 100), 2)
            st.metric(label="EBITDA Marjları", value=f"{ebitdaMargins} %")
        if infos.get("operatingMargins") is not None:
            operatingMargins = round((infos.get("operatingMargins", "") * 100), 2)
            st.metric(label="Faaliyet Marjları", value=f"{operatingMargins} %")
        if infos.get("trailingEps") is not None:
            trailingEps = round((infos.get("trailingEps", "")), 2)
            st.metric(label="Hisse Başına Kar (EPS)", value=f"$ {trailingEps}")

    with col8:
        if infos.get("priceToBook") is not None:
            priceToBook = round(infos.get("priceToBook", ""), 2)
            st.metric(label="Fiyat/Defter Değeri (P/B)", value=f"{priceToBook}")
        if infos.get("debtToEquity") is not None:
            debtToEquity = round(infos.get("debtToEquity", ""), 2)
            st.metric(label="Borç/Öz Sermaye Oranı", value=f"{debtToEquity}")
        if infos.get("enterpriseToEbitda") is not None:
            enterpriseToEbitda = round(infos.get("enterpriseToEbitda", ""), 2)
            st.metric(
                label="Firma Değeri / EBITDA (EV/EBITDA)",
                value=f"{enterpriseToEbitda}",
            )


# Bölücü çizgi #
st.divider()

# Alt Başlık - Analiz #
st.subheader("Analiz")

financials_df = pd.DataFrame(financials)

financials1_check = ["Gross Profit", "Cost Of Revenue", "Operating Revenue"]
if all(metric in financials_df.index for metric in financials1_check):
    short_financials1 = (
        financials_df.loc[["Gross Profit", "Cost Of Revenue", "Operating Revenue"]]
        .transpose()
        .dropna()
    )
    line1 = px.line(
        short_financials1,
        x=short_financials1.index,
        y=["Gross Profit", "Cost Of Revenue", "Operating Revenue"],
        title="Gelir Tarihçesi",
    )
    st.write(update_axis_names(line1, "Zaman", "Değer"))

financials2_check = [
    "Total Revenue",
    "Net Income",
    "Operating Income",
    "Operating Expense",
    "Interest Expense",
    "Total Expenses",
]
if all(metric in financials_df.index for metric in financials2_check):
    short_financials2 = (
        financials_df.loc[
            [
                "Total Revenue",
                "Net Income",
                "Operating Income",
                "Operating Expense",
                "Interest Expense",
                "Total Expenses",
            ]
        ]
        .transpose()
        .dropna()
    )
    line2 = px.line(
        short_financials2,
        x=short_financials2.index,
        y=[
            "Total Revenue",
            "Net Income",
            "Operating Income",
            "Operating Expense",
            "Interest Expense",
            "Total Expenses",
        ],
        title="Gelir ve Gider Tarihçesi",
    )
    st.write(update_axis_names(line2, "Zaman", "Değer"))
