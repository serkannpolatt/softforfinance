import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Döviz kurları için sembol
usd_try_symbol = "USDTRY=X"


# Dolar kurunu almak için fonksiyon
def get_usd_try_data(start_date, end_date):
    try:
        df_usd_try = yf.download(usd_try_symbol, start=start_date, end=end_date)
        df_usd_try["Date"] = pd.to_datetime(df_usd_try.index)
        df_usd_try.set_index("Date", inplace=True)
        return df_usd_try
    except Exception:
        st.warning("Döviz kurunu alamıyoruz. Lütfen tekrar deneyin.")
        return None


# Hareketli ortalamaları ve alım/satış sinyalleri hesaplamak için fonksiyon
def calculate_moving_averages(df, short_window, long_window):
    # Hareketli ortalamaları hesapla
    df["Short_MA"] = df["Close"].rolling(window=short_window).mean()
    df["Long_MA"] = df["Close"].rolling(window=long_window).mean()

    # Alım/Satış sinyallerini işaretleme
    df["Signal"] = np.where(df["Short_MA"] > df["Long_MA"], 1, 0)
    df["Position"] = df["Signal"].diff()

    return df


# Hareketli ortalamaları ve alım/satış sinyalleri hesaplamak için fonksiyon
def calculate_moving_averages_currency(df, short_window, long_window, price_column):
    # Hareketli ortalamaları hesaplama
    df["Short_MA"] = df[price_column].rolling(window=short_window).mean()
    df["Long_MA"] = df[price_column].rolling(window=long_window).mean()

    # Alım/Satış sinyallerini işaretleme
    df["Signal"] = np.where(df["Short_MA"] > df["Long_MA"], 1, 0)
    df["Position"] = df["Signal"].diff()  # Alım/Satış sinyalleri için

    return df


# Dosyadan liste okuyan fonksiyon
def read_tickers_from_file(file_path):
    with open(file_path, "r") as f:
        tickers = [line.strip() for line in f.readlines()]
    return tickers


# BIST 50 hisse senetlerinin listesini dosyadan okuyun
bist_50_tickers = read_tickers_from_file(
    "Hisse Senedi Detaylı Analiz/bist_50_tickers.txt"
)

# Sayfa seçimi için yan menü
page = st.sidebar.selectbox(
    "Sayfa Seçin",
    [
        "Teknik Analiz",
        "Kazanç Tablosu",
        "BIST Hacim Grafikleri",
        "Hisse Artış/Azalış Yüzdesi",
    ],
)

end_date = pd.Timestamp.now()

