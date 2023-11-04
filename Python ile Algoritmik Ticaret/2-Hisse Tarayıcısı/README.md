## Türkçe
## Hisse Senedi Analizi ve Filtreleme

Bu proje, hisse senedi verilerini almak, analiz etmek ve filtrelemek için kullanılan Python tabanlı bir araçtır. Aşağıdaki işlevleri kapsar:

### S&P 500 Hisse Senetlerini Almak

Kod, Wikipedia'dan veri kazıyarak S&P 500 şirketlerinin hisse senedi sembollerini alır.

### Tarihsel Hisse Senedi Verilerini Alma

Proje, belirli bir tarih aralığında (başlangıçtan bitişe) Yahoo Finans'ın API'sini kullanarak tarihsel hisse senedi fiyat verilerini alır.

### Veri Temizleme ve Biçimlendirme

Eksik verileri kaldırmak için veri temizleme yapılır. Temizlenen veriler daha fazla analiz için kullanılır.

### Teknik Göstergelerin Hesaplanması

Kod, Exponential Moving Averages (EMA) ve Stokastik Osilatörler (STOCH) gibi teknik göstergeleri hesaplar ve bunları hisse senedi verilerine ekler.

### EMA Sıçrama Stratejisi

"EMA Sıçrama" stratejisi, EMA geçişleri, stokastik osilatör değerleri ve 52 haftalık düşük ve yüksek fiyatlarla ilgili belirli koşulları değerlendirerek uygulanır. Bu koşulları karşılayan hisseler daha fazla analiz için seçilir.

### Hisse Senedi Analizi ve Filtreleme

Kod, RSI değerleri, MACD ve P/E oranları gibi kriterlere göre seçilen hisseleri daha fazla analiz eder. Kriterleri karşılayan hisseler ekrana yazdırılır ve uygun hisselerin listesine çıkarılır.

### Çıktı ve Gösterim

Uygun hisseler, MACD, RSI ve P/E oranı bilgileri dahil olmak üzere ekranda görüntülenir. Proje, belirli teknik ve temel kriterleri karşılayan hisseler hakkında bilgi sağlar.

### Kullanılan Kütüphaneler ve Bağımlılıklar

Projede aşağıdaki kütüphaneler kullanılır:

- `requests`: HTTP istekleri yapmak için kullanılır.
- `beautifulsoup4`: Web kazıma için kullanılır.
- `pandas`: Veri analizi ve işlemek için kullanılır.
- `datetime`: Tarih ve saat verilerini işlemek için kullanılır.
- `yfinance`: Yahoo Finans API'sinden finansal veri almak için kullanılır.
- `os`: Dosya ve dizin işlemleri için kullanılır.
- `time`: Zaman gecikmelerini tanıtmak için kullanılır.

README dosyası, projenin yeteneklerine, nasıl kullanılacağına ve bağımlılıklarına dair net bir genel bakış sunar. Bu metni kopyalayarak ve yapıştırarak projenizin README dosyasını oluşturabilirsiniz.



## English
## Stock Analysis and Screening

This project is a Python-based tool for fetching, analyzing, and screening stock data. It encompasses the following functionalities:

### Fetching S&P 500 Tickers

The code retrieves a list of S&P 500 company tickers by scraping data from Wikipedia.

### Historical Stock Data Retrieval

The project retrieves historical stock price data using Yahoo Finance's API for a specific date range (from "start" to "end").

### Data Cleaning and Formatting

Data cleaning is performed to remove missing values. The cleaned data is then used for further analysis.

### Technical Indicators Calculation

The code calculates technical indicators, such as Exponential Moving Averages (EMAs) and Stochastic Oscillators (STOCH), and adds them to the stock data.

### Bounce EMA Strategy

The "Bounce EMA" strategy is implemented by evaluating specific conditions, including EMA crossovers, stochastic oscillator values, and price relative to the 52-week low and high. Stocks that meet these conditions are selected for further analysis.

### Stock Analysis and Screening

The code further analyzes the selected stocks using criteria such as RSI values, MACD, and P/E ratios. Stocks that meet the criteria are screened and output to the list of eligible stocks.

### Output and Display

The eligible stocks are displayed, including their MACD, RSI, and P/E ratio information. The project provides insights into stocks that meet specific technical and fundamental criteria.

### Libraries and Dependencies

The project relies on the following libraries:

- `requests`: Used for making HTTP requests.
- `beautifulsoup4`: Used for web scraping.
- `pandas`: Used for data analysis and manipulation.
- `datetime`: Used for handling date and time data.
- `yfinance`: Used for fetching financial data from Yahoo Finance API.
- `os`: Used for file and directory operations.
- `time`: Used for introducing time delays.


The README file provides a clear overview of the project's capabilities, how to use it, and the libraries it depends on. Feel free to copy and paste this text into a README file for your project.
