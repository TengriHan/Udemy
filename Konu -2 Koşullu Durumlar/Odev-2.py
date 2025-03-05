"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın
"""
print("""
----------------------------------------------------------
En büyük sayıyı Bulma
----------------------------------------------------------

""")
sayi_1 = int(input("Birinci sayıyı Giriniz: "))
sayi_2 = int(input("İkinci sayıyı Giriniz: "))
sayi_3 = int(input("Üçüncü sayıyı Giriniz: "))

if sayi_1 > sayi_2 > sayi_3:
    print("Birinci sayı: {} En Büyük \nİkinci sayı: {} Orta \nÜçüncü sayı: {} En küçük sayıdır.". format(sayi_1, sayi_2, sayi_3))
elif sayi_1 > sayi_3 > sayi_2:
    print("Birinci sayı: {} En Büyük \nÜçüncü sayı: {} Orta \nİkinci sayı: {} En küçük sayıdır.". format(sayi_1, sayi_3, sayi_2))
elif sayi_2 > sayi_1 > sayi_3:
    print("İkinci sayı: {} En Büyük \nBirinci sayı: {} Orta \nÜçüncü sayı: {} En küçük sayıdır.". format(sayi_2, sayi_1, sayi_3))
elif sayi_2 > sayi_3 > sayi_1:
    print("İkinci sayı: {} En Büyük \nÜçüncü sayı: {} Orta \nBirinci sayı: {} En küçük sayıdır.". format(sayi_2, sayi_3, sayi_1))
elif sayi_3 > sayi_2 > sayi_1:
    print("Üçüncü sayı: {} En Büyük \nİkinci sayı: {} Orta \nBirinci sayı: {} En küçük sayıdır.". format(sayi_3, sayi_2, sayi_1))
elif sayi_3 > sayi_1 > sayi_2:
    print("Üçüncü sayı: {} En Büyük \nBirinci sayı: {} Orta \nİkinci sayı: {} En küçük sayıdır.". format(sayi_3, sayi_1, sayi_2))
elif sayi_1 == sayi_2 == sayi_3:
    print("Birinci sayı: {} Eşittir \nİkinci sayı: {} Eşittir \nÜçüncü sayı: {} Eşittir.". format(sayi_1, sayi_2, sayi_3))
elif sayi_1 == sayi_2 > sayi_3:
    print("Birinci sayı: {} Eşittir \nİkinci sayı: {} Büyüktür \nÜçüncü sayı: {} En küçük sayıdır.". format(sayi_1, sayi_2, sayi_3))

elif sayi_3 == sayi_1 > sayi_2:
    print("Üçüncü sayı: {} Eşittir \nBirinci sayı: {} Büyüktür \nİkinci sayı: {} En küçük sayıdır.". format(sayi_3, sayi_1, sayi_2))
elif sayi_3 > sayi_1 == sayi_2:
    print("Üçüncü sayı: {} Büyüktür \nBirinci sayı: {} Eşittir \nİkinci sayı: {} En küçük sayıdır.". format(sayi_3, sayi_1, sayi_2))
elif sayi_2 > sayi_1 == sayi_3:
    print("İkinci sayı: {} Büyüktür \nBirinci sayı: {} Büyüktür \nÜçüncü sayı: {} En küçük sayıdır.". format(sayi_2, sayi_1, sayi_3))
else:
    print("HANGİ Değerleri girdin reis başka koşul kalmadı \nBirinci Sayı: {} \nİkinci Sayı: {} \nÜçüncü Sayı: {}".format(sayi_1, sayi_2, sayi_3))