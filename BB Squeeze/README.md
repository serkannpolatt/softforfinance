## Türkçe 
## BIST 100 Hisse Senedi Bollinger Bantları Sıkışma Analizi

Bu depo, BIST 100 endeksinde listelenen hisse senetleri için Bollinger Bands sıkışmasını analiz etmek üzere tasarlanmış bir Python betiği içerir. Komut dosyası, temel hisse senedi verilerini alır, geçmiş hisse senedi fiyatlarını getirir, Bollinger Bantlarını ve bunların sıkışıklığını hesaplar ve sonuçları görselleştirir. Aşağıda bileşenlerin ve amaçlarının ayrıntılı bir açıklaması bulunmaktadır.

### Genel Bakış
Komut dosyası aşağıdaki temel görevleri gerçekleştirir:

**1. Veri Erişimi:** BIST 100 şirketlerinin temel verilerini ve geçmiş hisse senedi fiyatlarını getirir.
**2. Bollinger Bantları Hesaplaması:** Bollinger Bantlarını hesaplar ve sıkışma dönemlerini belirler.
**3. Görselleştirme:** Bollinger Bantlarını çizer ve grafiklerdeki sıkışma noktalarını işaretler.

### İşlevler
**1. Hisse_Temel_Veriler**
- BIST 100 hisse senedine ait temel verileri İş Yatırım'dan alır.
- HTML içeriğinden stok sembollerini ayrıştırır.
- Hisse senedi sembollerinin bir listesini döndürür.

**2. Stok fiyatları**
- İş Yatırım'ın API'sini kullanarak belirli bir hisse senedi sembolüne ait geçmiş hisse senedi fiyatlarını getirir.
- Hisse senedi fiyatı ve hacim verilerini içeren bir DataFrame döndürür.

**3. BBands_Squeeze**
- Verilen hisse senedi fiyat verileri için Bollinger Bantlarını hesaplar.
- Bant genişliği yüzdesinin belirli bir eşiğin altında olduğu Bollinger Bantları sıkışma dönemlerini tanımlar.
- Bollinger Bantları ve sıkıştırma bilgileri içeren bir DataFrame döndürür.

**4. Plot_BBands_with_Squeeze**
- Hisse senedinin kapanış fiyatını Bollinger Bantlarıyla birlikte çizer.
- Grafikteki en son sıkışma noktasını işaretler.
- Grafiği PNG dosyası olarak kaydeder.

### Örnek Hisse Senetleri
Senaryo, İş Yatırım internet sitesinden alınan BIST 100 endeksinde yer alan tüm hisse senetlerini analiz ediyor. Komut dosyası, her hisse senedi için geçmiş fiyatları getirir, Bollinger Bantlarını hesaplar, sıkışma noktalarını belirler ve son 10 dönem içinde bir sıkışma tespit edilirse bir grafik oluşturur.

### Sonuçlar
Komut dosyası, işlenmekte olan hisse senedi sembolünü yazdırır ve son 10 dönemde Bollinger Bands sıkışması tespit edilen hisse senetleri için PNG dosyaları oluşturur. Her PNG dosyası <StockSymbol>_BB_Sıkışması.png formatında adlandırılır.

### Çözüm
Bu script, BIST 100 hisse senetleri üzerindeki Bollinger Bands sıkışmasını analiz etmek için kapsamlı bir araç sağlar. Teknik analiz ve görselleştirme tekniklerinden yararlanarak yatırımcıların ve analistlerin düşük volatilite dönemlerinde potansiyel ticaret fırsatlarını belirlemelerine yardımcı olur.

## English
## BIST 100 Stocks Bollinger Bands Squeeze Analysis

This repository contains a Python script designed to analyze Bollinger Bands squeeze for stocks listed in the BIST 100 index. The script retrieves fundamental stock data, fetches historical stock prices, calculates Bollinger Bands and their squeeze, and visualizes the results. Below is a detailed explanation of the components and their purposes.

### Overview
The script performs the following key tasks:

**1. Data Retrieval:** Fetches fundamental data and historical stock prices for BIST 100 companies.
**2. Bollinger Bands Calculation:** Computes Bollinger Bands and identifies periods of squeeze.
**3. Visualization:** Plots the Bollinger Bands and marks the squeeze points on the charts.

### Functions
**1. Hisse_Temel_Veriler**
- Retrieves the fundamental data of BIST 100 stocks from İş Yatırım.
- Parses the stock symbols from the HTML content.
- Returns a list of stock symbols.

**2. Stock_Prices**
- Fetches historical stock prices for a given stock symbol using İş Yatırım's API.
- Returns a DataFrame with the stock price and volume data.

**3. BBands_Squeeze**
- Calculates Bollinger Bands for the given stock price data.
- Identifies periods of Bollinger Bands squeeze, where the band width percentage is below a specified threshold.
- Returns a DataFrame with Bollinger Bands and squeeze information.

**4. Plot_BBands_with_Squeeze**
- Plots the stock's closing price along with the Bollinger Bands.
- Marks the most recent squeeze point on the chart.
- Saves the plot as a PNG file.

### Example Stocks
The script analyzes all stocks listed in the BIST 100 index, as retrieved from the İş Yatırım website. For each stock, the script fetches historical prices, calculates Bollinger Bands, identifies squeeze points, and generates a plot if a squeeze is detected within the last 10 periods.

### Results
The script prints the stock symbol being processed and generates PNG files for stocks where a Bollinger Bands squeeze is detected in the last 10 periods. Each PNG file is named in the format <StockSymbol>_BB_Sıkışması.png.

### Conclusion
This script provides a comprehensive tool for analyzing Bollinger Bands squeeze on BIST 100 stocks. By leveraging technical analysis and visualization techniques, it helps traders and analysts identify potential trading opportunities during periods of low volatility.