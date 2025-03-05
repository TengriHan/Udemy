"""
Koşullu durumlar - if - else
"""
space = "--------------------------"

print("Örnek Python çalıştırılma mantığı")
a = 2
b = 3
c = 4
print(a + b + c)

print(space)

print("Örnek if kullanımı")
if a == 2:
    print(a)
print("Merhaba")

if a == 3:
    print(a)
print("Merhaba")

print(space)

"""
Koşullu durumlar belli koşullara göre belli işlemin yapılıp yapılmaması
"""
# if Bloğu belirli bir koşulu kontrol etmek istersek kullanılan bloklardır.
print("if koşul durumları")
yas = int(input("Yaşınızı Giriniz: "))

if yas < 18:
    print("Bu mekana giremezsiniz!")

print(space)

"""
else bloğu if koşulu sağlanmadıysa else bloğu çalışır.
"""
print("else koşul durumları")
if yas < 18:
    print("Bu mekana giremezsiniz!")
else:
    print("Mekana hoş geldiniz.")

print(space)

sayı = int(input("Sayı: "))

if sayı < 0:
    print("Negatif Sayı")
else:
    print("Sıfır veya pozitif sayı")