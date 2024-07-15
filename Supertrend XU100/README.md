## Türkçe
## Supertrend Ticaret Stratejisi ve Analizi

### Amaç
Bu projenin amacı Borsa İstanbul'da (BIST) işlem gören hisse senetleri için Supertrend ticaret stratejisini uygulamaktır. Supertrend, fiyat ve volatiliteye dayalı olarak giriş ve çıkış noktalarının belirlenmesine yardımcı olan, trendi takip eden bir göstergedir.

### Nasıl çalışır
**1. Süper Trend Hesaplaması:**

- **Ortalama Gerçek Aralık (ATR):** Pandas_ta kitaplığını kullanarak ATR göstergesini hesaplar.
- **Süper Trend Formülü:** Trend yönünü ve volatiliteyi tanımlamak için ATR'yi kullanan Süper Trend göstergesini hesaplar. Uzun ve kısa pozisyonlar için zararı durdurma seviyelerinin belirlenmesine yardımcı olur.
- **Sinyal Üretimi:** Fiyat Supertrend çizgisinin üzerine çıktığında alış sinyalleri, Supertrend çizgisinin altına geçtiğinde ise satış sinyalleri üretir.

**2. Uygulama Adımları:**

- **Hisse Senedi Listesini Getir:** Belirtilen kaynaktan BIST hisse senetlerinin listesini alır.
- **Geçmiş Verilerini Getir**: Yahoo Finance API'yi (yfinance) kullanarak her hisse senedi için geçmiş fiyat ve hacim verilerini alır.
- **Süper Trendi Hesapla:** Supertrend göstergesine dayalı alım satım sinyallerini tanımlamak için Supertrend işlevini uygular.
- **Geri Test İstatistikleri Oluşturun:** Vectorbt kütüphanesini kullanarak kazanma oranı, Sharpe oranı, ortalama kazanan ticaret süresi ve ortalama kaybedilen ticaret süresi gibi ticaret performansı ölçümlerini hesaplar.
- **Geriye Dönük Test Sonuçlarını Görselleştirin:** Geçerli satın alma sinyallerine sahip hisse senetleri için geriye dönük test performans grafikleri oluşturur ve kaydeder.

### Faydalar
- **Trend Belirleme:** Fiyat hareketine dayalı olarak trendleri ve potansiyel giriş/çıkış noktalarını belirlemek için Supertrend'i kullanır.
- **Performans Değerlendirmesi:** İstatistiksel ölçümler ve görselleştirmeler kullanarak ticaret stratejisinin etkinliğini değerlendirir.
- **Otomatik Analiz:** Stratejiyi BIST'te listelenen birden fazla hisse senedine otomatik olarak uygulayarak potansiyel ticaret fırsatlarına ilişkin bilgiler sağlar.

### Kullanım
Bu komut dosyası, trend takip stratejileri ve Supertrend göstergesini kullanan teknik analizle ilgilenen yatırımcılar ve analistler için faydalıdır. Sağlanan istatistikler ve görselleştirmeler, stratejinin performansının değerlendirilmesine ve bilinçli ticaret kararları alınmasına yardımcı olur.

### Not
Bu proje, Supertrend göstergesinin BIST hisse senetlerindeki potansiyel işlem fırsatlarını belirlemek için bir araç olarak kullanılmasına odaklanmaktadır. Mali tavsiye sağlamaz ve yalnızca eğitim amaçlı ve araştırma amaçlı kullanılmalıdır.

## English
## Supertrend Trading Strategy and Analysis

### Purpose
The purpose of this project is to implement a Supertrend trading strategy for stocks listed on Borsa Istanbul (BIST). Supertrend is a trend-following indicator that helps identify entry and exit points based on price and volatility.

### How It Works
**1. Supertrend Calculation:**

- **Average True Range (ATR):** Calculates the ATR indicator using the pandas_ta library.
- **Supertrend Formula:** Computes the Supertrend indicator which uses the ATR to define the trend direction and volatility. It helps identify the stop-loss levels for long and short positions.
- **Signal Generation:** Generates buy signals when the price crosses above the Supertrend line and sell signals when the price crosses below the Supertrend line.

**2. Implementation Steps:**

- **Fetch Stock List:** Retrieves the list of BIST stocks from a specified source.
- **Fetch Historical Data**: Retrieves historical price and volume data for each stock using the Yahoo Finance API (yfinance).
- **Calculate Supertrend:** Implements the Supertrend function to identify trading signals based on Supertrend indicator.
- **Generate Backtest Statistics:** Calculates trading performance metrics such as win rate, Sharpe ratio, average winning trade duration, and average losing trade duration using the vectorbt library.
- **Visualize Backtest Results:** Generates and saves backtest performance plots for stocks with valid buy signals.

### Benefits
- **Trend Identification:** Utilizes Supertrend to identify trends and potential entry/exit points based on price action.
- **Performance Evaluation:** Evaluates trading strategy effectiveness using statistical metrics and visualizations.
- **Automated Analysis:** Automatically applies the strategy across multiple stocks listed on BIST, providing insights into potential trading opportunities.

### Usage
This script is useful for traders and analysts interested in trend-following strategies and technical analysis using the Supertrend indicator. The provided statistics and visualizations aid in assessing the strategy's performance and making informed trading decisions.

### Note
This project focuses on using the Supertrend indicator as a tool for identifying potential trading opportunities in BIST stocks. It does not provide financial advice and should be used for educational purposes and research only.