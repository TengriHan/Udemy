"""
2. Dereceden Bilinmeyenli denklemin köklerini bulma

Denklem: ax^2 + bx + c
Deltayı Hesaplama: b ** 2 - 4 * a * c

Birinci Kök: (-b -delta ** 0.5) / (2 * a)
İkinci Kök: (-b +delta ** 0.5) / (2 * a))

"""
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b ** 2 - 4 * a * c

kök1 = (-b -delta ** 0.5) / (2 * a)
kök2 = (-b +delta ** 0.5) / (2 * a)

print("Birinci kök: {} \nİkinci Kök: {}\n".format(kök1, kök2))