if page == "Teknik Analiz":
    st.title("Hisse Senedi Analizi")
    selected_ticker = st.selectbox("Hisse Senedi Seçin", bist_50_tickers)

    date_range_options = ["1 Senelik", "3 Senelik", "5 Senelik"]
    selected_date_range = st.selectbox("Tarih Aralığını Seçin", date_range_options)

    # Başlangıç tarihini seçilen aralığa göre ayarlayın
    if selected_date_range == "1 Senelik":
        start_date = end_date - pd.DateOffset(years=1)
    elif selected_date_range == "3 Senelik":
        start_date = end_date - pd.DateOffset(years=3)
    elif selected_date_range == "5 Senelik":
        start_date = end_date - pd.DateOffset(years=5)

    # Döviz kurlarını alma
    usd_try_data = get_usd_try_data(start_date, end_date)
    if usd_try_data is None:
        st.warning("Dolar/TL kurunu alamadık. Lütfen daha sonra tekrar deneyin.")

    # Hisse senedi verilerini indirin
    df = yf.download(selected_ticker, start=start_date, end=end_date)
    df["Date"] = pd.to_datetime(df.index)
    df.set_index("Date", inplace=True)

    # Dolar cinsinden fiyatları hesaplama
    df["USD_Close"] = df["Close"] / usd_try_data["Close"]

    # Kullanıcıya hangi türden fiyatları göstermek istediğini sorma
    price_type = st.radio(
        "Hangi fiyat türünü görmek istersiniz?", ["Türk Lirası", "Dolar"]
    )

    # Hareketli ortalamalar ve alım/satış sinyalleri hesaplamak için aynı veri kümesini kullanın
    # Kullanıcıdan kısa pencere ve uzun pencere girdisi
    short_window_str = st.sidebar.text_input(
        "Kısa Pencere (5-50)", value="10"
    )  # Metin olarak alıyoruz
    long_window_str = st.sidebar.text_input(
        "Uzun Pencere (60-200)", value="100"
    )  # Metin olarak alıyoruz

    # Girdi doğrulaması ve hatalara karşı önlem
    try:
        # String'i tam sayıya dönüştür
        short_window = int(short_window_str)
        long_window = int(long_window_str)

        # Değer aralıklarını kontrol et
        if short_window < 5 or short_window > 50:
            st.sidebar.warning("Kısa pencere 5 ile 50 arasında olmalıdır.")
        if long_window < 60 or long_window > 200:
            st.sidebar.warning("Uzun pencere 60 ile 200 arasında olmalıdır.")

    except ValueError:
        # Eğer girdi bir tam sayı değilse
        st.sidebar.warning("Lütfen geçerli bir sayı girin.")

    df = calculate_moving_averages_currency(
        df, short_window, long_window, "USD_Close" if price_type == "Dolar" else "Close"
    )

    buy_signals = df[df["Position"] == 1]
    sell_signals = df[df["Position"] == -1]

    # Grafik çizimi
    subset_df = df.loc[start_date:end_date]

    fig, ax = plt.subplots(figsize=(12, 6))
    if price_type == "Türk Lirası":
        ax.plot(subset_df["Close"], label="Kapanış Fiyatı", color="k", linewidth=2)
        ax.plot(
            buy_signals.index,
            buy_signals["Close"],
            "^",
            markersize=10,
            color="g",
            label="Alım Sinyali",
        )
        ax.plot(
            sell_signals.index,
            sell_signals["Close"],
            "v",
            markersize=10,
            color="r",
            label="Satış Sinyali",
        )
    else:
        ax.plot(subset_df["USD_Close"], label="Kapanış Fiyatı", color="k", linewidth=2)
        ax.plot(
            buy_signals.index,
            buy_signals["USD_Close"],
            "^",
            markersize=10,
            color="g",
            label="Alım Sinyali",
        )
        ax.plot(
            sell_signals.index,
            sell_signals["USD_Close"],
            "v",
            markersize=10,
            color="r",
            label="Satış Sinyali",
        )
    ax.plot(
        subset_df["Short_MA"],
        label=f"{short_window} Günlük Hareketli Ortalama",
        color="g",
    )
    ax.plot(
        subset_df["Long_MA"],
        label=f"{long_window} Günlük Hareketli Ortalama",
        color="b",
    )

    #    ax.plot(buy_signals.index, buy_signals['Close'], '^', markersize=10, color='g', label='Alım Sinyali')
    #    ax.plot(sell_signals.index, sell_signals['Close'], 'v', markersize=10, color='r', label='Satış Sinyali')

    ax.set_xlabel("Tarih")
    ax.set_ylabel("Fiyat")
    ax.legend(loc="upper left")
    plt.title(f"{selected_ticker} için Hareketli Ortalamalar ve Alım/Satış Sinyalleri")
    plt.grid(True)

    st.pyplot(fig)

