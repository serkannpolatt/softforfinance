## Türkçe
## BIST 100 Hisse Senedi Bollinger Bantları Sıkışma Analizi

### Amaç
Bu projenin amacı Bollinger Bands sıkıştırma stratejisini kullanarak BIST 100 hisse senetlerindeki potansiyel işlem fırsatlarını tespit etmektir. Bollinger Bantları, yatırımcıların volatilite daralması ve ardından genişlemeye dayalı olarak potansiyel fiyat hareketlerini gösteren potansiyel giriş noktalarını belirlemelerine yardımcı olan bir teknik analiz aracıdır.

### Nasıl çalışır
**1. Bollinger Bantları Hesaplaması:**

- **Bollinger Bantları üç çizgiden oluşur:** orta çizgi (basit hareketli ortalama), üst bant (SMA + 2 standart sapma) ve alt bant (SMA - 2 standart sapma).
- **Sıkışma Tanımlaması:** Üst ve alt bantlar arasındaki mesafe tarihsel olarak düşük seviyelere daraldığında, düşük volatiliteye işaret eden bir sıkışma meydana gelir.

**2. Uygulama Adımları:**
- **Hisse Senedi Listesini Getir:** Belirli bir kaynaktan BIST 100 hisse senetlerinin listesini alır.
- **Geçmiş Fiyatları Getir:** Her hisse senedi için geçmiş gün içi fiyatları bir finansal veri sağlayıcısından alınır.
- **Bollinger Bantlarını Hesaplayın:** Her hisse senedi için Bollinger Bantlarını hesaplar ve bant genişliğinin (üst ve alt bantlar arasındaki fark) belirli bir eşiğin altında olduğu, bir sıkışmayı işaret eden dönemleri tanımlar.
- **Grafik Oluştur ve Kaydet:** Bir sıkışma tespit edilirse, Bollinger Bantlarıyla birlikte hisse senedi fiyatının bir grafiği oluşturulur ve daha fazla analiz için kaydedilir.

### Faydalar
Sinyal Potansiyeli Kırılmaları: Bollinger Bantlarındaki sıkışmalar genellikle önemli fiyat hareketlerinden önce gelir ve yatırımcıların potansiyel kırılmaları veya kırılmaları öngörmesine yardımcı olur.
Teknik Analiz Aracı: Geçmiş fiyat verilerine dayanarak volatiliteyi ve potansiyel ticaret fırsatlarını değerlendirmek için görsel ve niceliksel bir yöntem sağlar.

### Kullanım
Bu komut dosyası, tüccarlar ve analistler tarafından BIST 100 hisse senetlerini Bollinger Bands sıkışmalarına karşı otomatik olarak taramak için kullanılabilir. Yatırımcılar, düşük volatilite dönemlerini tespit ederek sonraki fiyat hareketlerinden yararlanmaya hazırlanabilirler. Oluşturulan grafikler, sıkışıklığın net bir şekilde görselleştirilmesini sağlayarak karar verme süreçlerine yardımcı olur.

### Not
Bu proje, bağımsız bir teknik analiz stratejisi olarak Bollinger Bantları sıkışmalarını tanımlamaya odaklanmaktadır. Bollinger Bantları sinyallerinin yorumlanmasının ötesinde ek ticaret stratejileri veya finansal tavsiyeler içermez.


## English
## Bollinger Bands Squeeze Analysis for BIST 100 Stocks

### Purpose
The purpose of this project is to identify potential trading opportunities in BIST 100 stocks using the Bollinger Bands squeeze strategy. Bollinger Bands are a technical analysis tool that helps traders identify potential entry points based on volatility contraction followed by expansion, indicating potential price movements.

### How It Works
**1. Bollinger Bands Calculation:**

- **Bollinger Bands consist of three lines:** the middle line (simple moving average), an upper band (SMA + 2 standard deviations), and a lower band (SMA - 2 standard deviations).
- **Squeeze Identification:** A squeeze occurs when the distance between the upper and lower bands narrows to historically low levels, indicating low volatility.

**2. Implementation Steps:**
- **Fetch Stock List:** Retrieves the list of BIST 100 stocks from a specified source.
- **Fetch Historical Prices:** For each stock, historical intraday prices are fetched from a financial data provider.
- **Calculate Bollinger Bands:** Calculates the Bollinger Bands for each stock and identifies periods where the bandwidth (difference between upper and lower bands) is below a specified threshold, indicating a squeeze.
- **Plot and Save:** If a squeeze is detected, a plot of the stock's price along with its Bollinger Bands is generated and saved for further analysis.

### Benefits
Signal Potential Breakouts: Squeezes in Bollinger Bands often precede significant price movements, helping traders anticipate potential breakouts or breakdowns.
Technical Analysis Tool: Provides a visual and quantitative method to assess volatility and potential trading opportunities based on historical price data.

### Usage
This script can be used by traders and analysts to scan BIST 100 stocks automatically for Bollinger Bands squeezes. By identifying periods of low volatility, traders can prepare to capitalize on subsequent price movements. The generated plots provide a clear visualization of the squeeze, aiding in decision-making processes.

### Note
This project focuses on identifying Bollinger Bands squeezes as a standalone technical analysis strategy. It does not include additional trading strategies or financial advice beyond the interpretation of Bollinger Bands signals.

