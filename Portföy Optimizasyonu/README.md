## Türkçe
## Portföy Optimizasyonu
Bu Python kodu, Borsa İstanbul'da bulunan 94 adet hisse senedinin günlük kapanış fiyatlarından yola çıkarak portföy optimizasyonu yapmayı amaçlamaktadır. Kod, Monte Carlo Simülasyonu ve Modern Portföy Teorisi'nin temel prensiplerini kullanarak, yatırımcılara belirli bir risk seviyesi altında maksimum getiriyi elde etmelerini sağlayan optimal portföyü bulma amacını taşımaktadır.

### Kullanım

**1. Veri Yükleme:**
- Kod, belirtilen DATA_DIR dizinindeki hisse senedi verilerini toplar ve birleştirir. Verilerin CSV dosyalarında olması beklenir.

**2. Veri Temizleme ve İşleme:**
- Kod, hisse senedi isimlerini çıkarır, veri çerçevesini hazırlar ve belirli bir tarih aralığını seçer.

**3. Portföy Optimizasyonu:**
- Monte Carlo Simülasyonu kullanılarak farklı portföy ağırlıkları denenecek ve Sharpe oranı maksimize edilmeye çalışılacaktır.

**4. Sonuçları Görselleştirme:**
- Elde edilen portföylerin verimlilik sınırları çizilir ve en düşük volatiliteye sahip ve en yüksek Sharpe oranına sahip portföyler belirlenir.

**5. Optimal Portföyü Bulma:**
- En yüksek Sharpe oranına sahip olan ve minimum volatiliteye sahip olan portföy bulunur.

## English
## Portfolio Optimization
This Python code enables placement based on the daily ongoing prices of 94 stocks in Borsa Istanbul. Using the basic principles of Code, Monte Carlo Simulation and Modern Portfolio Theory, we aim to find the optimal portfolio that allows them to achieve maximum carry under a given level of risk.

### Usege

**1. Data Loading:**
- The code is a collection and concatenation of sense isolations in the specified DATA_DIR array. Enables data to be found in CSV files.

**2. Data Cleansing and Processing:**
- The code extracts stock names, prepares the dataframe and selects a specific date range.

**3. Portfolio Optimization:**
- Different portfolio weights will be tried using Monte Carlo Simulation and the Sharpe ratio will be tried to be maximized.

**4. Visualizing Results:**
- Efficiency zones of the resulting portfolios can be drawn and the portfolios with the lowest volatility and highest Sharpe characteristics were determined.

**5. Finding the Optimal Portfolio:**
- There is a portfolio with the highest sharpness and minimum volatility.