## Türkçe
## Makine Öğrenimi Yatırımcısı

### Genel Bakış
Bu Python betiği, lumibot kütüphanesi kullanılarak uygulanan bir makine öğrenimi ticaret stratejisini göstermektedir. Strateji, ticari kararlar vermek için finansal haberlere ilişkin duyarlılık analizini kullanıyor. İşlemleri gerçekleştirmek için Alpaca API ile entegre olur ve duyarlılık analizi için FinBERT modelini kullanır.

### Amaç
Bu senaryonun amacı, borsada alım satım kararları vermek için finansal haberlerin duyarlılık analizini içeren, makine öğrenimine dayalı bir ticaret stratejisini sergilemektir.

### Nasıl çalışır
**1. Alpaca API Entegrasyonu:** Komut dosyası, piyasa verilerine erişmek ve işlemleri yürütmek için sağlanan API anahtarlarını kullanarak Alpaca API'sine bağlanır.
**2. Strateji Başlatma:** MLTrader sınıfı, işlem stratejisini, işlem yapılacak sembol ve her işlemde riske atılacak nakit yüzdesi gibi parametrelerle başlatır.
**3. Duyarlılık Analizi:** get_sentiment işlevi, Alpaca API'sini kullanarak finansal haber verilerini getirir ve FinBERT modelini kullanarak haber makalelerinin duyarlılığını analiz eder.
**4. Ticaret Mantığı:** Duyarlılık analizi sonuçlarına ve önceden tanımlanmış olasılık eşiklerine dayanarak, strateji satın alma veya satma kararları verir ve kar al ve zararı durdur fiyatlarıyla parantez emirleri verir.
**5. Geriye dönük test:** Komut dosyası, Yahoo Finance'den alınan geçmiş verileri kullanarak ticaret stratejisinin geriye dönük testini gerçekleştirir.

### Gereksinimler
- Python 3.x
- lumibot kütüphanesi
- Alpaka Ticaret API'si
- finbert kütüphanesi
- transformatörler kütüphanesi

### Not
- Betiği çalıştırmadan önce API anahtarlarının ve diğer kimlik bilgilerinin doğru şekilde yapılandırıldığından emin olun.
- Ticaret sembolü ve risk altındaki nakit yüzdesi gibi parametreleri tercihlerinize ve risk toleransınıza göre ayarlayın.
- Komut dosyası yalnızca eğitim ve tanıtım amaçlı sağlanmıştır. Gerçek ticaret riskler içerir ve dikkatli yapılmalıdır.

### Sorumluluk reddi beyanı
Bu komut dosyası herhangi bir garanti olmaksızın olduğu gibi sağlanmaktadır. Yazarlar doğruluğunu veya herhangi bir özel amaca uygunluğunu garanti etmez. Riski size ait olmak üzere kullanın.

## English
## Machine Learning Trader

### Overview
This Python script demonstrates a machine learning trading strategy implemented using the lumibot library. The strategy utilizes sentiment analysis on financial news to make trading decisions. It integrates with the Alpaca API for executing trades and utilizes the FinBERT model for sentiment analysis.

### Purpose
The purpose of this script is to showcase a machine learning-based trading strategy that incorporates sentiment analysis of financial news to make buy and sell decisions in the stock market.

### How it works
**1. Alpaca API Integration:** The script connects to the Alpaca API using provided API keys for accessing market data and executing trades.
**2. Strategy Initialization:** The MLTrader class initializes the trading strategy with parameters such as the symbol to trade and the percentage of cash to risk in each trade.
**3. Sentiment Analysis:** The get_sentiment function fetches financial news data using the Alpaca API and analyzes the sentiment of the news articles using the FinBERT model.
**4. Trading Logic:** Based on the sentiment analysis results and predefined probability thresholds, the strategy makes buy or sell decisions and places bracket orders with take-profit and stop-loss prices.
**5. Backtesting:** The script performs backtesting of the trading strategy using historical data fetched from Yahoo Finance.

### Requirements
- Python 3.x
- lumibot library
- Alpaca Trade API
- finbert library
- transformers library

### Note
- Ensure proper configuration of API keys and other credentials before running the script.
- Adjust parameters such as the symbol to trade and cash-at-risk percentage according to your preferences and risk tolerance.
- The script is provided for educational and demonstration purposes only. Actual trading involves risks and should be done cautiously.

### Disclaimer
This script is provided as-is without any warranties. The authors do not guarantee its accuracy or suitability for any specific purpose. Use it at your own risk.