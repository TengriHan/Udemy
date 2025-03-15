import random

print(f"""
{"-" * 80}
İsim ve Soy isimleri atadığınız listeden rastgele isim ve soy isimler seçerek
isim oluşturan kodu yazın.
{"-" * 80}
""")

isim = ["Furkan Bayraktar",
        "Tengri Han",
        "Rabia Aykır",
        "Hakan Bayraktar",
        "Ülkü Bayraktar",
        "Gökhan Bayraktar",
        "Raay Han"]

sayi = int(input("Sayı Giriniz: "))
index = isim[sayi]

print(f"Girilen Sayı: {sayi} Oluşturulan isim: {index}")



print(f"\n{"*" * 80} ChatGpt Çözüm ")
isimler = ["Furkan", "Tengri", "Rabia", "Hakan", "Ülkü", "Gökhan", "Raay"]
soyisimler = ["Bayraktar", "Han", "Aykır", "Bayraktar", "Bayraktar", "Bayraktar", "Han"]


deger = int(input("Kaç tane isim oluşturmak istiyorsun? "))

for i in range(deger):
    rastgele_isim = random.choice(isimler)
    rastgele_soyisim = random.choice(soyisimler)
    print(f"Oluşturulan isim: {rastgele_isim} {rastgele_soyisim}")