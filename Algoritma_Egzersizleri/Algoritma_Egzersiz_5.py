import math

print("""
-------------------------------------------------------------------
Hipotenüs hesaplayan program yazınız.
-------------------------------------------------------------------
""")

a = int(input("Birinci Kenarı Giriniz: "))
b = int(input("İkinci Kenarı Giriniz: "))

hipotenüs = math.sqrt((a ** 2) + (b ** 2))
hipotenüs = int(hipotenüs)

print("Taban: {}, Yükseklik: {}, Hipotenüs: {}".format(a, b, hipotenüs))