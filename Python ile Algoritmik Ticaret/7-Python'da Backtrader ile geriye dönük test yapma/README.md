## Türkçe
## Geri Test İçin Hareketli Ortalama Çapraz Stratejisi

Bu proje, Backtrader çerçevesi ve Yahoo Finance'den gelen tarihsel hisse senedi fiyat verileri kullanılarak geri test yapmak için basit bir hareketli ortalama çapraz stratejisi oluşturmanın nasıl yapılacağını göstermektedir.

### Proje Amaçları

Bu proje, temel bir hareketli ortalama çapraz işlem stratejisi tanıtmak amacıyla tasarlanmıştır. Bu, tarihsel hisse senedi fiyat verileri kullanarak bir işlem stratejisi geliştirmenin ve test etmenin nasıl yapılacağına dair net bir örnek sunmayı amaçlar.

### Bileşenler

#### 1. Hareketli Ortalama Çapraz Stratejisi

Bu proje, `MovingAverageCrossStrategy` adlı özel bir işlem stratejisini içerir. Bu stratejinin ana bileşenleri şunlardır:

- **Kısa ve Uzun Hareketli Ortalamalar**: İşlem kararları almak için kısa ve uzun basit hareketli ortalamaları (SMA'lar) kullanır. Kısa SMA genellikle kısa bir döneme (örneğin 40 gün) sahiptir, uzun SMA ise daha uzun bir döneme (örneğin 100 gün) sahiptir.

- **Çapraz Gösterge**: Strateji, kısa SMA'nın uzun SMA'nın üstünde çapraz yaptığında alış sinyalleri üreten ve kısa SMA'nın uzun SMA'nın altına çapraz yaptığında satış sinyalleri üreten bir çapraz gösterge tanımlar.

#### 2. Veri Yükleme

Türk Hava Yolları (THYAO.IS) için Yahoo Finance'den tarihsel hisse senedi fiyat verileri, `yfinance` kütüphanesini kullanarak indirilir. Daha sonra veriler, Backtrader için uygun bir formata dönüştürülür.

#### 3. Geri Test Kurulumu

Geri test yapmak için Backtrader `Cerebro` örneği ayarlanır. Aşağıdaki konfigürasyonları içerir:

- Test edilecek işlem stratejisi olarak `MovingAverageCrossStrategy` eklenir.

- Tarihsel fiyat verileri `Cerebro` örneğine eklenir.

- Sanal portföy için başlangıçta 100.000 birimlik nakit miktarı ayarlanır.

#### 4. Ek Konfigürasyonlar (İsteğe Bağlı)

- Her işlem için bir sabit pozisyon boyutu (stake) `bt.sizers.FixedSize` kullanılarak 1000 birim olarak tanımlanır.

- Her işlem için %0.1 (0.001) komisyon belirlemek için `cerebro.broker.setcommission` ayarlanır.

#### 5. Geri Testi Çalıştırma

Geri test, `cerebro.run()` kullanılarak başlatılır. Belirtilen çapraz mantığa dayalı olarak tarihsel veriler üzerinde `MovingAverageCrossStrategy` işlemi simüle eder.

#### 6. Sonuçları Görselleştirme

Geri testin sonunda portföyün performansının görsel bir temsili `cerebro.plot()` kullanılarak görüntülenir. Bu görselleştirme, stratejinin karlılığı ve performansı hakkında bilgi sağlar.

### Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:

- Backtrader
- yfinance
- pandas
- numpy
- matplotlib

Bu kütüphaneleri `pip install` kullanarak veya bir `requirements.txt` dosyasına dahil ederek yükleyebilirsiniz.

### Projeyi Çalıştırma

Bu projeyi çalıştırmak için:

1. Gerekli Python kütüphanelerinin yüklendiğinden emin olun.
2. Sağlanan kodu bir Python betiği veya Jupyter Notebook'a kopyalayın.
3. Betiği veya notebook'u çalıştırarak geri testi başlatın.
4. Sonuçları ve görselleştirmeleri inceleyerek stratejinin performansını değerlendirin.

Keyifli geri testler!

## Geri Test İçin Bollinger Bantları ve RSI Stratejisi

Bu proje, Bollinger Bantları ve Relative Strength Index (RSI) göstergelerini birleştiren bir işlem stratejisi oluşturmanın ve Backtrader çerçevesi kullanarak Yahoo Finance'den gelen tarihsel hisse senedi fiyat verileri ile geri test yapmanın nasıl yapılacağını göstermektedir.

### Proje Amaçları

Bu proje, birden fazla teknik göstergeyi işlem kararları için kullanan daha gelişmiş bir işlem stratejisi tanıtmayı amaçlar. Bollinger Bantları ve RSI göstergelerini kullanarak ticaret stratejisi örnekleyen bir örnek sunmayı amaçlar.

### Bileşenler

#### 1. Bollinger Bantları ve RSI Stratejisi

Bu proje, `BollingerRSIStrategy` adlı özel bir işlem stratejisini içerir. Bu stratejinin ana bileşenleri şunlardır:

- **Bollinger Bantları**: Fiyatın volatiliteye dayalı potansiyel alım ve satım sinyallerini tanımlamak için Bollinger Bantları kullanır.

- **Relative Strength Index (RSI)**: Strateji, aşırı alım ve aşırı satım koşullarını tanımlamak için RSI göstergesini içerir.

#### 2. Veri Yükleme

Türk Hava Yolları (THYAO.IS) için Yahoo Finance'den gelen tarihsel hisse senedi fiyat verileri, `yfinance` kütüphanesini kullanarak indirilir. Daha sonra veriler, Backtrader için uygun bir formata dönüştürülür.

#### 3. Geri Test Kurulumu

Geri test yapmak için Backtrader `Cerebro` örneği ayarlanır. Aşağıdaki konfigürasyonları içerir:

- Test edilecek işlem stratejisi olarak `BollingerRSIStrategy` eklenir.

- Tarihsel fiyat verileri `Cerebro` örneğine eklenir.

- Sanal portföy için başlangıçta 100.000 birimlik nakit miktarı ayarlanır.

#### 4. Ek Konfigürasyonlar (İsteğe Bağlı)

- Her işlem için bir sabit pozisyon boyutu (stake) `bt.sizers.FixedSize` kullanılarak 1000 birim olarak tanımlanır.

- Her işlem için %0.1 (0.001) komisyon belirlemek için `cerebro.broker.setcommission` ayarlanır.

#### 5. Geri Testi Çalıştırma

Geri test, `cerebro.run()` kullanılarak başlatılır. Belirtilen göstergelere ve mantığa dayalı olarak tarihsel veriler üzerinde `BollingerRSIStrategy` işlemi simüle eder.

#### 6. Sonuçları Görselleştirme

Geri testin sonunda portföyün performansının görsel bir temsili `cerebro.plot()` kullanılarak görüntülenir. Bu görselleştirme, stratejinin karlılığı ve performansı hakkında bilgi sağlar.

### Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:

- Backtrader
- yfinance
- pandas
- numpy
- matplotlib

Bu kütüphaneleri `pip install` kullanarak veya bir `requirements.txt` dosyasına dahil ederek yükleyebilirsiniz.

### Projeyi Çalıştırma

Bu projeyi çalıştırmak için:

1. Gerekli Python kütüphanelerinin yüklendiğinden emin olun.
2. Sağlanan kodu bir Python betiği veya Jupyter Notebook'a kopyalayın.
3. Betiği veya notebook'u çalıştırarak geri testi başlatın.
4. Sonuçları ve görselleştirmeleri inceleyerek stratejinin performansını değerlendirin.


## English
## Moving Average Cross Strategy for Backtesting

This project demonstrates how to create a simple moving average cross strategy for backtesting using the Backtrader framework and historical stock price data from Yahoo Finance.

### Project Purpose

The purpose of this project is to introduce a basic moving average cross trading strategy. It aims to provide a clear example of how to develop and test a trading strategy using historical stock price data.

### Components

#### 1. Moving Average Cross Strategy

This project includes a custom trading strategy called `MovingAverageCrossStrategy`. The key components of this strategy include:

- **Short and Long Moving Averages**: It uses short and long simple moving averages (SMAs) to make trading decisions. The short SMA typically has a shorter period (e.g., 40 days), while the long SMA has a longer period (e.g., 100 days).

- **Crossover Indicator**: The strategy defines a crossover indicator that triggers buy signals when the short SMA crosses above the long SMA and sell signals when the short SMA crosses below the long SMA.

#### 2. Data Loading

Historical stock price data for the Turkish Airlines (THYAO.IS) from Yahoo Finance is downloaded using the `yfinance` library. The data is then transformed into a format suitable for Backtrader using the `bt.feeds.PandasData` class.

#### 3. Backtest Setup

A Backtrader `Cerebro` instance is set up to perform the backtest. It includes the following configurations:

- The `MovingAverageCrossStrategy` is added as the trading strategy to be tested.

- The historical price data is added to the `Cerebro` instance.

- Initial cash amount is set to 100,000 units for the virtual portfolio.

#### 4. Additional Configurations (Optional)

- A fixed position size (stake) is defined as 1000 units using `bt.sizers.FixedSize`.

- A commission of 0.1% (0.001) is set on each trade to simulate trading costs.

#### 5. Running the Backtest

The backtest is initiated using `cerebro.run()`. It will execute the `MovingAverageCrossStrategy` on the historical data, simulating trades based on the defined crossover logic.

#### 6. Visualizing Results

At the end of the backtest, a visual representation of the portfolio's performance is displayed using `cerebro.plot()`. This visualization provides insight into the strategy's profitability and performance.

### Prerequisites

To run this project, you need to have the following Python libraries installed:

- Backtrader
- yfinance
- pandas
- numpy
- matplotlib

You can install these libraries using `pip install` or by including them in a `requirements.txt` file.

### Running the Project

To run this project:

1. Ensure that the required Python libraries are installed.
2. Copy the provided code into a Python script or Jupyter Notebook.
3. Execute the script or notebook to run the backtest.
4. Analyze the results and visualizations to evaluate the strategy's performance.

Happy backtesting!

## Bollinger Bands and RSI Strategy for Backtesting

This project demonstrates how to create a trading strategy that combines Bollinger Bands and Relative Strength Index (RSI) for backtesting using the Backtrader framework and historical stock price data from Yahoo Finance.

### Project Purpose

The purpose of this project is to introduce a more advanced trading strategy that incorporates Bollinger Bands and RSI indicators. It aims to provide an example of a strategy that uses multiple technical indicators for trading decisions.

### Components

#### 1. Bollinger Bands and RSI Strategy

This project includes a custom trading strategy called `BollingerRSIStrategy`. The key components of this strategy include:

- **Bollinger Bands**: It uses Bollinger Bands to identify potential buy and sell signals based on price volatility.

- **Relative Strength Index (RSI)**: The strategy includes the RSI indicator to identify overbought and oversold conditions.

#### 2. Data Loading

Historical stock price data for the Turkish Airlines (THYAO.IS) from Yahoo Finance is downloaded using the `yfinance` library. The data is then transformed into a format suitable for Backtrader using the `bt.feeds.PandasData` class.

#### 3. Backtest Setup

A Backtrader `Cerebro` instance is set up to perform the backtest. It includes the following configurations:

- The `BollingerRSIStrategy` is added as the trading strategy to be tested.

- The historical price data is added to the `Cerebro` instance.

- Initial cash amount is set to 100,000 units for the virtual portfolio.

#### 4. Additional Configurations (Optional)

- A fixed position size (stake) is defined as 1000 units using `bt.sizers.FixedSize`.

- A commission of 0.1% (0.001) is set on each trade to simulate trading costs.

#### 5. Running the Backtest

The backtest is initiated using `cerebro.run()`. It will execute the `BollingerRSIStrategy` on the historical data, simulating trades based on the defined indicators and logic.

#### 6. Visualizing Results

At the end of the backtest, a visual representation of the portfolio's performance is displayed using `cerebro.plot()`. This visualization provides insight into the strategy's profitability and performance.

### Prerequisites

To run this project, you need to have the following Python libraries installed:

- Backtrader
- yfinance
- pandas
- numpy
- matplotlib

You can install these libraries using `pip install` or by including them in a `requirements.txt` file.

### Running the Project

To run this project:

1. Ensure that the required Python libraries are installed.
2. Copy the provided code into a Python script or Jupyter Notebook.
3. Execute the script or notebook to run the backtest.
4. Analyze the results and visualizations to evaluate the strategy's performance.