elif page == "BIST Hacim Grafikleri":
    st.title("BIST Hacim Grafikleri")

    user_input = st.text_input("Hisse Kodu Girin (ör. AKBNK)")

    date_range_options = ["1 Senelik", "3 Senelik", "5 Senelik"]
    selected_date_range = st.selectbox("Tarih Aralığını Seçin", date_range_options)

    # Başlangıç tarihini seçilen aralığa göre ayarlayın
    if selected_date_range == "1 Senelik":
        start_date = end_date - pd.DateOffset(years=1)
    elif selected_date_range == "3 Senelik":
        start_date = end_date - pd.DateOffset(years=3)
    elif selected_date_range == "5 Senelik":
        start_date = end_date - pd.DateOffset(years=5)

    if user_input:
        hisse_kodu = user_input.strip().upper() + ".IS"
        try:
            df = yf.download(hisse_kodu, start=start_date, end=end_date)
            if not df.empty:
                df["Date"] = pd.to_datetime(df.index)
                df.set_index("Date", inplace=True)

                fig, ax = plt.subplots(figsize=(12, 6))
                ax.plot(df["Close"], label="Kapanış Fiyatı", color="k", linewidth=2)

                ax2 = ax.twinx()
                ax2.bar(df.index, df["Volume"], color="gray", alpha=0.5, label="Hacim")
                ax2.set_ylabel("Hacim")

                ax.set_xlabel("Tarih")
                ax.set_ylabel("Fiyat")
                ax.legend(loc="upper left")
                ax2.legend(loc="upper right")
                plt.title(
                    f"{hisse_kodu} için Hareketli Ortalamalar, Alım/Satış Sinyalleri ve Hacim"
                )
                plt.grid(True)

                st.pyplot(fig)
            else:
                st.warning("Bu hisse bulunamamıştır.")
        except Exception:
            st.warning("Bu hisse bulunamamıştır veya indirilemedi.")

elif page == "Kazanç Tablosu":
    st.title("Kazanç Tablosu Top 5")

    selected_ticker = st.selectbox("Hisse Senedi Seçin", bist_50_tickers)

    date_range_options = ["1 Senelik", "3 Senelik", "5 Senelik"]
    selected_date_range = st.selectbox("Tarih Aralığını Seçin", date_range_options)
    # Başlangıç tarihini seçilen aralığa göre ayarlayın
    if selected_date_range == "1 Senelik":
        start_date = end_date - pd.DateOffset(years=1)
    elif selected_date_range == "3 Senelik":
        start_date = end_date - pd.DateOffset(years=3)
    elif selected_date_range == "5 Senelik":
        start_date = end_date - pd.DateOffset(years=5)

    # Döviz kurlarını alma
    usd_try_data = get_usd_try_data(start_date, end_date)
    if usd_try_data is None:
        st.warning("Dolar/TL kurunu alamadık. Lütfen daha sonra tekrar deneyin.")

    df = yf.download(selected_ticker, start=start_date, end=end_date)
    df["Date"] = pd.to_datetime(df.index)
    df.set_index("Date", inplace=True)

    df["USD_Close"] = df["Close"] / usd_try_data["Close"]
    price_type = st.radio(
        "Hangi fiyat türünü görmek istersiniz?", ["Türk Lirası", "Dolar"]
    )

    results = []
    for short_window in range(5, 51, 5):
        for long_window in range(60, 201, 10):
            if long_window <= short_window:
                continue

            df = calculate_moving_averages_currency(
                df,
                short_window,
                long_window,
                "USD_Close" if price_type == "Dolar" else "Close",
            )

            buy_signals = df[df["Position"] == 1]
            sell_signals = df[df["Position"] == -1]

            min_length = min(len(buy_signals), len(sell_signals))
            buy_signals = buy_signals.iloc[:min_length]
            sell_signals = sell_signals.iloc[:min_length]

            if min_length > 0:
                if price_type == "Dolar":
                    gain_loss = (
                        sell_signals["USD_Close"].values
                        - buy_signals["USD_Close"].values
                    )
                else:
                    gain_loss = (
                        sell_signals["Close"].values - buy_signals["Close"].values
                    )
                total_gain_loss = gain_loss.sum()

                results.append(
                    {
                        "Short Window": short_window,
                        "Long Window": long_window,
                        "Total Gain/Loss": total_gain_loss,
                    }
                )

    results_df = pd.DataFrame(results).sort_values(
        by="Total Gain/Loss", ascending=False
    )

    if not results_df.empty:
        top_5_gain = results_df.head(5)

        st.write("En Yüksek 5 Kazanç Kombinasyonu:")
        st.dataframe(top_5_gain)

