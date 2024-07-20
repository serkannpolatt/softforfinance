## Türkçe
## Trend Kanal Analizi ve Çıkış Tespiti
### Amaç
Bu scriptin amacı BIST (Borsa İstanbul)'de işlem gören hisse senetlerinin trend kanallarını doğrusal regresyon kullanarak analiz etmek ve potansiyel trend kırılmalarını tespit etmektir. Trend kanalları, yukarı veya aşağı doğru kırılmaları belirlemek için son kapanış fiyatlarına göre görselleştirilir ve analiz edilir.

### Nasıl çalışır
**1. Temel Verileri Getir:**

- **Hisse_Temel_Veriler:** pd.read_html kullanarak belirli bir web sayfasından stok kodları listesini alır.

**2. Geçmiş Hisse Senedi Fiyatlarını Getir:**

- **Stock_Prices:** İş Yatırım'dan bir API uç noktası kullanarak her hisse senedi için geçmiş fiyat ve hacim verilerini alır.

**3. Trend Kanal Analizi:**

- **Trend_Channel:** Farklı kapanış fiyatları dönemlerine uyan doğrusal regresyon çizgilerinin korelasyon katsayısını (R-değeri) değerlendirerek trend analizi için en uygun dönemi belirler.

**4. Çizim ve Koparma Tespiti:**

- **Plot_Trendlines:** Trend_Channel tarafından belirlenen en iyi döneme göre kapanış fiyatlarını trend çizgisi ve üst/alt kanallarla birlikte çizer.
- **Koparma Tespiti:** Koparma koşullarını kontrol eder:
- **Yukarı doğru kırılma:** Kapanış fiyatı üst kanalın üzerine çıktığında tespit edilir.
- **Aşağı Kırılım:** Kapanış fiyatı alt kanalın altına düştüğünde tespit edilir.
- **Grafikleri Kaydetme:** Algılanan kesintilerin grafiklerini PNG formatında kaydeder.

### Faydalar
- **Görsel Analiz:** Her hisse senedi için trend kanallarının ve kırılmaların görsel temsillerini sağlar.
- **Otomatik Analiz:** Veri alma, trend analizi yapma ve birden fazla hisse senedi için kırılmaları tespit etme sürecini otomatikleştirir.
- **Karar Desteği:** Yatırımcıların ve analistlerin trend kanalı analizine dayanarak potansiyel ticaret fırsatlarını belirlemelerine yardımcı olur.

### Kullanım
Bu komut dosyası, teknik analiz ve trend takip stratejileriyle ilgilenen yatırımcılar ve analistler için faydalıdır. Son fiyat hareketlerine ve trend kanallarına dayanarak potansiyel çıkış yapan işlemlere ilişkin eyleme geçirilebilir bilgiler sağlar.

### Not
Bu proje, doğrusal regresyon teknikleri kullanılarak BIST'te listelenen hisse senetleri için trend kanalı analizi ve kırılma tespitine odaklanmaktadır. Mali tavsiye sağlamaz ve yalnızca eğitim amaçlı ve araştırma amaçlı kullanılmalıdır.

## Trend Channel Analysis and Breakout Detection
### Purpose
The purpose of this script is to analyze the trend channels of stocks listed on BIST (Borsa Istanbul) using linear regression and to detect potential trend breakouts. Trend channels are visualized and analyzed based on recent closing prices to identify upward or downward breakouts.

### How It Works
**1. Fetch Fundamental Data:**

- **Hisse_Temel_Veriler:** Retrieves the list of stock codes from a specified webpage using pd.read_html.

**2. Fetch Historical Stock Prices:**

- **Stock_Prices:** Retrieves historical price and volume data for each stock using an API endpoint from Is Yatirim.

**3. Trend Channel Analysis:**

- **Trend_Channel:** Determines the optimal period for trend analysis by evaluating the correlation coefficient (R-value) of linear regression lines fitted to different periods of closing prices.

**4. Plotting and Breakout Detection:**

- **Plot_Trendlines:** Plots the closing prices along with the trendline and upper/lower channels based on the best period determined by Trend_Channel.
- **Breakout Detection:** Checks for breakout conditions:
- **Upward Breakout:** Detected when the closing price breaks above the upper channel.
- **Downward Breakout:** Detected when the closing price breaks below the lower channel.
- **Saving Plots:** Saves plots of detected breakouts in PNG format.

### Benefits
- **Visual Analysis:** Provides visual representations of trend channels and breakouts for each stock.
- **Automated Analysis:** Automates the process of fetching data, performing trend analysis, and detecting breakouts for multiple stocks.
- **Decision Support:** Helps traders and analysts identify potential trading opportunities based on trend channel analysis.

### Usage
This script is useful for traders and analysts interested in technical analysis and trend following strategies. It provides actionable insights into potential breakout trades based on recent price movements and trend channels.

### Note
This project focuses on trend channel analysis and breakout detection for stocks listed on BIST using linear regression techniques. It does not provide financial advice and should be used for educational purposes and research only.