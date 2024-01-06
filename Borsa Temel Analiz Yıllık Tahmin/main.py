class FinansalRasyolar:
    def __init__(self):
        pass

    @staticmethod
    def likidite_rasyosu():
        try:
            donen_varliklar = float(input("\n Dönen varlıklar değerini giriniz: "))
            kisa_donem_yabanci_kaynaklar = float(input("\n Kısa dönem yabancı kaynaklar değerini giriniz: "))
            stoklar = float(input("\n Stokların değerini giriniz: "))
            
            cari_oran = donen_varliklar / kisa_donem_yabanci_kaynaklar
            asit_testi_orani = (donen_varliklar - stoklar) / kisa_donem_yabanci_kaynaklar
            
            print("\nGirilen değerlere göre Cari Oran: ", cari_oran)
            print("\nGirilen değerlere göre Asit Testi Oran: ", asit_testi_orani)

        except ValueError:
            print("Geçersiz bir değer girdiniz. Lütfen sayısal bir değer girin.")

    @staticmethod
    def mali_yapi_rasyosu():
        try:
            toplam_borc = float(input("\n Toplam borç değerini giriniz: "))
            toplam_varlik = float(input("\n Toplam varlık değerini giriniz: "))
            duran_varliklar = float(input("\n Duran varlıklar değerini giriniz: "))
            oz_sermaye = float(input("\n Öz sermaye değerini giriniz: "))
            
            kaldırac_orani = toplam_borc / toplam_varlik
            duran_varlik_sermaye_orani = duran_varliklar / oz_sermaye
            
            print("\nGirilen değerlere göre Kaldıraç Oranı: ", kaldırac_orani)
            print("\nGirilen değerlere göre Duran Varlıkların Öz Sermayeye Oranı: ", duran_varlik_sermaye_orani)

        except ValueError:
            print("Geçersiz bir değer girdiniz. Lütfen sayısal bir değer girin.")

    @staticmethod
    def faaliyet_rasyosu():
        try:
            net_satislar = float(input("\n Net satışların değerini giriniz: "))
            kisa_vadeli_tic_alacaklar = float(input("\n Kısa vadeli ticari alacakların değerini giriniz: "))
            satislarin_maaliyeti = float(input("\n Satışların maaliyeti değerini giriniz: "))
            donem_basi_stok = float(input("\n Dönem başı stok değerini giriniz: "))
            donem_sonu_stok = float(input("\n Dönem sonu stok değerini giriniz: "))
            
            alacak_devir_hizi = net_satislar / kisa_vadeli_tic_alacaklar
            alacak_tahsil_suresi = 365 / alacak_devir_hizi
            stok_devir_hizi = satislarin_maaliyeti / ((donem_basi_stok + donem_sonu_stok) / 2)
            stok_donusum_suresi = 365 / stok_devir_hizi
            
            print("\nGirilen değerlere göre Alacak Devir Hızı: ", alacak_devir_hizi, " ve Alacak Tahsil Süresi: ", alacak_tahsil_suresi)
            print("\nGirilen değerlere göre Stok Devir Hızı: ", stok_devir_hizi, " ve Stok Dönüşüm Süresi: ", stok_donusum_suresi)

        except ValueError:
            print("Geçersiz bir değer girdiniz. Lütfen sayısal bir değer girin.")

    @staticmethod
    def karlilik_rasyosu():
        try:
            net_kar = float(input("\n Net kar değerini giriniz: "))
            net_satislar = float(input("\n Net satışların değerini giriniz: "))
            oz_sermaye = float(input("\n Öz sermaye değerini giriniz: "))
            
            net_kar_marji = net_kar / net_satislar
            oz_sermaye_karliligi = net_kar / oz_sermaye
            
            print("\nGirilen değerlere göre Net Kar Marjı: ", net_kar_marji)
            print("\nGirilen değerlere göre Öz Sermaye Karlılığı: ", oz_sermaye_karliligi)

        except ValueError:
            print("Geçersiz bir değer girdiniz. Lütfen sayısal bir değer girin.")

    @staticmethod
    def tahminleme_rasyosu():
        try:
            hasilat_guncel_donem = float(input("\n Açıklanan ve güncel en son dönemin hasılat değerini giriniz: "))
            hasilat_gecen_donem = float(input("\n Açıklanandan bir önceki hasılat değerini giriniz: "))
            guncel_donem_hasilat = float(input("\n Bu senenin hasılatını giriniz: "))
            guncel_donem_net_kar = float(input("\n Bu senenin NET DÖNEM KARI değerini giriniz: "))
            hisse_senedi_sayisi = float(input("\n Hisse senedi sayısını giriniz: "))
            yuzde = float(input("\n Güvenli bir tahmin yapabilmek için, çıkan sonucu yüzde kaç aşağı yuvarlamak istiyorsunuz? Örneğin %15 için sadece 15 yazınıp enter'a basınız. En az %10 önerilir."))
            
            hasilat_degisim_katsayisi = hasilat_guncel_donem / hasilat_gecen_donem
            yilsonu_hasilat_tahmini = (hasilat_degisim_katsayisi * hasilat_guncel_donem) - ((hasilat_degisim_katsayisi * hasilat_guncel_donem) * (yuzde / 100))
            net_kar_marji = guncel_donem_net_kar / hasilat_guncel_donem
            yilsonu_net_kar_tahmin = yilsonu_hasilat_tahmini * net_kar_marji
            hisse_basina_net_kar = yilsonu_net_kar_tahmin / hisse_senedi_sayisi
            
            print("\nGirilen değerlere göre Hasılat Değişim Katsayısı: ", hasilat_degisim_katsayisi)
            print("\nGirilen değerlere göre ve %", yuzde, "güven ile Yılsonu Hasılat Tahmini: ", yilsonu_hasilat_tahmini)
            print("\nGirilen değerlere göre Net Kar Marjı: ", net_kar_marji)
            print("\nGirilen değerlere göre Yılsonu Net Kar Tahmini: ", yilsonu_net_kar_tahmin)
            print("\nGirilen değerlere göre Hisse Başına Net Kar: ", hisse_basina_net_kar)

        except ValueError:
            print("Geçersiz bir değer girdiniz. Lütfen sayısal bir değer girin.")

    @staticmethod
    def degerleme_rasyosu():
        try:
            hisse_borsa_fiyat = float(input("\n Hisse senedinin borsa fiyatını giriniz: "))
            hisse_basina_net_kar = float(input("\n Tahmin kısmında hesapladığınız HİSSE BAŞINA KAR değerini giriniz: "))
            oz_kaynaklar = float(input("\n Öz Kaynaklar değerini giriniz: "))
            yilsonu_net_kar_tahmin = float(input("\n Tahmin kısmında hesapladığınız YILSONU NET KAR TAHMİNİ değerini giriniz: "))
            net_kar = float(input("\n NET DÖNEM KARI değerini giriniz: "))
            hisse_senedi_sayisi = float(input("\n Hisse senedi sayısını giriniz: "))
            
            firma_fk = hisse_borsa_fiyat / hisse_basina_net_kar
            ogf_fk = (10 / firma_fk) * hisse_borsa_fiyat
            yilsonu_tahmini_oz_kaynak = oz_kaynaklar + (yilsonu_net_kar_tahmin - net_kar)
            hisse_basina_defter_degeri = yilsonu_tahmini_oz_kaynak / hisse_senedi_sayisi
            firma_pddd = hisse_borsa_fiyat / hisse_basina_defter_degeri
            ogf_pddd = (2 / firma_pddd) * hisse_borsa_fiyat
            gercek_deger = (ogf_fk + ogf_pddd) / 2
            
            print("\nGirilen değerlere göre Firma F/K: ", firma_fk, "ve Firma F/K 'ya göre olması gereken fiyat: ", ogf_fk)
            print("\nGirilen değerlere göre Yılsonu Tahmini Öz Kaynak: ", yilsonu_tahmini_oz_kaynak, "\n Hisse Başına Defter Değeri : ", hisse_basina_defter_degeri)
            print("\nGirilen değerlere göre Firma PD/DD: ", firma_pddd, "ve Firma PD/DD 'ye göre olması gereken fiyat: ", ogf_pddd)
            print("\nF/K ve PD/DD hesaplamalarına göre HİSSENİN GERÇEK(NİHAİ DEĞERİ): ", gercek_deger)

        except ValueError:
            print("Geçersiz bir değer girdiniz. Lütfen sayısal bir değer girin.")

def main():
    finansal_rasyolar = FinansalRasyolar()

    while True:
        print("\n\n*** RASYOLAR (ORANLAR) ***")
        print("\n1 - Likidite Rasyoları\n2 - Mali Yapı Rasyoları\n3 - Faaliyet Rasyoları\n4 - Karlılık Rasyoları\n5 - Tahminleme Rasyoları\n6 - Değerleme Rasyoları\n0 - Çıkış")

        try:
            secenek = int(input("\nHesaplamak istediğiniz veri grubunu seçiniz: "))
            if secenek == 0:
                break
            elif secenek == 1:
                finansal_rasyolar.likidite_rasyosu()
            elif secenek == 2:
                finansal_rasyolar.mali_yapi_rasyosu()
            elif secenek == 3:
                finansal_rasyolar.faaliyet_rasyosu()
            elif secenek == 4:
                finansal_rasyolar.karlilik_rasyosu()
            elif secenek == 5:
                finansal_rasyolar.tahminleme_rasyosu()
            elif secenek == 6:
                finansal_rasyolar.degerleme_rasyosu()
            else:
                print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")

        except ValueError:
            print("Geçersiz bir değer girdiniz. Lütfen sayısal bir değer girin.")

if __name__ == "__main__":
    main()
