import time

print(f"""
{"-" * 80}
Kodlama egzersinizinde yazılan kumanda sınıfına ek olarak metodlar ve özellikler ekleyin
{"-" * 80}
""")

class Kumanda:
    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi=None, kanal=None):
        if kanal_listesi is None:
            kanal_listesi = ["FOX"]  # Varsayılan kanal listesi
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal or kanal_listesi[0]  # Varsayılan kanal ilk kanaldır

    def tv_ac(self):
        if self.tv_durum == "Açık":
            print("Televizyon zaten açık.")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"
            print("Televizyon açıldı.")



    def tv_kapat(self):
        if self.tv_durum == "Kapalı":
            print("Televizyon zaten kapalı.")
        else:
            print("Televizyon kapatalıyor...")
            self.tv_durum = "Kapalı"
            print("Televizyon kapandı.")


    def ses_ayar(self):
        while True:
            cevap = input("Sesi Açmak için '+' tuşuna basın Kısmak için '-': ")
            if cevap == "+":
                if self.tv_ses != 32:
                    self.tv_ses += 1
                    print(f"Güncel Ses Seviyesi: {self.tv_ses}")
            elif cevap == "-":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print(f"Güncel Ses Seviyesi: {self.tv_ses}")
            elif cevap == "q":
                print(f"Ses ayalarından çıkılıyor. \nGüncel Ses Seviyesi: {self.tv_ses}")
                break
            else:
                print("Geçersiz İşlem.")

    def kanal_degistir(self):
        try:
            deger = int(input(f"Kanal Seçin (0-{len(self.kanal_listesi) - 1}): "))
            if 0 <= deger < len(self.kanal_listesi):
                self.kanal = self.kanal_listesi[deger]
                print(f"Şu anki Kanal: {self.kanal}")
            else:
                print("Hatalı kanal numarası!")
        except ValueError:
            print("Lütfen sadece rakam giriniz!")


    def kanal_ekle(self, kanal_ismi):
        self.kanal_listesi.append(kanal_ismi)
        time.sleep(0.5)
        print("Kanal Eklendi")


    def __len__(self):
        return  len(self.kanal_listesi)


    def __str__(self):
        return (f"TV Durum: {self.tv_durum}\nGüncel Ses Seviyesi: {self.tv_ses}"
                f"\nKanal Listesi: {self.kanal_listesi}\nAçık Olan Kanal: {self.kanal}")


kumanda = Kumanda()

print(f"""

Televizyon Uygulaması

1. TV Aç

2. Tv kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Kanal Değiştirme

7. Televizyon Bilgileri

Çıkmak için q'ya basın.

""")

while True:
    islem = input("İşlem Seçiniz: ")

    if islem == "q":
        print("Program Sonlandırılıyor...")
        break

    elif islem == "1":
        kumanda.tv_ac()

    elif islem == "2":
        kumanda.tv_kapat()

    elif islem == "3":
        kumanda.ses_ayar()

    elif islem == "4":
        yeni_kanallar = input("Lütfen ',' ile ayırarak kanalları giriniz: ")
        kanal_listesi = yeni_kanallar.split(",")
        for ekle in kanal_listesi:
            kumanda.kanal_ekle(ekle)

    elif islem == "5":
        print(kumanda.__len__())
    elif islem == "6":
        kumanda.kanal_degistir()

    elif islem == "7":
        print(kumanda)

    else:
        print("Geçersiz İşlem...")
