import math

print("""
-------------------------------------------------------------------
Kullanıcının istediği büyüklükte bir diziyi 0-100 arasında rastgele
oluşturulmuş sayılarla doldurup bu sayıların standart sapmasını
hesaplayınız.
-------------------------------------------------------------------
"""
)
import random

uzunluk = int(input("Dizi uzunluğunu giriniz: "))

dizi = []

for i in range(uzunluk):
    dizi.append(random.randint(0, 100))

print(dizi)

toplam = 0

for x in dizi:
    toplam += x
print("Toplam =", toplam)
ortalama = toplam / uzunluk
print("Ortalama =", ortalama)

fark_toplam = 0

for j in dizi:
    fark = j - ortalama
    fark = fark ** 2
    fark_toplam += fark

standart_sapma = math.sqrt(fark_toplam / uzunluk)

print("Standart Sapma =", standart_sapma)
