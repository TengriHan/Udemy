print("""
-------------------------------------------------------------------------------
Klavyeden girilen sayının karesini alın bulduğu sonucun rakamları çarpımını
ekrana yazdıran programın algoritması ve akış şemasını yazın
-------------------------------------------------------------------------------
""")

sayi = int(input("Bir sayı giriniz: "))
sayi_kare = sayi * sayi
print(f"Girilen Sayı: {sayi} \nGirilen Sayının Karesi: {sayi_kare}")

sayi_kare = str(sayi_kare)

carpim = 1

for i in sayi_kare:
    rakam = int(i)
    carpim *= rakam
    print(f"Girilen Sayının Karesine Ait Rakam: {rakam}")

print(f"Rakamların Çarpımı: {carpim}")