elif page == "Hisse Artış/Azalış Yüzdesi":
    st.title("Hisse Artış/Azalış Yüzdesi")

    # Kullanıcıdan tarih aralığını seçmesini isteyin
    date_range_options = [
        "1 Ay",
        "3 Ay",
        "6 Ay",
        "Yıl Başından Beri",
        "1 Yıl",
        "3 Yıl",
        "5 Yıl",
    ]
    selected_date_range = st.selectbox("Tarih Aralığını Seçin", date_range_options)

    # Başlangıç tarihini seçilen aralığa göre ayarlayın
    if selected_date_range == "1 Ay":
        start_date = end_date - pd.DateOffset(months=1)
    elif selected_date_range == "3 Ay":
        start_date = end_date - pd.DateOffset(months=3)
    elif selected_date_range == "6 Ay":
        start_date = end_date - pd.DateOffset(months=6)
    elif selected_date_range == "Yıl Başından Beri":
        start_date = pd.Timestamp(end_date.year, 1, 1)
    elif selected_date_range == "1 Yıl":
        start_date = end_date - pd.DateOffset(years=1)
    elif selected_date_range == "3 Yıl":
        start_date = end_date - pd.DateOffset(years=3)
    elif selected_date_range == "5 Yıl":
        start_date = end_date - pd.DateOffset(years=5)

    # Hisselerin artış/azalış yüzdesini hesaplamak için bir sözlük oluşturun
    performance_dict = {}

    # Seçilen tarih aralığına göre hisse senetlerinin performansını hesaplayın
    for ticker in bist_50_tickers:
        try:
            # Belirtilen tarih aralığında hisse senedinin kapanış fiyatlarını alın
            df = yf.download(ticker, start=start_date, end=end_date)
            if not df.empty:
                # Başlangıç ve bitiş fiyatlarını alın
                start_price = df.iloc[0]["Close"]
                end_price = df.iloc[-1]["Close"]
                # Artış/Azalış yüzdesini hesaplayın
                price_change_percentage = (
                    (end_price - start_price) / start_price
                ) * 100
                # Hisselerin artış/azalış yüzdesini sözlüğe ekleyin
                performance_dict[ticker] = price_change_percentage
        except Exception as e:
            st.warning(f"{ticker} için veri alınamadı: {e}")

    # Hisselerin artış/azalış yüzdesini büyükten küçüğe göre sıralayın
    sorted_performance = sorted(
        performance_dict.items(), key=lambda x: x[1], reverse=False
    )

    # Artış/Azalış yüzdesini görselleştirin
    if sorted_performance:
        fig, ax = plt.subplots(figsize=(10, len(sorted_performance) * 0.5))
        tickers, percentages = zip(*sorted_performance)
        colors = [
            "skyblue" if percentage >= 0 else "lightcoral" for percentage in percentages
        ]
        ax.barh(tickers, percentages, color=colors)
        for i, (ticker, percentage) in enumerate(sorted_performance):
            ax.text(percentage, i, f"{percentage:.2f}%", ha="left", va="center")
        ax.set_xlabel("Artış/Azalış Yüzdesi")
        ax.set_ylabel("Hisse Senedi")
        ax.set_title(
            f"{selected_date_range} Tarih Aralığındaki Hisselerin Artış/Azalış Yüzdesi"
        )
        plt.grid(True)
        st.pyplot(fig)
    else:
        st.warning("Veri bulunamadı. Lütfen daha sonra tekrar deneyin.")
