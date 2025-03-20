print(f"""
{"-" * 80}
Kumanda Sınıfı
{"-" * 80}
""")

import random
import time

class Kumanda():
    def __init__(self, tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["Fox"], kanal = True):

        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durum == "Açık":
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if self.tv_durum == "Kapalı":
            print("Televizyon zaten kapalı.")
        else:
            print("Televizyon kapatılıyor...")
            self.tv_durum = "Kapalı"

    def ses_ayar(self):
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Arttır: '>'\nÇıkış: ")
            if cevap == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print(f"Ses: {self.tv_ses}")
            elif cevap == ">":
                if self.tv_ses != 32:
                    self.tv_ses += 1
                    print(f"Ses: {self.tv_ses}")
            else:
                print(f"Ses Güncellendi: {self.tv_ses}")
                break

    def kanal_ekle(self, kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi) -1)

        self.kanal = self.kanal_listesi[rastgele]
        print(f"Şu anki Kanal: {self.kanal}")

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return ("TV Durumu: {}\n TV Ses: {}\n Kanal Listesi: {}\nŞu anki Kanal: {}\n"
                .format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal))

kumanda = Kumanda()

print(f"""

Televizyon Uygulaması

1. TV Aç

2. Tv kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rastgele Kanala Geçme

7. Televizyon Bilgileri

Çıkmak için q'ya basın.

""")

while True:
    islem = input("İşlemi Seçiniz: ")
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
        kanal_isimleri = input("Kanal İsimlerini Virgülle Ayırarak Giriniz: ")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif islem == "5":
        kumanda.__len__()
    elif islem == "6":
        kumanda.rastgele_kanal()
    elif islem == "7":
        print(kumanda)
    else:
        print("Geçersiz İşlem...")



