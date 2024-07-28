## Türkçe
## RSI Iraksak Ticaret Stratejisi ve Analizi
### Amaç
Bu projenin amacı BIST 100 hisse senetleri için RSI (Göreceli Güç Endeksi) sapmasına dayalı bir alım satım stratejisi uygulamaktır. RSI farklılığı, fiyat hareketlerini RSI hareketleriyle karşılaştırarak potansiyel trend dönüşlerini belirlemek için kullanılır.

### Nasıl çalışır
**1. RSI Sapma Hesaplaması:**

- **Göreceli Güç Endeksi (RSI):** Pandas_ta kitaplığını kullanarak RSI göstergesini hesaplar.
- **Farklılık Tanımlaması**: Scipy.stats.linregress'i kullanarak yükseliş (fiyat daha düşük dipler oluştururken RSI daha yüksek dipler oluşturur) ve düşüş eğilimi (fiyat daha yüksek en yüksekler oluştururken RSI daha düşük en yüksekler oluşturur) sapmalarını tanımlar.
- **Giriş ve Çıkış Sinyalleri:** Yükseliş eğilimi oluştuğunda ve RSI 40'ın altında olduğunda alış sinyalleri üretir. Düşüş eğilimi oluştuğunda satış sinyalleri üretir.

**2. Uygulama Adımları:**

- **Hisse Senedi Listesini Getir:** Belirli bir kaynaktan BIST 100 hisse senetlerinin listesini alır.
- **Geçmiş Verilerini Getir:** Stock_Prices işlevini kullanarak her bir hisse senedi için geçmiş fiyat ve hacim verilerini alır.
- **RSI Farklılığını Hesapla:** RSI farklılıklarını temel alarak ticaret sinyallerini tanımlamak için rsi_divergence işlevini uygular.
- **Geri Test İstatistikleri Oluşturun:** Vectorbt kütüphanesini kullanarak kazanma oranı, Sharpe oranı, ortalama kazanan ticaret süresi ve ortalama kaybedilen ticaret süresi gibi ticaret performansı ölçümlerini hesaplar.
- **Geri Test Sonuçlarını Görselleştirin:** Yüksek kazanma oranlarına (>%80) ve geçerli satın alma sinyallerine sahip hisse senetleri için geriye dönük test performans grafikleri oluşturur ve kaydeder.

### Faydalar
- **Sinyal Doğruluğu:** Yaygın olarak tanınan bir teknik analiz aracı olan RSI sapmasını kullanarak potansiyel trend dönüşlerini tanımlar.
- **Performans Değerlendirmesi:** İstatistiksel ölçümler ve görselleştirmeler kullanarak ticaret stratejisinin etkinliğini değerlendirir.
- **Otomatik Analiz:** Stratejiyi BIST 100 endeksindeki birden fazla hisse senedine otomatik olarak uygulayarak potansiyel ticaret fırsatlarına ilişkin kapsamlı bilgiler sağlar.

### Kullanım
Bu komut dosyası, teknik analiz ve RSI farklılığına dayalı algoritmik ticaret stratejileriyle ilgilenen yatırımcılar ve analistler tarafından kullanılabilir. Oluşturulan istatistikler ve görselleştirmeler, stratejinin performansının anlaşılmasına ve bilinçli ticaret kararları alınmasına yardımcı olur.

### Not
Bu proje, BIST 100 hisse senetlerindeki potansiyel ticaret fırsatlarının belirlenmesinde RSI farklılığının bir araç olarak kullanılmasına odaklanmaktadır. Mali tavsiye sağlamaz ve yalnızca eğitim amaçlı ve araştırma amaçlı kullanılmalıdır.


## English
## RSI Divergence Trading Strategy and Analysis
### Purpose
The purpose of this project is to implement a trading strategy based on RSI (Relative Strength Index) divergence for BIST 100 stocks. RSI divergence is used to identify potential trend reversals by comparing price movements with RSI movements.

### How It Works
**1. RSI Divergence Calculation:**

- **Relative Strength Index (RSI):** Calculates the RSI indicator using the pandas_ta library.
- **Divergence Identification**: Identifies bullish (price making lower lows while RSI making higher lows) and bearish (price making higher highs while RSI making lower highs) divergences using scipy.stats.linregress.
- **Entry and Exit Signals:** Generates buy signals when bullish divergence occurs and the RSI is below 40. Generates sell signals when bearish divergence occurs.

**2. Implementation Steps:**

- **Fetch Stock List:** Retrieves the list of BIST 100 stocks from a specified source.
- **Fetch Historical Data:** Retrieves historical price and volume data for each stock using the Stock_Prices function.
- **Calculate RSI Divergence:** Implements the rsi_divergence function to identify trading signals based on RSI divergences.
- **Generate Backtest Statistics:** Calculates trading performance metrics such as win rate, Sharpe ratio, average winning trade duration, and average losing trade duration using the vectorbt library.
- **Visualize Backtest Results:** Generates and saves backtest performance plots for stocks with high win rates (>80%) and valid buy signals.

### Benefits
- **Signal Accuracy:** Identifies potential trend reversals using RSI divergence, a widely recognized technical analysis tool.
- **Performance Evaluation:** Evaluates trading strategy effectiveness using statistical metrics and visualizations.
- **Automated Analysis:** Automatically applies the strategy across multiple stocks in the BIST 100 index, providing comprehensive insights into potential trading opportunities.

### Usage
This script can be used by traders and analysts interested in technical analysis and algorithmic trading strategies based on RSI divergence. The generated statistics and visualizations assist in understanding the strategy's performance and making informed trading decisions.

### Note
This project focuses on using RSI divergence as a tool for identifying potential trading opportunities in BIST 100 stocks. It does not provide financial advice and should be used for educational purposes and research only.