## Türkçe
## İngilizce
## BIST 100 Hisse Analizi ve Ticaret Stratejisi

Bu depo, BIST 100 endeksinde listelenen hisse senetleri için alım satım stratejilerini analiz etmek ve uygulamak üzere tasarlanmış bir Python betiği içerir. Komut dosyası, kapsamlı bir ticaret stratejisi değerlendirmesi sağlamak için çeşitli teknik analiz göstergelerini ve kitaplıklarını kullanır. Aşağıda bileşenlerin ve amaçlarının ayrıntılı bir açıklaması bulunmaktadır.

### Genel Bakış
Komut dosyası aşağıdaki temel görevleri gerçekleştirir:

- **Veri Alma:** Çeşitli veri kaynaklarını kullanarak BIST 100 şirketlerinin geçmiş hisse senedi verilerini getirir.
- **Teknik Gösterge Hesaplaması:** ADX, WaveTrend, Tillson T3 ve Optimize Edilmiş Trend Takipçisi (OTT) dahil olmak üzere birden fazla teknik göstergeyi hesaplar.
- **Ticaret Stratejisi Uygulaması: **Alış ve satış sinyalleri oluşturmak için hesaplanan göstergelere dayalı bir ticaret stratejisi uygular.
- **Performans Değerlendirmesi:** Vectorbt kütüphanesini kullanarak ticaret stratejisinin performansını değerlendirir ve sonuçları derler.

### Teknik Göstergeler
**1. Ortalama Yön Endeksi (ADX)**
- Bir trendin gücünü ölçer.
- Yüksek, düşük ve kapanış fiyatları kullanılarak hesaplanır.

**2. Dalga Trendi (WT)**
- Piyasa trendlerini ve potansiyel geri dönüş noktalarını belirleyen bir osilatör.
- Yüksek, düşük ve kapanış fiyatları kullanılarak hesaplanır.

**3. Tillson T3**
- Üstel hareketli ortalamanın (EMA) gecikmeyi azaltan daha yumuşak bir versiyonu.
- Kapanış, yüksek ve düşük fiyatlar kullanılarak hesaplanır.

**4. Optimize Edilmiş Trend Takipçisi (OTT)**
- Gelişmiş bir trend takip göstergesi.
- Kapanış fiyatları ve kümülatif hareketli ortalamaları içeren özel bir formül kullanılarak hesaplanır.

### Ticaret Stratejisi
- **Giriş Durumu:** OTT göstergesi ve Z-skor göstergesi belirli koşulları karşıladığında bir satın alma sinyali oluşturulur.
- **Çıkış Durumu:** Tillson T3 göstergesine dayalı olarak bir satış sinyali oluşturulur.
- **Geriye dönük test:** Strateji, toplam işlemler, kazanma oranı, toplam getiri ve ortalama kazanan işlem gibi performans ölçümlerini değerlendirmek için Vectorbt kullanılarak geriye doğru test edilir.

### Örnek Hisse Senetleri
Komut dosyası, AEFES, AGHOL, AHGAZ ve diğerleri gibi BIST 100 hisse senetlerinin bir listesini analiz eder. Her hisse senedi için strateji uygulanır ve sonuçlar bir DataFrame'de derlenir.

### Sonuçlar
Her hisse senedinin sonuçları, hisse senedi adını, toplam işlem sayısını, kazanma oranını, toplam getiriyi ve ortalama kazanan ticareti gösterecek şekilde konsola yazdırılır. Sonuçlar ayrıca daha fazla analiz için bir DataFrame'de derlenir.

### Çözüm
Bu script, BIST 100 hisse senetleri üzerindeki işlem stratejilerini analiz etmek ve test etmek için kapsamlı bir araç sağlar. Çeşitli teknik göstergelerden ve geriye dönük test yöntemlerinden yararlanarak yatırımcıların ve analistlerin stratejilerinin etkinliğini değerlendirmelerine ve bilinçli kararlar almalarına yardımcı olur.


## English
## BIST 100 Stock Analysis and Trading Strategy

This repository contains a Python script designed to analyze and implement trading strategies for stocks listed in the BIST 100 index. The script utilizes several technical analysis indicators and libraries to provide a comprehensive trading strategy evaluation. Below is a detailed explanation of the components and their purposes

### Overview
The script performs the following key tasks:

- **Data Retrieval:** Fetches historical stock data for BIST 100 companies using various data sources.
- **Technical Indicators Calculation:** Computes multiple technical indicators, including ADX, WaveTrend, Tillson T3, and Optimized Trend Tracker (OTT).
- **Trading Strategy Implementation: **Applies a trading strategy based on the calculated indicators to generate buy and sell signals.
- **Performance Evaluation:** Evaluates the performance of the trading strategy using the vectorbt library and compiles the results.

### Technical Indicators
**1. Average Directional Index (ADX)**
- Measures the strength of a trend.
- Computed using high, low, and close prices.

**2. WaveTrend (WT)**
- An oscillator to identify market trends and potential reversal points.
- Computed using high, low, and close prices.

**3. Tillson T3**
- A smoother version of the exponential moving average (EMA) that reduces lag.
- Computed using closing, high, and low prices.

**4. Optimized Trend Tracker (OTT)**
- An advanced trend-following indicator.
- Computed using closing prices and a custom formula involving cumulative moving averages.

### Trading Strategy
- **Entry Condition:** A buy signal is generated when the OTT indicator and the Z-score indicator meet certain conditions.
- **Exit Condition:** A sell signal is generated based on the Tillson T3 indicator.
- **Backtesting:** The strategy is backtested using vectorbt to evaluate performance metrics such as total trades, win rate, total return, and average winning trade.

### Example Stocks
The script analyzes a list of BIST 100 stocks, such as AEFES, AGHOL, AHGAZ, and others. For each stock, the strategy is applied, and the results are compiled into a DataFrame.

### Results
The results for each stock are printed to the console, showing the stock name, total number of trades, win rate, total return, and average winning trade. The results are also compiled into a DataFrame for further analysis.

### Conclusion
This script provides a comprehensive tool for analyzing and testing trading strategies on BIST 100 stocks. By leveraging various technical indicators and backtesting methods, it helps traders and analysts evaluate the effectiveness of their strategies and make informed decisions.