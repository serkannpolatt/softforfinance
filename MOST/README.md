## Türkçe
## BIST Hisse Senetleri MOST Stratejisinin Geriye Dönük Testi ve Sinyalleri
### Amaç
Bu proje, TradingView API'sinden alınan geçmiş fiyat verilerini kullanarak BIST hisse senetleri üzerinde Hareketli Optimal Stratejiyi (MOST) uygulamayı ve geriye doğru test etmeyi amaçlamaktadır. Strateji, üstel hareketli ortalamalara (EMA) dayalı trendleri belirler ve buna göre alım ve satım sinyalleri üretir. Geriye dönük test, stratejinin performansını kazanma oranı açısından değerlendirir ve potansiyel ticaret sinyalleri hakkında raporlar üretir.

### Nasıl çalışır
**1. MOST Stratejisi:**

- **En İyi Hareket Stratejisi:** Strateji, eğilimleri belirlemek için üstel bir hareketli ortalama (EMA) kullanır ve bu eğilimlere dayalı olarak işlemlere giriş ve çıkış için en uygun fiyat seviyelerini belirler.
- **EMA Hesaplaması:** Pandas_ta kitaplığını kullanarak EMA'yı hesaplar.
- Trend Belirleme: EMA ile dinamik olarak ayarlanmış optimal fiyat seviyesi (MOST) arasındaki ilişkiye dayalı olarak trendin yönünü (yukarı veya aşağı) belirler.
- **Sinyal Üretimi:** Fiyat MOST'un altına geçtiğinde alış sinyalleri (Giriş) ve fiyat MOST'un üzerine çıktığında satış sinyalleri (Çıkış) üretir.

**2. Uygulama Adımları:**
- **Hisse Senedi Sembollerini Getir:** Tradingview_screener kitaplığını kullanarak tüm BIST hisse senedi sembollerini alır.
- **Geçmiş Verilerini Getir:** tvDatafeed kitaplığını kullanarak her hisse senedi için geçmiş fiyat ve hacim verilerini alır.
- **MOST Hesaplaması:** MOST değerlerini hesaplar ve trend değişikliklerine göre işlem sinyallerini tanımlar.
- **Geriye dönük test:** MOST stratejisini geçmiş veriler üzerinde geriye doğru test etmek için geriye dönük test kitaplığından yararlanır.
- **Sinyal Değerlendirmesi:** Kazanma oranı gibi stratejinin performans ölçümlerini değerlendirir ve potansiyel alım ve satım sinyallerini belirler.

### Raporlama:

- **DataFrame Yapısı:** Hisse senedi adları, son fiyat, MOST değeri, kazanma oranı ve sinyal göstergeleri dahil sonuçları depolamak ve görüntülemek için yapılandırılmış bir DataFrame kullanır.
- **Sinyal Tanımlama:** Oluşturulan sinyallere (Giriş ve Çıkış) göre alım ve satım sinyallerini belirler.

### Faydalar
- **Otomatik Analiz:** Birden fazla BIST hisse senedi için strateji uygulama, geriye dönük test etme ve sinyal oluşturma sürecini otomatikleştirir.
- **Performans Değerlendirmesi:** Kazanma oranı gibi niceliksel ölçümler yoluyla MOST stratejisinin etkinliğini değerlendirir.
- **Sinyal Görselleştirme:** Daha fazla analiz ve karar alma için potansiyel ticaret sinyalleri hakkında yapılandırılmış bir rapor sağlar.

### Kullanım
Bu script, geçmiş fiyat verilerini kullanarak BIST hisse senetlerinde Hareketli Optimal Stratejiyi (MOST) uygulamak ve değerlendirmek isteyen yatırımcılar ve analistler için tasarlanmıştır. Stratejinin performansına ilişkin bilgiler sağlar ve önceden tanımlanmış sinyallere dayalı olarak potansiyel ticaret fırsatlarını belirler.

### Not
Bu proje finansal tavsiye niteliğinde değildir ve yalnızca eğitim ve araştırma amaçlı kullanılmalıdır. Yatırımcıların, oluşturulan sinyallere dayanarak alım satım kararları vermeden önce kapsamlı analiz ve doğrulama yapmaları teşvik edilir.

## English
## BIST Stocks MOST Strategy Backtesting and Signals
### Purpose
This project aims to implement and backtest the Moving Optimal Strategy (MOST) on BIST stocks using historical price data fetched from the TradingView API. The strategy identifies trends based on exponential moving averages (EMA) and generates buy and sell signals accordingly. The backtesting evaluates the strategy's performance in terms of win rate and generates reports on potential trading signals.

### How It Works
**1. MOST Strategy:**

- **Moving Optimal Strategy:** The strategy uses an exponential moving average (EMA) to identify trends and determines the optimal price levels for entering and exiting trades based on these trends.
- **EMA Calculation:** Calculates the EMA using the pandas_ta library.
- Trend Identification: Determines the direction of the trend (up or down) based on the relationship between the EMA and a dynamically adjusted optimal price level (MOST).
- **Signal Generation:** Generates buy signals (Entry) when the price crosses below the MOST and sell signals (Exit) when the price crosses above the MOST.

**2. Implementation Steps:**
- **Fetch Stock Symbols:** Retrieves all BIST stock symbols using the tradingview_screener library.
- **Fetch Historical Data:** Retrieves historical price and volume data for each stock using the tvDatafeed library.
- **MOST Calculation:** Computes the MOST values and identifies trading signals based on trend changes.
- **Backtesting:** Utilizes the backtesting library to backtest the MOST strategy on historical data.
- **Signal Evaluation:** Evaluates the strategy's performance metrics such as win rate and identifies potential buy and sell signals.

### Reporting:

- **DataFrame Structure:** Uses a structured DataFrame to store and display results including stock names, last price, MOST value, win rate, and signal indicators.
- **Signal Identification:** Determines buy and sell signals based on the generated signals (Entry and Exit).

### Benefits
- **Automated Analysis:** Automates the process of strategy implementation, backtesting, and signal generation for multiple BIST stocks.
- **Performance Evaluation:** Evaluates the effectiveness of the MOST strategy through quantitative metrics such as win rate.
- **Signal Visualization:** Provides a structured report on potential trading signals for further analysis and decision-making.

### Usage
This script is designed for traders and analysts interested in implementing and evaluating the Moving Optimal Strategy (MOST) on BIST stocks using historical price data. It provides insights into the strategy's performance and identifies potential trading opportunities based on predefined signals.

### Note
This project does not constitute financial advice and should be used for educational and research purposes only. Traders are encouraged to conduct thorough analysis and validation before making trading decisions based on the generated signals.