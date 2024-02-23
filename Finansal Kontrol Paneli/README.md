## Türkçe
## Finansal Kontrol Paneli

### Tanım:
Bu proje, seçilen şirketler için hisse senedi fiyatları, geçmiş veriler, finansal haberler ve temel finansal ölçümler dahil olmak üzere borsa verilerini izlemek için bir finansal gösterge tablosu sağlamayı amaçlamaktadır. Kontrol paneli, üst düzey bir Python web çerçevesi olan Django kullanılarak oluşturulmuştur ve gerçek zamanlı hisse senedi verilerini almak için Yahoo Finance API'yi (yfinance) kullanır.

### Özellikler:

**1. Ana Sayfa Yönlendirmesi:** Ana sayfaya eriştikten sonra kullanıcılar, seçilen bir şirkete ait varsayılan kayan yazı sayfasına yönlendirilir (bu durumda THYAO.IS).
**2. Hisse Senedi Verilerinin Alınması:** Seçilen şirket için Yahoo Finance API kullanılarak gerçek zamanlı hisse senedi verileri alınır.
**3. Veri Görselleştirme:** Alınan hisse senedi verileri, AmCharts kitaplığı tarafından desteklenen etkileşimli grafikler kullanılarak görselleştirilir ve geçmiş hisse senedi fiyatları ve hacim eğilimleri hakkında bilgi sağlanır.
**4. Finansal Ölçümler Ekranı:** Toplam gelir, FAVÖK, brüt kar ve işletme giderleri gibi temel finansal ölçümler tablo formatında görüntülenir.
**5. Haber Kaynağı:** Seçilen şirketle ilgili en son finansal haberler, kullanıcıları son gelişmelerden haberdar etmek için kontrol panelinde görüntülenir.
**6. Duyarlı Tasarım:** Kontrol paneli, çeşitli cihazlarda en iyi görüntüleme deneyimini sağlayacak şekilde duyarlı olacak şekilde tasarlanmıştır.

###Kurulum:

1. Depoyu yerel makinenize kopyalayın.
2. pip install -r gereksinimleri.txt dosyasını çalıştırarak gerekli Python paketlerini yükleyin.
3. Python Manage.py runserver'ı kullanarak Django sunucusunu çalıştırın.
4. Kontrol paneline http://localhost:8000 adresindeki web tarayıcınız aracılığıyla erişin.

### Kullanım:

1. Kontrol paneline eriştiklerinde kullanıcılara hisse senedi verileri, finansal ölçümler ve varsayılan olarak seçilen şirketle ilgili haberler sunulur.
2. Kullanıcılar kenar çubuğunda sağlanan bağlantılara tıklayarak farklı şirketler arasında gezinebilir.
3. Etkileşimli grafikler, kullanıcıların geçmiş hisse senedi fiyatlarını ve hacim eğilimlerini analiz etmesine olanak tanır.
4. Finansal ölçümler, seçilen şirketin finansal sağlığına ilişkin bilgiler sağlar.
5. En son haber akışı, kullanıcıları finansal piyasadaki son gelişmelerden haberdar eder.

### Katkı:
Projeye katkılar memnuniyetle karşılanır. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, bir konu açmaktan veya çekme isteği göndermekten çekinmeyin.

### Lisans:
Bu proje MIT Lisansı kapsamında lisanslanmıştır.

### Kredi:

- **Django:** Kontrol panelini oluşturmak için web çerçevesi.
- **Yahoo Finance API (yfinance):** Gerçek zamanlı hisse senedi verilerini almak için kullanılır.
- **AmCharts:** Etkileşimli grafikler oluşturmaya yönelik kitaplık.
- **Bootstrap:** Stillendirme için ön uç çerçevesi.

## English
## Financial Dashboard

### Description:
This project aims to provide a financial dashboard for monitoring stock market data, including stock prices, historical data, financial news, and key financial metrics for selected companies. The dashboard is built using Django, a high-level Python web framework, and utilizes the Yahoo Finance API (yfinance) to fetch real-time stock data.

### Features:

**1. Homepage Redirect:** Upon accessing the homepage, users are redirected to a default ticker page for a selected company (THYAO.IS in this case).
**2. Stock Data Retrieval:** Real-time stock data is retrieved using the Yahoo Finance API for the selected company.
**3. Data Visualization:** The retrieved stock data is visualized using interactive charts powered by AmCharts library, providing insights into historical stock prices and volume trends.
**4. Financial Metrics Display:** Key financial metrics such as total revenue, EBITDA, gross profit, and operating expenses are displayed in a tabular format.
**5. News Feed:** Latest financial news related to the selected company is displayed on the dashboard to keep users informed about recent developments.
**6. Responsive Design:** The dashboard is designed to be responsive, ensuring optimal viewing experience across various devices.

###Installation:

1. Clone the repository to your local machine.
2. Install the required Python packages by running pip install -r requirements.txt.
3. Run the Django server using python manage.py runserver.
4. Access the dashboard through your web browser at http://localhost:8000.

### Usage:

1. Upon accessing the dashboard, users are presented with stock data, financial metrics, and news related to the default selected company.
2. Users can navigate between different companies by clicking on the provided links in the sidebar.
3. Interactive charts allow users to analyze historical stock prices and volume trends.
4. Financial metrics provide insights into the financial health of the selected company.
5. Latest news feed keeps users updated with recent developments in the financial market.

### Contributing:
Contributions to the project are welcome. If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

### License:
This project is licensed under the MIT License.

### Credits:

- **Django:** Web framework for building the dashboard.
- **Yahoo Finance API (yfinance):** Used for retrieving real-time stock data.
- **AmCharts:** Library for creating interactive charts.
- **Bootstrap:** Frontend framework for styling.




