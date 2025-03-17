print(f"""
{"-" * 80}
Nesne Tabanlı Programlama - Metodlar
{"-" * 80}
""")

class Yazilimci():
    def __init__(self, isim, soyisim, numara, maas, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller

    def bilgileri_goster(self):
        print(f"""
        Yazılımcı Objesinin Özellikleri
        isim : {self.isim}
        Soyisim : {self.soyisim}
        Numara : {self.numara}
        Maaş : {self.maas}
        Bildiği Diller : {self.diller} 
        """)

    def zam_yap(self, zam_miktari):
        print("Zam Yapılıyor...")
        self.maas += zam_miktari

    def dil_ekle(self, yeni_dil):
        print("Dil ekleniyor...")
        self.diller.append(yeni_dil)


yazilimci_1 = Yazilimci("Furkan", "Bayraktar",
                      "12345", 30000,
                      ["Python", "Java", "Html", "Css"])
print(yazilimci_1.bilgileri_goster())

yazilimci_1.dil_ekle("GoLang")

yazilimci_1.bilgileri_goster()

yazilimci_1.zam_yap(500)
yazilimci_1.bilgileri_goster()
