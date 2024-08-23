import streamlit as st
import yfinance as yf
import mplfinance as mpf
import pandas as pd
from PIL import Image
from datetime import datetime, timedelta
from io import BytesIO
from ultralytics import YOLO

# Model dosyasının yolu
model_path = "SFW-STOCK SCAN/weights/custom_yolov8.pt"


# Sayfa düzeni ayarı
st.set_page_config(
    page_title="SFW-STOCK SCAN",  # Sayfa başlığı
    page_icon="📊",  # Sayfa ikonu
    layout="wide",  # Geniş düzen
    initial_sidebar_state="expanded",  # Kenar çubuğunu varsayılan olarak genişlet
)


# Grafik indirme ve çizim fonksiyonu
def generate_chart(ticker, interval="1d", chunk_size=180, figsize=(18, 6.5), dpi=100):
    if interval == "1h":
        end_date = datetime.now()
        start_date = end_date - timedelta(days=730)
        period = None
    else:
        start_date = None
        end_date = None
        period = "max"

    # Ticker verilerini indir
    data = yf.download(
        ticker, interval=interval, start=start_date, end=end_date, period=period
    )

    # İndeksin DatetimeIndex olduğundan emin olun ve verilerin boş olup olmadığını kontrol edin
    if not data.empty:
        data.index = pd.to_datetime(data.index)
        # En son 180 mumları seçin
        data = data.iloc[-chunk_size:]

        # Grafiği çiz
        fig, ax = mpf.plot(
            data,
            type="candle",
            style="yahoo",
            title=f"{ticker} Son {chunk_size} Mumlar",
            axisoff=True,
            ylabel="",
            ylabel_lower="",
            volume=False,
            figsize=figsize,
            returnfig=True,
        )

        # Grafiği bir BytesIO nesnesine kaydet
        buffer = BytesIO()
        fig.savefig(buffer, format="png", dpi=dpi)  # DPI burada ayarlanır
        buffer.seek(0)
        return buffer
    else:
        st.error("Belirtilen ticker ve aralık için veri bulunamadı.")
        return None


# Kenar çubuğunu oluşturma
with st.sidebar:
    st.write("")
    st.header("Konfigürasyonlar")  # Kenar çubuğuna başlık ekle
    # Grafik oluşturma ve indirme bölümü
    st.subheader("Grafik Oluştur")
    ticker = st.text_input("Ticker Sembolünü Girin (ör. AAPL):")
    interval = st.selectbox("Aralığı Seçin", ["1d", "1h", "1wk"])
    chunk_size = 180  # Varsayılan mum sayısı
    if st.button("Grafik Oluştur"):
        if ticker:
            chart_buffer = generate_chart(
                ticker, interval=interval, chunk_size=chunk_size
            )
            if chart_buffer:
                st.success("Grafik başarıyla oluşturuldu.")
                st.download_button(
                    label=f"{ticker} Grafiğini İndir",
                    data=chart_buffer,
                    file_name=f"{ticker}_son_{chunk_size}_mumlar.png",
                    mime="image/png",
                )
                st.image(
                    chart_buffer, caption=f"{ticker} Grafiği", use_column_width=True
                )
        else:
            st.error("Lütfen geçerli bir ticker sembolü girin.")
    st.write("")
    st.subheader("Tespit için Görüntü Yükle")
    # Görüntü seçmek için dosya yükleyici ekleyin
    source_img = st.file_uploader(
        "Bir görüntü yükleyin...", type=("jpg", "jpeg", "png", "bmp", "webp")
    )

    # Model seçenekleri
    confidence = float(st.slider("Model Güvenini Seçin", 25, 100, 30)) / 100

# Ana sayfa başlığını oluşturma
st.title("SFW-STOCK SCAN")
st.caption("📈 Uygulamayı kullanmak için aşağıdaki seçeneklerden birini seçin:")

st.markdown("""
**Seçenek 1: Kendi Görüntünüzü Yükleyin**
1. **Görüntü Yükle:** Yerel PC'nizden bir mum grafiği görüntüsü yüklemek için kenar çubuğunu kullanın.
2. **Nesneleri Tespit Et:** Yüklenen grafiği analiz etmek için :blue[Nesneleri Tespit Et] butonuna tıklayın.

**Seçenek 2: Grafik Oluştur ve Analiz Et**
1. **Grafik Oluştur:** Kenar çubuğuna ticker sembolü ve aralığını girerek bir grafik oluşturun ve indirin (son 180 mumlar).
2. **Oluşturulan Grafiği Yükle:** Kenar çubuğunu kullanarak oluşturulan grafik görüntüsünü yükleyin.
3. **Nesneleri Tespit Et:** Oluşturulan grafiği analiz etmek için :blue[Nesneleri Tespit Et] butonuna tıklayın.
""")

# Ana sayfada iki sütun oluşturma
col1, col2 = st.columns(2)

# Görüntü yüklendiğinde ilk sütuna ekleme
if source_img:
    with col1:
        # Yüklenen görüntüyü açma
        uploaded_image = Image.open(source_img)
        # Yüklenen görüntüyü başlık ile sayfaya ekleme
        st.image(uploaded_image, caption="Yüklenen Görüntü", use_column_width=True)

# Modeli yükle
try:
    model = YOLO(model_path)
except Exception as ex:
    st.error(f"Model yüklenemiyor. Belirtilen yolu kontrol edin: {model_path}")
    st.error(ex)

# Butona tıklanırsa nesne tespiti yapma
if st.sidebar.button("Nesneleri Tespit Et"):
    if source_img:
        # Görüntüyü yeniden açmak için dosya işaretçisini sıfırlama
        source_img.seek(0)
        uploaded_image = Image.open(source_img)

        # Nesne tespiti yapma
        res = model.predict(uploaded_image, conf=confidence)
        boxes = res[0].boxes
        res_plotted = res[0].plot()[:, :, ::-1]
        with col2:
            st.image(
                res_plotted, caption="Tespit Edilen Görüntü", use_column_width=True
            )
            try:
                with st.expander("Tespit Sonuçları"):
                    for box in boxes:
                        st.write(box.xywh)
            except Exception:
                st.write("Tespit sonuçlarını görüntülerken hata oluştu.")
    else:
        st.error("Lütfen önce bir görüntü yükleyin.")
