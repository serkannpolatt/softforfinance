## Türkçe 
## BIST 100 Hisse Senedi Piyasası Profili ve İşlem Sinyalleri
### Amaç
Bu projenin amacı BIST 100 hisse senetlerini piyasa profili analizi kullanarak analiz etmek ve piyasa profili göstergelerinden elde edilen spesifik piyasa koşullarına göre potansiyel işlem sinyallerini belirlemektir.

### Nasıl çalışır
**1. Pazar Profili Hesaplaması:**

- **Piyasa Profili:** Piyasa profili, zaman içindeki fiyat dağılımını gösteren ve yatırımcıların ticaret faaliyetinin nerede yoğunlaştığını anlamalarına yardımcı olan bir tekniktir.
- **Değer Alanı:** Toplam işlem hacminin belirli bir yüzdesinin gerçekleştiği fiyat aralığını tanımlar.
- **Kontrol Noktası (POC):** En fazla işlem hacminin gerçekleştiği fiyat seviyesini temsil eder.

**2. Uygulama Adımları:**

- **Hisse Senedi Listesini Getir:** Belirli bir kaynaktan BIST 100 hisse senetlerinin listesini alır.
- Geçmiş Verileri Getir: TVDatafeed kitaplığını kullanarak her hisse senedi için geçmiş fiyat ve hacim verilerini alır.
- **Piyasa Profilini Hesaplayın:** Geçmiş verilerin her bir bölümü için yüksek değer alanı (VAH), düşük değer alanı (VAL) ve kontrol noktasını (POC) hesaplar.
- **Mum Grafiği Oluşturun:** MPlfinance kütüphanesini kullanarak hisse senedinin fiyat hareketlerini piyasa profili göstergeleriyle birlikte görselleştirir.
- **Ticaret Sinyallerini Tanımlayın:** Kapanış fiyatı ile VAL (alış sinyali) veya VAH (satış sinyali) arasındaki ilişkiye dayalı olarak potansiyel giriş ve çıkış noktalarını belirler.

### Faydalar
- **Görsel Analiz:** Belirtilen zaman aralıklarındaki fiyat dağılımının ve alım satım faaliyeti seviyelerinin görsel bir temsilini sağlar.
- **İşlem Sinyalleri:** Kapanış fiyatlarının değer alanı göstergeleri (VAL ve VAH) ile kesişimine dayalı olarak alış ve satış sinyalleri üretir.
- **İstatistiksel Analiz:** Stratejinin etkinliğini değerlendirmek için toplam getiri, kazanma oranı ve Sharpe oranı gibi temel ticaret performansı ölçümlerini hesaplar.

### Kullanım
Bu komut dosyası, tüccarlar ve analistler tarafından piyasa profili analizini kullanarak BIST 100 hisse senetlerini analiz etmek ve geçmiş fiyat ve hacim verilerine dayalı potansiyel ticaret sinyalleri oluşturmak için kullanılabilir. Oluşturulan istatistikler ve görselleştirmeler, bilinçli ticaret kararları alınmasına yardımcı olur.

### Not
Bu proje, BIST 100 hisse senetlerindeki potansiyel alım satım fırsatlarının belirlenmesinde piyasa profili analizinin bir araç olarak kullanılmasına odaklanmaktadır. Mali tavsiye sağlamaz ve yalnızca eğitim amaçlı ve araştırma amaçlı kullanılmalıdır.


## English
## BIST 100 Stocks Market Profile and Trading Signals
### Purpose
The purpose of this project is to analyze BIST 100 stocks using market profile analysis and identify potential trading signals based on specific market conditions derived from market profile indicators.

### How It Works
**1. Market Profile Calculation:**

- **Market Profile:** Market profile is a technique that shows price distribution over time, helping traders understand where trading activity is concentrated.
- **Value Area:** Identifies the range of prices where a specified percentage of total volume traded occurred.
- **Point of Control (POC):** Represents the price level at which the most trading volume occurred.

**2. Implementation Steps:**

- **Fetch Stock List:** Retrieves the list of BIST 100 stocks from a specified source.
- Fetch Historical Data: Retrieves historical price and volume data for each stock using the TVDatafeed library.
- **Calculate Market Profile:** Computes the value area high (VAH), value area low (VAL), and point of control (POC) for each segment of historical data.
- **Generate Candlestick Chart:** Visualizes the stock's price movements along with the market profile indicators using the mplfinance library.
- **Identify Trading Signals:** Determines potential entry and exit points based on the relationship between the closing price and the VAL (buy signal) or VAH (sell signal).

### Benefits
- **Visual Insight:** Provides a visual representation of price distribution and trading activity levels over specified time intervals.
- **Trading Signals:** Generates buy and sell signals based on the intersection of closing prices with value area indicators (VAL and VAH).
- **Statistical Analysis:** Calculates key trading performance metrics such as total return, win rate, and Sharpe ratio to evaluate the effectiveness of the strategy.

### Usage
This script can be used by traders and analysts to analyze BIST 100 stocks using market profile analysis and generate potential trading signals based on historical price and volume data. The generated statistics and visualizations assist in making informed trading decisions.

### Note
This project focuses on using market profile analysis as a tool for identifying potential trading opportunities in BIST 100 stocks. It does not provide financial advice and should be used for educational purposes and research only.

