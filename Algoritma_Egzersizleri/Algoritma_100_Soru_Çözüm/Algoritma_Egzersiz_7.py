print("""
---------------------------------------------------------------------
Klavyeden girilen 5 adet sayının tek tek karelerini alan program 
---------------------------------------------------------------------
""")

sayi = [int(input(f"{i + 1}. Sayıyı Giriniz: ")) for i in range(5)]

for i in sayi:
    print("Sayı: {}, Karesi: {} ".format(i, i ** 2))

#Farklı print kullanımı
print("----------------------------------------------")
for x in sayi:
    print(f"Sayı: {x}, karesi: {x ** 2}")