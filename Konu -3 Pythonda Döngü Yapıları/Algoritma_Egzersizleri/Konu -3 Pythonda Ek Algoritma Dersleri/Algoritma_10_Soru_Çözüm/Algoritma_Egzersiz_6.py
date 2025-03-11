print("""
---------------------------------------------------------------------------
Aracın kilometrede ne kadar yakıt yaktığını yakıt masrafını hesaplayın.
---------------------------------------------------------------------------
""")

yol = float(input("Gidilen Yol (km): "))
harcanan_yakit = float(input("Harcanan Yakıt (L): "))
ortalama = (harcanan_yakit * 100) / yol

benzin = 36

masraf = harcanan_yakit * benzin

print("Kilometrede yakılan ortalama yakıt: {} \nYakıt masrafı: {}".format(ortalama, masraf))
