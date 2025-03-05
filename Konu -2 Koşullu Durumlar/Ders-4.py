"""
if - elif - else durumları
Bir çok durumu kontrol etmek için kullanılır.
"""
"""
if koşul:
elif başka bir koşul:
elif başka bir koşul:
elif başka bir koşul:
else: yapılacak işler
"""
space = "----------------------------------"

print("if - elif - else kullanımı")
islem = int(input("İşlem Giriniz: "))

if islem == 1:
    print("İşlem 1 seçildi")
elif islem == 2:
    print("İşlem 2 seçildi")
elif islem == 3:
    print("İşlem 3 seçildi")
elif islem == 4:
    print("İşlem 4 seçildi")
else:
    print("Geçersiz işlem")

print(space)

note = float(input("Notunuzu girin: "))

if note >= 90:
    print("AA")
elif note >= 85:
    print("BA")
elif note >= 75:
    print("CB")
elif note >= 70:
    print("CC")
elif note >= 65:
    print("CD")
elif note >= 60:
    print("DC")
elif note >= 55:
    print("DD")
else:
    print("Kaldınız!")