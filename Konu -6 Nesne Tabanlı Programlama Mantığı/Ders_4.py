print(f"""
{"-" * 80}
Nesne Tabanlı Programlama - Kalıtım (Inheritance)
Kalıtım bir sınıfın başka bir sınıftan özelliklerini (attribute) ve motedlarını miras alır.

{"-" * 80}
""")

class Calisan():
    def __init__(self, isim, maas, departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Çalışan Bilgileri Gösteriliyor...")
        print(f"Çalışan İsim: {self.isim} \nMaaşı: {self.maas} \nDepartmanı: {self.departman}")

    def departman_degistirme(self, yeni_departman):
        print("Departman Değiştirme İşlemi")
        self.departman = yeni_departman


class Yonetici(Calisan):
    def zam_yap(self, zam_miktarı):
        self.maas += zam_miktarı

yonetici = Yonetici("Furkan", 30000, "Bilişim")

print(yonetici.bilgileri_goster())

print(f"{"-" * 80}")

yonetici.departman_degistirme("Yazılım")
print(yonetici.bilgileri_goster())

print(f"{"-" * 80}")

yonetici_2 = Yonetici("Rabia", 25000, "İnsan Kaynakları")
print(yonetici_2.bilgileri_goster())

print(f"{"-" * 80}")

yonetici_2.zam_yap(500)
print(yonetici_2.bilgileri_goster())

print(f"{"-" * 80}")

print("Overriding (iptal etme)")
"""
Eğer miras aldığımız metodları aynı isimle kendi sınıfımızda tekrar tanımlarsak artık metodu çağırdığımız zaman miras
aldığımız değil kendi metodumuz çalışacaktır.

Örneğin artık çalışan sınıfının init metodunu kullanmak yerine Yönetici sınıfnda init metodunu override edebiliriz.
Böylelikle Yönetici sınıfına ekstra özelliker (attribute) ekleyebiliriz.
"""

class Calisan_2():
    def __init__(self, isim, maas, departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Çalışan Bilgileri Gösteriliyor...")
        print(f"Çalışan İsim: {self.isim} \nMaaşı: {self.maas} \nDepartmanı: {self.departman}")

    def departman_degistirme(self, yeni_departman):
        print("Departman Değiştirme İşlemi")
        self.departman = yeni_departman


class Yonetici_2(Calisan):
    def __init__(self, isim, maas, departman, kisi_sayisi):
        print("Yönetici sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi


    def zam_yap(self, zam_miktarı):
        self.maas += zam_miktarı

    def bilgileri_goster(self):
        print("Yönetici Bilgileri Gösteriliyor...")
        print(f"Yönetici İsim: {self.isim} \nMaaşı: {self.maas} \nDepartmanı: {self.departman} "
              f"\nSorumlu Kişi Sayısı: {self.kisi_sayisi}")

yonetici_3 = Yonetici_2("Tengri", 35000, "Bilişim", 10)

print(yonetici_3.bilgileri_goster())

print(f"{"-" * 80}")


print("Super Anahtar Kelimesi")
"""
Super Anahtar Kelimesi özellikle override ettiğimiz bir metodun içinde aynı zamanda miras aldığımız bir
metodu kullanmak istersek kullanılabilir. Yani super en genel anlamıyla miras aldığımız sınıfın metodlarını alt sınıflardan
kullanmamızı sağlar.
"""


class Calisan_3():
    def __init__(self, isim, maas, departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Çalışan Bilgileri Gösteriliyor...")
        print(f"Çalışan İsim: {self.isim} \nMaaşı: {self.maas} \nDepartmanı: {self.departman}")

    def departman_degistirme(self, yeni_departman):
        print("Departman Değiştirme İşlemi")
        self.departman = yeni_departman



class Yonetici_3(Calisan):
    def __init__(self, isim, maas, departman, kisi_sayisi):
        super().__init__(isim, maas, departman)
        print("Yönetici sınıfının init fonksiyonu")

        self.kisi_sayisi = kisi_sayisi

    def zam_yap(self, zam_miktarı):
        self.maas += zam_miktarı

    def bilgileri_goster(self):
        print("Yönetici Bilgileri Gösteriliyor...")
        print(f"Yönetici İsim: {self.isim} \nMaaşı: {self.maas} \nDepartmanı: {self.departman} "
              f"\nSorumlu Kişi Sayısı: {self.kisi_sayisi}")

yonetici_4 = Yonetici_3("TengriHan", 30050, "Yönetim", 100)

print(yonetici_4.bilgileri_goster())