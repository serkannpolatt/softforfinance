## Türkçe
## WaveTrend Stratejisi Geriye Dönük Test ve Analiz
### Amaç
Bu projenin amacı, TradingView'in veri akışından alınan geçmiş fiyat verilerini kullanarak BIST borsasında listelenen hisse senetleri üzerinde WaveTrend ticaret stratejisini uygulamak ve geriye doğru test etmektir.

### Nasıl çalışır
**1. WaveTrend Stratejisi:**

- **Gösterge Hesaplaması:** Pandas_ta kitaplığını kullanarak WaveTrend osilatörünü hesaplar. WaveTrend osilatörü, trend dönüşlerini belirlemek için hareketli ortalamaları ve Bollinger Bantlarını birleştiren bir teknik analiz aracıdır.
- **Giriş ve Çıkış Sinyalleri:** tci1, tci2'nin üzerine geçtiğinde alış sinyalleri, tci1, tci2'nin altına geçtiğinde ise satış sinyalleri üretir.

**2. Uygulama Adımları:**

- **Hisse Senedi Listesini Getir:** Tradingview_screener'daki get_all_symbols işlevini kullanarak BIST piyasasındaki tüm hisse senedi simgelerinin listesini alır.
- **Geçmiş Verilerini Getir:** TradingView'den TvDatafeed'i kullanarak her hisse senedi için geçmiş OHLCV (Açık, Yüksek, Düşük, Kapanış, Hacim) verilerini alır.
- **WaveTrend Osilatörünü Hesapla:** Sağlanan parametrelere (n1 ve n2) dayalı olarak osilatör değerlerini hesaplamak için WaveTrend işlevini uygular.
- **Backtest Stratejisi:** WaveTrend sinyallerini kullanarak ticareti simüle etmek için geriye dönük test kütüphanesindeki Backtest sınıfını kullanır.
- **Geri Test İstatistikleri Oluşturun:** Geriye dönük test edilmiş verileri kullanarak kazanma oranı gibi işlem performansı ölçümlerini hesaplar.
- **Ticaret Sinyallerini Tanımlayın:** Oluşturulan WaveTrend osilatör değerlerine göre alım ve satım sinyallerini belirler.
- **Özet DataFrame Oluştur:** Hisse senedi sembolü, son fiyat, kazanma oranı ve giriş/çıkış sinyallerini içeren sonuçları df_signals DataFrame'de saklar.
- **Sonuçları Filtrele**: Al sinyalinin (Giriş Sinyali) True olduğu hisse senetlerini filtreler ve yazdırır.

### Faydalar
- **Teknik Analiz Aracı:** Trend dönüşlerine dayalı potansiyel ticaret fırsatlarını belirlemek için WaveTrend osilatörünü kullanır.
- **Otomatik Geriye Dönük Test:** BIST pazarındaki birden fazla hisse senedinde stratejiyi test etme sürecini otomatikleştirir.
- **Performans Değerlendirmesi:** İstatistiksel ölçümleri kullanarak ticaret stratejisinin etkinliğini değerlendirir ve potansiyel satın alma sinyallerine sahip hisse senetlerini belirler.

### Kullanım
Bu script, WaveTrend osilatörünü temel alan teknik analiz ve algoritmik ticaret stratejileriyle ilgilenen yatırımcılar ve analistler için tasarlanmıştır. Geçmiş fiyat verilerine dayanarak BIST hisse senetlerindeki potansiyel ticaret fırsatlarına ilişkin öngörüler sağlar.

### Not
Bu proje, BIST hisse senetlerindeki potansiyel ticaret fırsatlarını belirlemek için WaveTrend osilatörünün bir araç olarak kullanılmasına odaklanmaktadır. Mali tavsiye sağlamaz ve yalnızca eğitim amaçlı ve araştırma amaçlı kullanılmalıdır.

## WaveTrend Strategy Backtesting and Analysis
### Purpose
The purpose of this project is to implement and backtest the WaveTrend trading strategy on stocks listed on the BIST exchange using historical price data fetched from TradingView's data feed.

### How It Works
**1. WaveTrend Strategy:**

- **Indicator Calculation:** Calculates the WaveTrend oscillator using the pandas_ta library. The WaveTrend oscillator is a technical analysis tool that combines moving averages and Bollinger Bands to identify trend reversals.
- **Entry and Exit Signals:** Generates buy signals when the tci1 crosses above tci2 and sell signals when tci1 crosses below tci2.

**2. Implementation Steps:**

- **Fetch Stock List:** Retrieves the list of all stock symbols from the BIST market using get_all_symbols function from tradingview_screener.
- **Fetch Historical Data:** Retrieves historical OHLCV (Open, High, Low, Close, Volume) data for each stock using TvDatafeed from TradingView.
- **Calculate WaveTrend Oscillator:** Implements the WaveTrend function to compute the oscillator values based on provided parameters (n1 and n2).
- **Backtest Strategy:** Utilizes the Backtest class from backtesting library to simulate trading using the WaveTrend signals.
- **Generate Backtest Statistics:** Calculates trading performance metrics such as win rate using the backtested data.
- **Identify Trading Signals:** Determines buy and sell signals based on the generated WaveTrend oscillator values.
- **Create Summary DataFrame:** Stores the results including stock symbol, last price, win rate, and entry/exit signals in df_signals DataFrame.
- **Filter Results**: Filters and prints the stocks where the buy signal (Giriş Sinyali) is True.

### Benefits
- **Technical Analysis Tool:** Uses WaveTrend oscillator for identifying potential trading opportunities based on trend reversals.
- **Automated Backtesting:** Automates the process of testing the strategy across multiple stocks in the BIST market.
- **Performance Evaluation:** Evaluates trading strategy effectiveness using statistical metrics and identifies stocks with potential buy signals.

### Usage
This script is designed for traders and analysts interested in technical analysis and algorithmic trading strategies based on the WaveTrend oscillator. It provides insights into potential trading opportunities in BIST stocks based on historical price data.

### Note
This project focuses on using the WaveTrend oscillator as a tool for identifying potential trading opportunities in BIST stocks. It does not provide financial advice and should be used for educational purposes and research only.