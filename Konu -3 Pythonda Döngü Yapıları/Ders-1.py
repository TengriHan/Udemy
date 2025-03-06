"""
Döngü Yapılarına Giriş
Bütün programlama dillerinde bulunan ve belli koşullarda işlemlerinin sürekli tekrar
eden yapılardır.
"""

"""
in operatörü bir elemanın başka bir listede demette veya stringte 
bulunup bulunmadığını kontrol eder.
"""
space = "--------------------------------------"

print(space)
print("in kullanımı")
ornek_list = [1,2,3,4]
print(5 in ornek_list)
print(2 in ornek_list)

print("p" in "Python")
print(4 in (1,2,3,4))

print(space)

"""
For döngüleri demetlerin listelerin stringlerin hatta sözlüklerin üzerinde 
dolaşmamızı sağlayan bir döngü türüdür.

for eleman in veri_yapısı(liste, demet vs.):
    Yapılacak İşlemler
    
Bu yapı bize eleman değişkeni her döngünün başında listenin, demetin vs. her bir elemanına
eşit olacak ve her döngüde bu elemanla işlem yapılacak.

"""
print("For döngüsü kullanımı")

liste = [1, 2, 3, 4, 5, 6, 7]
toplam = 0

print("Liste içerisindeki elemanları yazdırma.")
for eleman  in liste:
    print(eleman)

print(space)

print("Liste içerisindeki değerleri toplama")
for eleman in liste:
    toplam = toplam + eleman
    print("Toplam: {} Eleman: {}".format(toplam, eleman))
print(toplam)

print(space)

print("Çift sayıları bulma")
liste_2 = [1, 2, 3, 4, 34, 54, 63, 78]

for eleman in liste_2:
    if eleman % 2 == 0:
        print(eleman)

print(space)

print("Metin Yazdırma")
metin = "Python"

for i in metin:
    print(i)

print(space)

print("Metni Çarpma")
for i in metin:
    print(i * 3)

print(space)

demet = (1, 2, 3, 4, 5)

for a in demet:
    print(a)

print(space)

liste_3 = [(1, 2), (3, 4), (5, 6), (7, 8)]

for eleman in liste_3:
    print(eleman)

print("Demet içersinde gezinme")
for i, j in liste_3:
    print("i: {} j: {}".format(i, j))

print(space)
print("Demet içerisindeki elemanları çarpma")
for i, j in liste_3:
    print(i * j)

print(space)
print("Sözlüklerde for kullanımı")
dictionary = {"bir": 1, "iki": 2, "üç": 3, "dört": 4}
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

print(space)

print("Value değerlerini for ile çekme")
for eleman in dictionary.values():
    print(eleman)

for i, j in dictionary.items():
    print("Anahtar: {} , Değer: {}".format(i, j))

print(space)

liste_4 = [2, 1, 10, 2, 23, 1, 56, 3]
total = 0

for i in liste_4:
    if not (i % 2 == 0):
        total += i
print(total)