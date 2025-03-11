print("""
--------------------------------------------------------------------------------------
Girilen iki sayıdan ilk sayının ikinci sayıyı tam bölüp bölmediğini bulan program
--------------------------------------------------------------------------------------
""")

sayi_1 = int(input("Birinci Sayıyı (bölünecek) Giriniz: "))
sayi_2 = int(input("İkinci Sayıyı (bölen) Giriniz: "))

if sayi_1 % sayi_2 == 0:
    print("Birinci Sayı: {} İkinci Sayıyı: {} Tam bölüyor".format(sayi_1, sayi_2))
else:
    print("Birinci Sayı: {} İkinci Sayıyı: {} Tam Bölmüyor".format(sayi_1, sayi_2))
