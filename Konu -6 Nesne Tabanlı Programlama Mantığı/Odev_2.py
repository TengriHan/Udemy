print(f"""
{"-" * 80}
Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar 
ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.

Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.
{"-" * 80}
""")

class Bilgisayar:
    def __init__(self, pc_durum = "Kapalı", sayfa = None, pc_ses = 0, sayfalar = None, mod = "Normal Mod"):
        if sayfalar is None:
            sayfalar = ["Ana Sayfa"]

        self.pc_durum = pc_durum
        self.pc_ses = pc_ses
        self.sayfalar = sayfalar
        self.sayfa =  sayfa or sayfalar[0]
        self.mod = mod

    def pc_ac(self):
        if self.pc_durum == "Açık":
            print("Bilgisayar Zaten Açık.")
        else:
            print("Bilgisayar açılıyor...")
            self.pc_durum = "Açık"
            print("Bilgisayar Açıldı.")

    def pc_kapat(self):
        if self.pc_durum == "Kapalı":
            print("Bilgisayar Zaten Kapalı.")
        else:
            print("Bilgisayar kapatılıyor...")
            self.pc_durum = "Kapalı"
            print("Bilgisayar kapandı.")

    def ses_ayar(self):
        if self.pc_durum == "Kapalı":
            print("Bilgisayar kapalıyken ses ayarı yapılamaz...")
            return
        else:
            while True:
                deger = input("Sesi açmak için '+' Kısmak için '-' Çıkmak için 'q'ya basınız: ")

                if deger == "q":
                    print("Ses ayarlarından çıkılıyor.")
                    break

                elif deger == "+":
                    if self.pc_ses < 100:
                        print("Ses arttırılıyor.")
                        self.pc_ses += 1
                        print(f"Güncel Ses Seviyesi: {self.pc_ses}")
                    else:
                        print("Ses zaten Maksimumda")

                elif deger == "-":
                    if self.pc_ses > 0:
                        print("Ses azaltılıyor.")
                        self.pc_ses -= 1
                        print(f"Güncel Ses Seviyesi: {self.pc_ses}")
                    else:
                        print("Ses Seviyesi zaten 0!!")

                else:
                    print("Geçersiz İşlem")

    def sayfa_ekle(self):
        while True:
            yeni_sayfa_ekle = input("Eklemek istediğiniz sayfayı girin (Çıkmak için 'q'ya basın): ")
            if not yeni_sayfa_ekle.strip():  # Eğer kullanıcı sadece boşluk girerse engelle
                print("Geçersiz giriş, lütfen bir sayfa adı girin.")
                continue
            if yeni_sayfa_ekle == "q":
                print("Sayfa eklemeden çıkılıyor....")
                break
            if yeni_sayfa_ekle in self.sayfalar:
                print("Bu sayfa zaten mevcut..")
            else:
                self.sayfalar.append(yeni_sayfa_ekle)
                print(f"Sayfa eklendi.")
                print(f"Güncel Sayfalar: {', '.join(self.sayfalar)}")

    def mod_secimi(self):
        deger = input("Normal mod için '0', Gece Modu için '1'e basınız: ").strip()

        if deger == "0":
            if self.mod == "Normal Mod":
                print("Zaten Normal Moddasınız...")
            else:
                print("Normal moda geçiş yapılıyor...")
                self.mod = "Normal Mod"

        elif deger == "1":
            if self.mod == "Gece Modu":
                print("Zaten Gece Modundasınız...")
            else:
                print("Gece Moduna geçiş yapılıyor...")
                self.mod = "Gece Modu"

        else:
            print("Geçersiz giriş! Lütfen sadece '0' veya '1' girin.")


    def sayfa_degistir(self):
        if not self.sayfalar:
            print("Kayıtlı Sayfa Yok!")
            return
        print(f"Mevcut Sayfalar: {', '.join(self.sayfalar)}")
        yeni_sayfa = input("Geçmek istediğiniz sayfanın adını girin: ")
        if yeni_sayfa in self.sayfalar:
            self.sayfa = yeni_sayfa
            print(f"Şu anki sayfa: {self.sayfa}")
        else:
            print("Böyle bir sayfa bulunamadı")

    def __len__(self):
        return  len(self.sayfalar)

    def __str__(self):
        return (f"{"*" * 80}"
                f"\nBilgisayar durumu: {self.pc_durum}"
                f"\nAçık Sayfa: {self.sayfa}"
                f"\nBilgisayar Ses Seviyesi: {self.pc_ses},"
                f"\nSayfalar: {self.sayfalar} "    
                f"\n{"*" * 80}")


print(f"""
{"-" * 80}
Bilgisayar Uygulaması - Seçenekler:

1 - Bilgisayarı Aç
2 - Bilgisayarı Kapat
3 - Ses Ayarlarını Değiştir
4 - Yeni Sayfa Ekle
5 - Sayfa Değiştir
6 - Mod Seçimi (Normal / Gece Modu)
7 - Bilgisayar Bilgilerini Göster
8 - Sayfa Sayısını Göster

Çıkış için 'q' tuşuna basın.
{"-" * 80}
""")

bilgisayar = Bilgisayar()

while True:
    islem = input("İşlem Seçiniz: ").strip()

    if islem == "q":
        print("Programdan çıkılıyor...")
        break
    elif islem == "1":
        bilgisayar.pc_ac()
    elif islem == "2":
        bilgisayar.pc_kapat()
    elif islem == "3":
        bilgisayar.ses_ayar()
    elif islem == "4":
        bilgisayar.sayfa_ekle()
    elif islem == "5":
        bilgisayar.sayfa_degistir()
    elif islem == "6":
        bilgisayar.mod_secimi()
    elif islem == "7":
        print(bilgisayar)
    elif islem == "8":
        print(f"Toplam Sayfa Sayısı: {len(bilgisayar)}")
    else:
        print("Geçersiz işlem! Lütfen belirtilen seçeneklerden birini girin.")
