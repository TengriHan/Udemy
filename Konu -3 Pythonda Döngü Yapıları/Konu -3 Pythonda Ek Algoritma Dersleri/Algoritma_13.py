print("""
---------------------------------------------------------
Kullanıcıdan 10 adet sayı alan ve tek ve çift sayıların
adetini toplamını ortalamasını bulan program yazınız.
---------------------------------------------------------
""")

s = 0
tek_sayac = 0
cift_sayac = 0

tek_toplam = 0
cift_toplam = 0

for sayi in range(1, 11):
    s = int(input("Sayıyı Giriniz: "))
    if s % 2 == 1:
        tek_sayac += 1
        tek_toplam += s
    else:
        cift_sayac += 1
        cift_toplam += s
print(tek_sayac, "adet tek sayı vardır., toplamları", tek_toplam)
print("tek sayıların ortalaması: ", tek_toplam / tek_sayac)

print(cift_sayac, "adet çift sayı vardır., toplamları", cift_toplam)
print("çift sayıların ortalaması: ", cift_toplam / cift_sayac)
