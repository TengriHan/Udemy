print(f"""
{"-" * 80}
Nesne Tabanlı Programlama - Sınıflar
{"-" * 80}
""")

print("Sınıflar")

class Araba():
    model = "Renault Megane"
    renk = "Gümüş"
    beygir_gucu = 110
    silindir = 4

araba_1 = Araba.renk

araba_2 = Araba.model

print(araba_1)
print(araba_2)

print("__init__ metodu yapıcı(constructor) olarak tanımlanmaktadır.")
print("self objeyi gösteren anahtar kelimedir.")
print(f"{"-" * 80}")

class Araba_Detay():

    def __init__(self, model = "Bilgi Yok", renk = "Bilgi Yok",
                 beygir_gucu = "Bilgi Yok", silindir = "Bilgi Yok"):
        print("init fonksiyonu çağırıldı.")
        self.model = model
        self.renk = renk
        self.beygir_gucu = beygir_gucu
        self.silindir = silindir

araba_3 = Araba_Detay("Renault Megane", "Gümüş", "110", "4")
araba_4 = Araba_Detay("Peugeot 106", "Kırmızı", "95", "4")
araba_5 = Araba_Detay(beygir_gucu="120")

print(araba_3.model)
print(araba_4.model)
print(araba_5.model)
print(araba_5.beygir_gucu)

