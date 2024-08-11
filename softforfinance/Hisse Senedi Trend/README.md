## Türkçe
## Hisse Senedi Trend Tahmincisi
Bu proje, kullanıcıların belirli bir hisse senedi için fiyat trendlerini analiz etmelerine ve gelecekteki fiyat hareketlerini tahmin etmelerine yardımcı olan bir Streamlit uygulamasıdır.

### Amaç
Hisse Senedi Trend Tahmincisi, kullanıcıların belirli bir hisse senedi sembolü girerek, geçmiş fiyat verilerini analiz etmelerine ve fiyat tahminleri yapmalarına olanak tanır. Bu uygulama, hisse senedi yatırımcılarının daha bilinçli kararlar almalarını desteklemek için tasarlanmıştır.

### Nasıl Çalışır?
**1. Uygulama Başlığı:** Uygulama başlığı ve giriş formu ekranda görüntülenir.

**2. Hisse Sembolü Girişi:** Kullanıcıdan bir hisse sembolü, başlangıç ve bitiş tarihleri, satış ve alış eşik değerleri girmesi istenir.

**3. Veri İndirme ve Hazırlama:** Yahoo Finance API'si kullanılarak belirli tarihler arasındaki hisse senedi verileri indirilir ve gerekli hesaplamalar yapılır.

**4. Grafikler ve Analizler:**

- Kapanış fiyatı ve üssel hareketli ortalamalar (EMA) grafik olarak gösterilir.
- Ekstra özellikler (Fiyat Hareketi, Normalize Fiyat Hareketi, RSI, MACD, StochRSI) hesaplanır.
- Yerel ekstremumlar bulunur ve bu verilere dayalı olarak model eğitimi yapılır.

**5. Makine Öğrenimi Modeli:**

- Eğitim ve test verileri hazırlanır.
- Daha önce eğitilmiş model yüklenir ve test verileri üzerinde tahminler yapılır.
- Sınıflandırma raporu ve karışıklık matrisi görüntülenir.

**6. Tahmin Grafiği:** Tahmin edilen alış ve satış sinyalleri grafikte görselleştirilir.

## English
## Stock Trend Forecaster
This project is a Streamlit application that helps users analyze price trends and predict future price movements for a particular stock.

### Aim
Stock Trend Forecaster allows users to analyze historical price data and make price predictions by entering a specific stock symbol. This app is designed to support stock investors in making more informed decisions.

### How does it work?
**one. Application Title:** Application title and entry form are displayed on the screen.

**2. Stock Symbol Entry:** The user is asked to enter a stock symbol, start and end dates, sell and buy thresholds.

**3. Data Download and Preparation:** Using the Yahoo Finance API, stock data between certain dates is downloaded and the necessary calculations are made.

**4. Charts and Analysis:**

- The closing price and exponential moving averages (EMA) are displayed graphically.
- Extra features (Price Movement, Normalized Price Movement, RSI, MACD, StochRSI) are calculated.
- Local extremes are found and model training is done based on these data.

**5. Machine Learning Model:**

- Training and test data are prepared.
- The previously trained model is loaded and predictions are made on the test data.
- The classification report and confusion matrix are displayed.

**6. Prediction Chart:** Predicted buy and sell signals are visualized on the chart.
