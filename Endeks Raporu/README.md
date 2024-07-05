## BIST Endeks Günlük Raporu
Bu Python betiği, çeşitli BIST (Borsa İstanbul) endekslerindeki günlük yüzde değişimlerini analiz etmek ve görselleştirmek için tasarlanmıştır. Betik, seçilen endeksler için geçmiş verileri alır, günlük yüzde değişimlerini hesaplar ve görsel bir rapor oluşturur. Aşağıda, bileşenlerin ve amaçlarının ayrıntılı bir açıklaması bulunmaktadır.

### Genel Bakış
Betik şu anahtar görevleri yerine getirir:

**1. Veri Alımı:** Seçilen BIST endekslerinin geçmiş kapanış fiyatlarını alır.
**2. Yüzde Değişim Hesaplama:** Her bir endeks için günlük yüzde değişimini hesaplar.
**3. Görselleştirme:** Yüzde değişimlerini görselleştirmek için tablo ve çubuk grafik oluşturur ve raporu bir resim olarak kaydeder.

### Fonksiyonlar
**1. create_table_image**
- Bir tablo ve çubuk grafik kombinasyonu ile görsel bir rapor oluşturur.
- Tablo, her endeks için yüzde değişimlerini sıralar.
- Çubuk grafik, yüzde değişimlerini renk geçişi ile görselleştirir.


**2. retrieve_data**
- Belirli bir sembol için TradingView'den geçmiş kapanış fiyatı verilerini alır.
- Geçici veri alım hatalarını yönetmek için retry dekoratörünü kullanır.

### Endeks Listesi
Betik aşağıdaki BIST endekslerini analiz eder:
- BIST 30
- BIST 100
- BIST İnşaat
- BIST Bilişim
- BIST Teknoloji
- Gayrimenkul Y.O.
- BIST Holding ve Yatırım
- BIST Fin. Kir. Faktoring
- BIST Sigorta
- BIST Banka
- BIST Mali
- BIST İletişim
- BIST Turizm
- BIST Ulaştırma
- BIST Elektrik
- BIST Hizmetler
- BIST Metal Eşya Makine
- BIST Metal Ana
- BIST Taş Toprak
- BIST Kimya Petrol Plastik
- BIST Orman Kağıt Basım
- BIST Tekstil Deri
- BIST Gıda İçecek
- BIST Sınai
- BIST Maden

Her endeks için betik, son 90 günün geçmiş verilerini alır ve günlük yüzde değişimini hesaplar.

### Sonuçlar
Betik, yüzde değişimlerini yazdırır ve Günlük_Endeks_Raporu.png adlı bir PNG dosyası oluşturur. Bu dosya, yüzde değişimlerinin tablo ve çubuk grafiklerini içerir.

### Sonuç
Bu betik, çeşitli BIST endekslerindeki günlük yüzde değişimlerini analiz etmek ve görselleştirmek için kapsamlı bir araç sunar. Teknik analiz ve görselleştirme tekniklerinden yararlanarak, yatırımcılar ve analistler piyasadaki potansiyel trendleri ve fırsatları belirlemelerine yardımcı olur.


## English
## BIST Index Daily Report
This Python script is designed to analyze and visualize daily percentage changes in various BIST (Borsa Istanbul) indices. The script retrieves historical data for selected indices, calculates daily percentage changes and creates a visual report. Below is a detailed description of the components and their purposes.

### Overview
The script performs these key tasks:

**1. Data Retrieval:** Retrieves past closing prices of selected BIST indices.
**2. Percentage Change Calculation:** Calculates the daily percentage change for each index.
**3. Visualization:** Creates tables and bar charts to visualize percentage changes and saves the report as an image.

### Functions
**1. create_table_image**
- Creates a visual report with a combination of a table and bar chart.
- The table lists the percentage changes for each index.
- Bar chart visualizes percentage changes with color transition.


**2. retrieve_data**
- Retrieves historical closing price data from TradingView for a given symbol.
- Uses retry decorator to handle temporary data retrieval errors.

### Index List
The script analyzes the following BIST indices:
-BIST 30
- BIST 100
- BIST Construction
- BIST Informatics
- BIST Technology
- Real Estate Y.O.
- BIST Holding and Investment
- BIST Fin. Dirt. Factoring
- BIST Insurance
- BIST Bank
- BIST Financial
- BIST Contact
- BIST Tourism
- BIST Transportation
- BIST Electric
- BIST Services
- BIST Metal Goods Machinery
- BIST Metal Main
- BIST Stone Soil
- BIST Chemistry Petroleum Plastic
- BIST Orman Paper Printing
- BIST Textile Leather
- BIST Food and Beverage
- BIST Industrial
- BIST Mining

For each index, the script retrieves historical data for the last 90 days and calculates the daily percentage change.

### Results
The script prints the percentage changes and creates a PNG file named Daily_Index_Report.png. This file contains tables and bar charts of percentage changes.

### Conclusion
This script provides a comprehensive tool to analyze and visualize daily percentage changes in various BIST indices. By utilizing technical analysis and visualization techniques, it helps investors and analysts identify potential trends and opportunities in the market.