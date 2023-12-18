
## Türkçe
## Hisse Senedi Fiyat Tahmini ve RSI Entegrasyonu
Bu Python kodu, EREGL.IS hissesi için geçmiş fiyat verilerini kullanarak bir fiyat tahmin modeli oluşturur. Ayrıca Göreceli Güç Endeksi'ni (RSI) başka bir hisse senedinden (GOOGL) gelen verilerle hesaplayarak bu özelliği modellemeye dahil eder.

### Kuralların Amacı
Sağlanan Python kodu aşağıdaki görevleri gerçekleştirir:

**1. Veri Alma:**
- EREGL.IS için geçmiş hisse senedi fiyat verilerini belirli bir tarih aralığında ("2020-01-01" ile "2023-02-28" arası) günlük aralıklarla Yahoo Finance'den indirmek için yfinance kütüphanesini kullanır.

**2. Veri goruntuleme:**
- Plotly kütüphanesini kullanarak zaman içindeki kapanış fiyatlarını ve hacim eğilimlerini görselleştirir.

**3. Özellik Mühendisliği:**
- Bir makine öğrenimi modeli için özellikler ve hedefler oluşturur. Özellikler geçmiş kapanış fiyatlarından oluşturulur ve hedef bir sonraki adımın kapanış fiyatıdır.

**4. Veri Ön İşleme:**
- Özellikleri ve hedefleri belirli bir aralığa getirmek için scikit-learn'deki MinMaxScaler'ı kullanarak ölçeklendirir.

**5. Model Eğitimi:**
- TensorFlow ve Keras kütüphanelerini kullanarak bir sinir ağı modeli tanımlar. Model, bırakma katmanlarına ve yoğun katmanlara sahip Çift Yönlü bir LSTM (Uzun Kısa Süreli Bellek) ağıdır.
- Kod, hazırlanan özellikleri ve hedefleri kullanarak modeli eğitir, bir test setinde doğrular ve en iyi ağırlıkları kaydeder.

**6. Model Değerlendirmesi ve Tahmini:**
- En iyi ağırlıkları yükler ve test seti üzerinde tahminlerde bulunmak için eğitilmiş modeli kullanır.
- Daha sonra tahminler, orijinal ölçeğe geri dönmek için ters dönüştürülür.

**7. RSI Hesaplaması ve Entegrasyonu:**
- Başka bir hisse senedinin (GOOGL) geçmiş hisse senedi fiyatlarını kullanarak Göreceli Güç Endeksi'ni (RSI) hesaplar ve bunu orijinal veri seti ile entegre eder.

**8. İkinci Model Eğitimi:**
- Artık ek bir özellik olarak RSI içeren güncellenmiş veri kümesini kullanarak özellik mühendisliği, ön işleme ve model eğitimi sürecini tekrarlar.

**9. Model Değerlendirmesi ve Son Görselleştirme:**
- Test seti üzerindeki ikinci modeli değerlendirir, tahminlerde bulunur ve gerçek ve öngörülen hisse senedi fiyatlarının görselleştirilmesini sağlar.

### Kullanım
**1. Veri Alma:**
- Gerekli kitaplıkların kurulu olduğundan emin olun: yfinance, tensorflow, numpy, pandas veplotly.
- Gerekirse veri alma bölümündeki hisse senedi sembolünü ve tarih aralığını değiştirin.

**2. Model Eğitimi:**
- Sağlanan koddaki sinir ağının mimarisini tanımlayın.
- İhtiyaçlarınıza göre öğrenme oranı, tekrarlanan bırakma ve diğerleri gibi hiperparametreleri ayarlayın.
- Modeli eğitmek için kodu çalıştırın.

**3. RSI Entegrasyonu (İsteğe bağlı):**
- RSI'yi bir özellik olarak eklemek istiyorsanız kodu buna göre değiştirin. RSI periyodunu ve hisse senedi sembolünü değiştirebilirsiniz.

**4. Görselleştirme:**
- Çizim kodunu tercihlerinize göre güncelleyin.
- Gerçek ve tahmin edilen hisse senedi fiyatlarını gözlemlemek için görselleştirme kodunu çalıştırın.

### Not
- Gerekli Python kitaplıklarının kurulu olduğundan emin olun; özel kullanım durumunuza veya tercihlerinize göre kodu ayarlamanız gerekebilir.
- Bu README, üst düzey bir genel bakış sağlar ve kullanımdan önce kod bileşenlerinin ayrıntılı olarak anlaşılması önerilir.

## English
## Stock Price Forecast and RSI Integration
This Python code creates a price prediction model using historical price data for EREGL.IS stock. It also incorporates this feature into modeling by calculating the Relative Strength Index (RSI) with data from another stock (GOOGL).

### Purpose of the Code
The provided Python code performs the following tasks:

**1. Data Retrieval:**
- It uses the yfinance library to download historical stock price data for EREGL.IS from Yahoo Finance within a specified date range (from "2020-01-01" to "2023-02-28") with a daily interval.

**2. Data Visualization:**
- It visualizes the closing prices and volume trends over time using the Plotly library.

**3. Feature Engineering:**
- It creates features and targets for a machine learning model. The features are constructed from historical closing prices, and the target is the closing price of the next time step.

**4. Data Preprocessing:**
- It scales the features and targets using MinMaxScaler from scikit-learn to bring them within a specific range.

**5. Model Training:**
- It defines a neural network model using the TensorFlow and Keras libraries. The model is a Bidirectional LSTM (Long Short-Term Memory) network with dropout layers and dense layers.
- The code trains the model using the prepared features and targets, validates it on a test set, and saves the best weights.

**6. Model Evaluation and Prediction:**
- It loads the best weights and uses the trained model to make predictions on the test set.
- The predictions are then inverse transformed to get them back to the original scale.

**7. RSI Calculation and Integration:**
- It calculates the Relative Strength Index (RSI) using the historical stock prices of another ticker (GOOGL) and integrates it with the original dataset.

**8. Second Model Training:**
- It repeats the process of feature engineering, preprocessing, and model training using the updated dataset that now includes RSI as an additional feature.

**9. Model Evaluation and Final Visualization:**
- It evaluates the second model on the test set, makes predictions, and visualizes the actual vs. predicted stock prices.

### Usage
**1. Data Retrieval:**
- Ensure that you have the required libraries installed: yfinance, tensorflow, numpy, pandas, and plotly.
- Modify the ticker symbol and date range in the data retrieval section if needed.

**2. Model Training:**
- Define the architecture of the neural network in the provided code.
- Adjust hyperparameters like the learning rate, recurrent dropout, and others based on your requirements.
- Run the code to train the model.

**3. RSI Integration (Optional):**
- If you want to include RSI as a feature, modify the code accordingly. You can change the RSI period and the ticker symbol.

**4. Visualization:**
- Update the plotting code based on your preferences.
- Run the visualization code to observe the actual vs. predicted stock prices.

### Note
- Make sure to have the required Python libraries installed, and you may need to adjust the code based on your specific use case or preferences.
- This README provides a high-level overview, and it's recommended to understand the code components in detail before usage.