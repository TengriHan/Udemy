import math

print("""
-------------------------------------------------------------------------------
İkinci dereceden ax^2 + bx + c = 0 denkleminin diskriminant çözümünü yapınız.
Kullanıcıdan a, b, c değerlerini alarak deltayı hesaplayınız.
-------------------------------------------------------------------------------
delta = b^2 - 4ac
"""
)

a = int(input("Birinci Sayıyı Giriniz: "))
b = int(input("İkinci Sayıyı Giriniz: "))
c = int(input("Üçüncü Sayıyı Giriniz: "))

delta = (b ** 2) - (4 * a * c)

print("Delta = ", delta)

if delta > 0:
    print("Sistemin 2 kökü vardır.")
    kok_1 = (-b + math.sqrt(delta)) / (2 ** a)
    print("Birinci kökümüz: ",kok_1)
    kok_2 = (-b - math.sqrt(delta)) / (2 ** a)
    print("İkinci kökümüz: ", kok_2)
elif delta == 0:
    kok = -b / (2 * a)
    print("Çakışık kök vardır, Kök: {}", kok)
else:
    print("Sistemin Kökü yoktur.")