## Türkçe
## Finansal Zaman Serisi Tahmin Projesi

Bu Python betiği, çeşitli tekrarlayan sinir ağı (RNN) mimarilerini kullanarak finansal zaman serisi verilerini tahmin etmeyi içeren kapsamlı bir projedir. Proje, Borsa İstanbul BIST 30 veri setinde yer alan Aselsan şirketinin 2015-2021 yıllarını kapsayan hisse senedi fiyatlarına odaklanıyor.

### Amaç

Projenin ana hedefleri aşağıdaki gibidir:

1. **Veri Keşfi ve Görselleştirme:** Betik, Aselsan'ın stok verilerinin CSV dosyasından yüklenmesi, ilgili özelliklerin çıkarılması ve Plotly ve Matplotlib kullanılarak görselleştirilmesiyle başlar. Proje, hisse senedinin açılış, en yüksek, en düşük ve kapanış fiyatlarını araştırıyor.

2. **Veri Ön İşleme:** Veri kümesi eğitim ve test kümelerine bölünmüştür. Kapanış fiyatları MinMaxScaler kullanılarak normalleştirilir ve RNN modellerinin eğitimi için diziler oluşturulur.

3. **SimpleRNN Modeli:** Komut dosyası, Keras kitaplığını kullanarak SimpleRNN tabanlı bir model uygular. Modeli optimize etmek için birim sayısı, aktivasyon fonksiyonları ve bırakma oranları gibi hiper parametreler denenir. Öğrenme oranı planlaması uygulanır ve model eğitilir.

4. **LSTM Modeli:** Uzun Kısa Süreli Bellek (LSTM) modeli, SimpleRNN modeline benzer şekilde oluşturulur ve eğitilir. Proje, modelin performansını artırmak için BatchNormalization ve dropout katmanlarını içeriyor.

5. **GRU Modeli:** Başka bir RNN mimarisi olan Geçitli Tekrarlayan Birim (GRU), farklı hiper parametrelerle uygulanır ve eğitilir.

6. **Model Değerlendirmesi:** Proje, eğitilen modellerin doğruluğunu R-kare puanı gibi ölçümler kullanarak değerlendirir. Matplotlib'i kullanarak gerçek ve tahmin edilen hisse senedi fiyatlarını görselleştirir.

7. **Ek Modeller:** Komut dosyası, farklı bir optimizasyon algoritmasına (RMSprop) sahip bir LSTM modeli ve Stokastik Gradyan İniş (SGD) optimizasyonuna sahip bir GRU modeli içerir.

8. **Finansal Zaman Serisi Tahmini:** Projenin son bölümünde, eğitilen modeller kullanılarak ertesi gün hisse senedi fiyatları tahmin edilir ve tahminler Ortalama Mutlak Hata (MAE), Ortalama Mutlak Yüzde Hata (MAPE), Ortalama Mutlak Yüzde Hata (MAPE), ve Medyan Mutlak Yüzde Hatası (MDAPE).

### Kullanım

Bu betiği kullanmak için şu adımları izleyin:

1. Gerekli kütüphaneleri pip install numpy matplotlib kullanarak kurun,plotly pandas scikit-learn tensorflow.

2. Gerekli veri setinin (CSV formatında Aselsan stok verileri) mevcut olduğundan emin olun.

3. Komut dosyasını çalıştırın; veri yükleme ve ön işlemeden model eğitimi ve değerlendirmeye kadar tüm projeyi yürütecektir.

> Not: Özel kurulumunuza bağlı olarak veri kümesi yolunda veya diğer parametrelerde ayarlamalar yapılması gerekebilir.

Modellerin performansını daha da artırmak için farklı hiper parametreler, mimariler ve optimizasyon algoritmalarıyla denemeler yapmaktan çekinmeyin.


## English
## Financial Time Series Prediction Project

This Python script is a comprehensive project that involves predicting financial time series data using various recurrent neural network (RNN) architectures. The project focuses on the stock prices of Aselsan, a company listed on the Borsa İstanbul BIST 30 dataset, covering the years 2015-2021.

### Purpose

The main objectives of the project are as follows:

1. **Data Exploration and Visualization:** The script starts by loading the stock data of Aselsan from a CSV file, extracting relevant features, and visualizing them using Plotly and Matplotlib. The project explores the opening, highest, lowest, and closing prices of the stock.

2. **Data Preprocessing:** The dataset is split into training and testing sets. The closing prices are normalized using MinMaxScaler, and sequences are created for training the RNN models.

3. **SimpleRNN Model:** The script implements a SimpleRNN-based model using the Keras library. Hyperparameters like the number of units, activation functions, and dropout rates are experimented with to optimize the model. Learning rate scheduling is applied, and the model is trained.

4. **LSTM Model:** A Long Short-Term Memory (LSTM) model is built and trained similarly to the SimpleRNN model. The project incorporates BatchNormalization and dropout layers to enhance the model's performance.

5. **GRU Model:** Another RNN architecture, Gated Recurrent Unit (GRU), is implemented and trained with different hyperparameters.

6. **Model Evaluation:** The project evaluates the accuracy of the trained models using metrics such as R-squared score. It visualizes the actual and predicted stock prices using Matplotlib.

7. **Additional Models:** The script includes an LSTM model with a different optimization algorithm (RMSprop) and a GRU model with Stochastic Gradient Descent (SGD) optimization.

8. **Financial Time Series Prediction:** The final part of the project predicts the next-day stock prices using the trained models and evaluates the predictions using metrics like Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE), and Median Absolute Percentage Error (MDAPE).

### Usage

To use this script, follow these steps:

1. Install the required libraries using pip install numpy matplotlib plotly pandas scikit-learn tensorflow.

2. Ensure you have the necessary dataset (Aselsan stock data in CSV format) available.

3. Run the script, and it will execute the entire project, from data loading and preprocessing to model training and evaluation.

> Note: Adjustments to the dataset path or other parameters may be needed based on your specific setup.

Feel free to experiment with different hyperparameters, architectures, and optimization algorithms to further enhance the models' performance.