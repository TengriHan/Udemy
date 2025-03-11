import math

print("""
---------------------------------------------------------------------
Girilen bir sayının tam kare olup olmadığını kontrol eden program.
---------------------------------------------------------------------
""")

sayi = int(input("Sayı Giriniz: "))

karekok = sayi ** (1/2)

if round (karekok)  ** 2 == sayi:
    print("Girilen Sayı Tam Karedir")
else:
    print("Girilen Sayı Tam Kare Değildir!!!")