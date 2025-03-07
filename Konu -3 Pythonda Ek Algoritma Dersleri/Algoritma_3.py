print("""
------------------------------------------------------------------
Kullanıcıdan alınan 3 sayının en büyüğünü bulma
------------------------------------------------------------------
""")

sayi_1 = float(input("Birinci Sayıyı Giriniz: "))
sayi_2 = float(input("İkinci Sayıyı Giriniz: "))
sayi_3 = float(input("Üçüncü Sayıyı Giriniz: "))

if sayi_1 > sayi_2 and sayi_1 > sayi_3:
    print("En büyük sayı birinci sayıdır: {}".format(sayi_1))
elif sayi_2 > sayi_1 and sayi_2 > sayi_3:
    print("En büyük sayı ikinci sayıdır: {}".format(sayi_2))
else:
    print("En büyük sayı üçüncü sayıdır: {}".format(sayi_3))
