## Türkçe
## Finansal Rasyo Hesaplama Aracı


Bu proje, finansal oranları hesaplamak ve finansal durumu değerlendirmek amacıyla kullanılan bir araçtır. Projede, likidite, mali yapı, faaliyet, karlılık rasyoları ve hisse değerleme ile ilgili çeşitli oranlar hesaplanabilir. Kullanıcı, finansal tablolarındaki verileri girerek, işletmenin likidite durumunu, mali yapısını, faaliyet etkinliğini, karlılığını ve hisse değerlemesini anlamak için bu aracı kullanabilir.

### Rasyo Hesapları

Projede bulunan rasyo hesapları şunlardır:

1. **Likidite Rasyoları:**
   - **Cari Oran:** Dönen varlıkların kısa vadeli yabancı kaynaklara olan oranını gösterir.
   - **Asit Test Oranı:** Stoklar çıkarıldığında dönen varlıkların kısa vadeli yabancı kaynaklara olan oranını gösterir.

2. **Mali Yapı Rasyoları:**
   - **Kaldıraç Oranı:** Toplam borcun toplam varlıklara olan oranını gösterir.
   - **Duran Varlık/Öz Sermaye Oranı:** Duran varlıkların öz sermayeye olan oranını gösterir.

3. **Faaliyet(Aktivite) Rasyoları:**
   - **Alacak Devir Hızı:** Net satışların kısa vadeli ticari alacaklara olan devir hızını gösterir.
   - **Stok Devir Hızı:** Satışların maliyetinin stoklara olan devir hızını gösterir.

4. **Karlılık(Verimlilik) Rasyoları:**
   - **Net Kar Marjı:** Net karın net satışlara olan oranını gösterir.
   - **Öz Sermaye Karlılığı:** Net karın öz sermayeye olan oranını gösterir.

5. **Hisse Değerleme:**
   - **Hasılat Değişim Katsayısı:** Bir önceki senenin 12 aylık hasılatının bir önceki senenin 9 aylık hasılatına olan oranını gösterir.
   - **Yılsonu Hasılat Tahmini:** Hasılat değişim katsayısı kullanılarak güncel döneme ait hasılat tahminini yapar.
   - **İlgili Dönem Kar Marjı:** Güncel dönemdeki net karın hasılat ile olan oranını gösterir.
   - **Yılsonu Net Kar Tahmini:** Yılsonu hasılat tahmini ve ilgili dönem kar marjı kullanılarak net kar tahmini yapar.
   - **Hisse Başına Net Kar:** Yılsonu net kar tahminini hisse senedi sayısına bölerek hisse başına net karı hesaplar.

6. **Tahmin Sonuçları ile Hisse Değerleme:**
   - **Firma F/K ile Olması Gereken Değer:** Firma fiyat/kazanç oranı kullanılarak hissenin gerçek değeri hesaplanır.
   - **Firma PD/DD ile Olması Gereken Değer:** Firma PD/DD oranı kullanılarak hissenin gerçek değeri hesaplanır.
   - **F/K ve PD/DD ile Hisse Gerçek Değer:** Firma F/K ve PD/DD hesaplamalarının ortalaması alınarak hissenin gerçek değeri belirlenir.

## Nasıl Kullanılır

Projeyi çalıştırmak için, aşağıdaki adımları takip edebilirsiniz:

1. Projenin ana dizininde terminali açın.
2. `python finansal_rasyo_hesaplama.py` komutunu çalıştırın.
3. İlgili rasyo grubunu ve ardından hesaplamak istediğiniz rasyoyu seçin.
4. İlgili verileri girin ve sonuçları görün.


## English
## Financial Ratio Calculator


This project is a tool used to calculate financial ratios and evaluate the financial situation. In the project, various ratios related to liquidity, financial structure, activity, profitability ratios and share valuation can be calculated. By entering data from its financial statements, the user can use this tool to understand the liquidity position, financial structure, operating efficiency, profitability and share valuation of the business.

### Ratio Calculations

The ratio calculations in the project are as follows:

1. **Liquidity Ratios:**
   - **Current Ratio:** It shows the ratio of current assets to short-term foreign resources.
   - **Acid Test Ratio:** It shows the ratio of current assets to short-term foreign resources when stocks are excluded.

2. **Financial Structure Ratios:**
   - **Leverage Ratio:** It shows the ratio of total debt to total assets.
   - **Fixed Asset/Equity Ratio:** Shows the ratio of fixed assets to equity capital.

3. **Activity Ratios:**
   - **Receivables Turnover Rate:** It shows the turnover rate of net sales to short-term trade receivables.
   - **Stock Turnover Rate:** It shows the turnover rate of the cost of sales to stocks.

4. **Profitability (Efficiency) Ratios:**
   - **Net Profit Margin:** It shows the ratio of net profit to net sales.
   - **Return on Equity:** It shows the ratio of net profit to equity capital.

5. **Share Valuation:**
   - **Revenue Variation Coefficient:** It shows the ratio of the previous year's 12-month revenue to the previous year's 9-month revenue.
   - **Year-End Revenue Forecast:** Makes the revenue forecast for the current period using the revenue variation coefficient.
   - **Relevant Period Profit Margin:** Shows the ratio of net profit to revenue in the current period.
   - **Year-End Net Profit Forecast:** Estimates the net profit using the year-end revenue estimate and the relevant period profit margin.
   - **Net Profit Per Share:** Calculates net profit per share by dividing the year-end net profit estimate by the number of shares.

6. **Stock Valuation with Estimation Results:**
   - **Required Value with Company P/E:** The real value of the share is calculated using the company price/earnings ratio.
   - **Required Value with Company PV/DD:** The real value of the share is calculated using the company PV/DD ratio.
   - **Real Value of the Stock with P/E and PV/DD:** The real value of the share is determined by taking the average of the company's P/E and PV/DD calculations.

## How to use

To run the project, you can follow the steps below:

1. Open terminal in the project's root directory.
2. Run the `python financial_rasyo_hesaplama.py` command.
3. Select the relevant ratio group and then select the ratio you want to calculate.
4. Enter relevant data and see the results.