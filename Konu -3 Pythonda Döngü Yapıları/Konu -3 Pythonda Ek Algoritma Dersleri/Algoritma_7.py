print("""
----------------------------------------------------------------------------
1'den n'e kadar olan sayılardan tek olanların toplamını bulunuz.
n sayısı kullanıcıdan alınacaktır
----------------------------------------------------------------------------
""")

print("Birinci Yol Mod Alma %")
n= int(input("n sayısını Giriniz: "))
toplam = 0

for i in range (n):
    if i % 2 == 1:
        toplam += i
print("tek sayıların toplamı: ", toplam)

print("-----------------------------------------")

print("İkinci Yol Döngü Aralığı")

toplam = 0

for x in range(1, n, 2):
    toplam += x
print("tek sayıların toplamı: ", toplam)


