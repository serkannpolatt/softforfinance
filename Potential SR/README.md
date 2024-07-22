## Türkçe
## BIST Hisse Senedi Destek ve Direnç Analizi

### Amaç
Bu proje, BIST hisse senetlerinin geçmiş fiyat verilerine dayanarak destek ve direnç seviyelerini analiz etmeyi amaçlamaktadır. Yerel ekstrem değerleri kullanarak potansiyel destek ve direnç bölgelerini tanımlar ve bu seviyelerin görsel bir temsilini sağlar. Analiz, yatırımcıların gelecekteki fiyat hareketlerini etkileyebilecek temel fiyat seviyelerini belirlemelerine yardımcı oluyor.

### Nasıl çalışır
**1. Veri Alma:**

- **Hisse_Temel_Veriler:** İş Yatırım web sitesinden BIST hisse senedi sembollerinin listesini alır.
- **Hisse_Fiyatları:** İş Yatırım API'sini kullanarak her hisse senedi için gün içi fiyat verilerini getirir.

2. Destek ve Direnç Hesaplaması:

- **Destek_ve_Direnç:** Kapanış fiyatlarının yerel ekstrem değerlerine göre potansiyel destek ve direnç seviyelerini tanımlar.
- **En Yakın Değerler:** Mevcut kapanış fiyatına en yakın destek ve direnç seviyelerini bulur.
- **Yüzde Mesafe**: Mevcut kapanış fiyatı ile belirlenen destek/direnç seviyeleri arasındaki yüzde mesafeyi hesaplar.

### Görselleştirme:

- **Plot_SR:** Belirlenen destek ve direnç seviyeleriyle birlikte geçmiş kapanış fiyatlarını gösterir.
- **Yatay Çizgiler:** Görsel netlik için belirlenen destek ve direnç seviyelerine yatay çizgiler ekler.
- **İşaretçiler:** Referans olması açısından grafikteki en son kapanış fiyatını işaretler.

### Raporlama:

- **DataFrame Yapısı:** Sonuçları, hisse senedi adlarını, destek/direnç durumunu ve ek yorumları içeren yapılandırılmış bir DataFrame'de saklar.
- **Filtrelenmiş Sonuçlar:** Yalnızca potansiyel destek veya direncin belirlendiği hisse senetlerini görüntüler.
- **Yorum:** Belirlenen destek/direnç seviyelerine göre açıklayıcı yorumlar sağlar.

### Faydalar
- **Teknik Analiz:** Geçmiş fiyat verilerine göre destek ve direnç seviyelerini belirleme sürecini otomatikleştirir.
- **Görselleştirme:** Hızlı analiz için destek ve direnç seviyelerinin net görsel temsillerini sağlar.
- **Karar Desteği:** Temel fiyat seviyelerini vurgulayarak yatırımcıların bilinçli kararlar almasına yardımcı olur.

### Kullanım
Bu script, BIST hisse senetleri üzerinde destek ve direnç analizi yapmak isteyen yatırımcılar ve analistler için tasarlanmıştır. Ticaret kararlarını etkileyebilecek potansiyel fiyat seviyelerine ilişkin bilgiler sağlar.

### Not
Bu proje finansal tavsiye niteliğinde değildir ve yalnızca eğitim ve araştırma amaçlı kullanılmalıdır. Yatırımcıların, belirlenen destek ve direnç seviyelerine göre alım satım kararları vermeden önce kapsamlı analiz ve doğrulama yapmaları teşvik edilmektedir.

## English
## BIST Stocks Support and Resistance Analysis

### Purpose
This project aims to analyze support and resistance levels for BIST stocks based on their historical price data. It identifies potential support and resistance zones using local extrema and provides a visual representation of these levels. The analysis helps traders identify key price levels that could influence future price movements.

### How It Works
**1. Data Retrieval:**

- **Hisse_Temel_Veriler:** Retrieves a list of BIST stock symbols from the Is Yatirim website.
- **Stock_Prices:** Fetches intraday price data for each stock using the Is Yatirim API.

2. Support and Resistance Calculation:

- **Support_and_Resistance:** Identifies potential support and resistance levels based on local extrema of closing prices.
- **Closest Values:** Finds the closest support and resistance levels to the current closing price.
- **Percentage Distance**: Calculates the percentage distance between the current closing price and identified support/resistance levels.

### Visualization:

- **Plot_SR:** Plots the historical closing prices along with identified support and resistance levels.
- **Horizontal Lines:** Adds horizontal lines at the identified support and resistance levels for visual clarity.
- **Markers:** Marks the most recent closing price on the plot for reference.

### Reporting:

- **DataFrame Structure:** Stores the results in a structured DataFrame containing stock names, support/resistance status, and additional comments.
- **Filtered Results:** Displays only stocks where potential support or resistance has been identified.
- **Commentary:** Provides descriptive comments based on the identified support/resistance levels.

### Benefits
- **Technical Analysis:** Automates the process of identifying support and resistance levels based on historical price data.
- **Visualization:** Provides clear visual representations of support and resistance levels for quick analysis.
- **Decision Support:** Assists traders in making informed decisions by highlighting key price levels.

### Usage
This script is designed for traders and analysts interested in conducting support and resistance analysis on BIST stocks. It provides insights into potential price levels that may influence trading decisions.

### Note
This project does not constitute financial advice and should be used for educational and research purposes only. Traders are encouraged to conduct thorough analysis and validation before making trading decisions based on the identified support and resistance levels.