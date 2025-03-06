"""
Döngülerde kullanılan ifadeler
break - continue
"""
"""
break döngülerde kullanıldığında break ifadesiyle karşılancı program çalışmasını durdurur.
Böylelikle döngü hiçbir koşula bağlı kalmadan sonlanmış olur.
Break sadece içinde bulunduğu döngüyü sonlandırır. Eğer iç içe döngü varsa break hangi kısımdaysa o 
döngüyü sonlandırır.
"""
space = "---------------------------------------"
print("""
---------------------------------------
Break kullanımı
---------------------------------------
""")
i = 0

while i < 10:
    if i == 5:
        break
    print("i:", i)
    i += 1


print(space)

liste = [1, 2, 3, 4, 5]

for i in liste:
    if i == 3:
        break
    print("i:", i)

print(space)

while True:
    isim = input("İsminizi Girin (Çıkmak için q'ya basın):")
    if isim == "q":
        print("Programdan Çıkılıyor...")
        break
    print(isim)

print(space)

"""
continue ifadesi break'e göre daha az kullanılır.
Döngü herhangi bir yerde veya herhangi bir zamanda continue ifadesiyle karşılaştığı zaman 
geri kalan işlemlerini yapmadan direk bloğun başına döner.
"""
print("""
---------------------------------------
Continue kullanımı
---------------------------------------
""")

print("Liste oluşturma ve liste içerisinde sayı atlama")
liste_1 = list(range(11))
print(liste_1)

for i in liste_1:
    if i == 3 or i == 5:
        continue
    print("i:", i)

print(space)

print("""
Yanlış kullanım
while i < 10:
    if i == 2:
        continue
    print(i)
    
Bu kodu sakın böyle çalıştırma Sonsuz döngü problemi
""")

x = 0

while x < 10:

    if x == 2:
        x += 1
        continue
    print(x)
    x += 1
