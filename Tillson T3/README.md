## Türkçe
## Tillson T3 Ticaret Stratejisi ve Analizi
### Amaç
Bu projenin amacı Borsa İstanbul'da (BIST) işlem gören hisse senetleri için Tillson T3 ticaret stratejisini uygulamaktır. Tillson T3 göstergesi, eğilimlerin ve potansiyel giriş/çıkış noktalarının belirlenmesine yardımcı olan daha yumuşak ve daha duyarlı bir hareketli ortalamadır.

### Nasıl çalışır
**1. Tillson T3 Hesaplaması:**

- **Üstel Hareketli Ortalamalar (EMA):** Hisse senedinin düzeltilmiş kapanış fiyatı üzerinden birden fazla EMA katmanı hesaplar.
- **Tillson T3 Formülü:** Tillson T3 göstergesini hesaplamak için EMA'yı içeren özel bir formül kullanır.
- **Sinyal Üretimi:** Tillson T3 göstergesi önceki değerinin üzerine çıktığında alış sinyali, altına geçtiğinde ise satış sinyali üretir.

**2. Uygulama Adımları:**

- **Hisse Senedi Listesini Getir:** Belirtilen kaynaktan BIST hisse senetlerinin listesini alır.
- **Geçmiş Verilerini Getir:** Yahoo Finance API'yi (yfinance) kullanarak her hisse senedi için geçmiş fiyat ve hacim verilerini alır.
- **Tillson T3'ü Hesapla:** Tillson T3 göstergesine dayalı olarak alım satım sinyallerini tanımlamak için TillsonT3 işlevini uygular.
- **Geri Test İstatistikleri Oluşturun:** Vectorbt kütüphanesini kullanarak kazanma oranı, Sharpe oranı, ortalama kazanan ticaret süresi ve ortalama kaybedilen ticaret süresi gibi ticaret performansı ölçümlerini hesaplar.
- **Geriye Dönük Test Sonuçlarını Görselleştirin:** Geçerli satın alma sinyallerine sahip hisse senetleri için geriye dönük test performans grafikleri oluşturur ve kaydeder.

### Faydalar
- **Trend Belirleme:** Düzleştirilmiş fiyat hareketine dayalı olarak trendleri ve potansiyel giriş/çıkış noktalarını belirlemek için Tillson T3'ü kullanır.
- **Performans Değerlendirmesi:** İstatistiksel ölçümler ve görselleştirmeler kullanarak ticaret stratejisinin etkinliğini değerlendirir.
- **Otomatik Analiz:** Stratejiyi BIST'te listelenen birden fazla hisse senedine otomatik olarak uygulayarak potansiyel ticaret fırsatlarına ilişkin bilgiler sağlar.

### Kullanım
Bu komut dosyası, trend takip stratejileri ve Tillson T3 göstergesini kullanan teknik analizle ilgilenen yatırımcılar ve analistler için faydalıdır. Sağlanan istatistikler ve görselleştirmeler, stratejinin performansının değerlendirilmesine ve bilinçli ticaret kararları alınmasına yardımcı olur.

### Not
Bu proje, BIST hisse senetlerindeki potansiyel ticaret fırsatlarını belirlemek için Tillson T3 göstergesinin bir araç olarak kullanılmasına odaklanmaktadır. Mali tavsiye sağlamaz ve yalnızca eğitim amaçlı ve araştırma amaçlı kullanılmalıdır.

## English
## Tillson T3 Trading Strategy and Analysis
### Purpose
The purpose of this project is to implement a Tillson T3 trading strategy for stocks listed on Borsa Istanbul (BIST). The Tillson T3 indicator is a smoother and more responsive moving average that helps in identifying trends and potential entry/exit points.

### How It Works
**1. Tillson T3 Calculation:**

- **Exponential Moving Averages (EMA):** Calculates multiple layers of EMAs on the adjusted close price of the stock.
- **Tillson T3 Formula:** Utilizes a specific formula involving EMA to compute the Tillson T3 indicator.
- **Signal Generation:** Generates buy signals when the Tillson T3 indicator crosses above its previous value and sell signals when it crosses below.

**2. Implementation Steps:**

- **Fetch Stock List:** Retrieves the list of BIST stocks from a specified source.
- **Fetch Historical Data:** Retrieves historical price and volume data for each stock using the Yahoo Finance API (yfinance).
- **Calculate Tillson T3:** Implements the TillsonT3 function to identify trading signals based on Tillson T3 indicator.
- **Generate Backtest Statistics:** Calculates trading performance metrics such as win rate, Sharpe ratio, average winning trade duration, and average losing trade duration using the vectorbt library.
- **Visualize Backtest Results:** Generates and saves backtest performance plots for stocks with valid buy signals.

### Benefits
- **Trend Identification:** Utilizes Tillson T3 to identify trends and potential entry/exit points based on smoothed price action.
- **Performance Evaluation:** Evaluates trading strategy effectiveness using statistical metrics and visualizations.
- **Automated Analysis:** Automatically applies the strategy across multiple stocks listed on BIST, providing insights into potential trading opportunities.

### Usage
This script is useful for traders and analysts interested in trend-following strategies and technical analysis using the Tillson T3 indicator. The provided statistics and visualizations aid in assessing the strategy's performance and making informed trading decisions.

### Note
This project focuses on using the Tillson T3 indicator as a tool for identifying potential trading opportunities in BIST stocks. It does not provide financial advice and should be used for educational purposes and research only.