## Türkçe
## Hisse Fiyat Trendi ve Sinyal Tespiti
Bu Python scripti, Türkiye Borsası'nda (BIST) listelenen hisse senetleri için fiyat trendi analizi yapar ve belirli sinyalleri tanımlar.

### Amaç
Bu betiğin amacı, Türkiye Borsası'nda listelenen hisse senetleri için aşağıdaki işlemleri gerçekleştirmektir:

**1. Trend Analizi:** Her hisse senedi için geçmiş fiyat verilerini analiz ederek bir trend çizgisi çıkarır.
**2. Sinyal Tespiti:** Belirlenen trend çizgisine göre alım veya satım sinyalleri tanımlar.
**3. Sonuçları Filtreleme:** Elde edilen sonuçları belirli kriterlere göre filtreler ve kullanıcıya sunar.

### Kullanım
1. Betiği çalıştırmak için Python yüklü olmalıdır.
2. Betiği indirin ve bir Python IDE'si veya metin editörü ile açın.
3. Kodun başında belirtilen kütüphaneleri yükleyin.
4. Betiği çalıştırın. Sonuçlar, terminal veya konsol üzerinde görüntülenecektir.

### Detaylar
- **Down_Trend_Line** fonksiyonu, verilen bir hisse senedinin fiyat verileri üzerinde eğim hesaplaması yapar ve trend çizgisini belirler.
- **get_all_symbols** fonksiyonu, Türkiye Borsası'ndaki tüm hisse senedi sembollerini alır.
- Betik, her hisse senedi için ayrı ayrı trend analizi yapar ve sonuçları** Yakınlık Durumu** ve **Kırılma Durumu** kriterlerine göre filtreler.

## English
## Stock Price Trend and Signal Detection
This Python script performs price trend analysis on the Turkish Stock Exchange (BIST) for their performance around the world and is organized in a specific way.

### Aim
The purpose of this script is to initiate the following transactions for transactions around the world on the Turkish Stock Exchange:

**one. Trend Analysis:** By analyzing the past price balance for the stock, a trend line emerges.
**2. Signal Detection:** Buying or selling is continued according to the determined trend line.
**3. Filtering Results:** The results obtained are filtered according to certain parameters and presented personally.

### Use
1. Python must be installed to run the script.
2. Download the script and open it with a Python IDE or text computer.
3. Load the libraries mentioned at the beginning of the code.
4. The script is run. The results will be displayed on the terminal or console.

### Details
- **Down_Trend_Line** function performs rating programming on the price data of a given stock and determines the trend line.
- **get_all_symbols** function gets all stock symbols on Turkish Stock Exchange.
- The script performs trend analysis for its own stocks separately and filters the results according to **Nearness Status** and **Break Status** criteria.