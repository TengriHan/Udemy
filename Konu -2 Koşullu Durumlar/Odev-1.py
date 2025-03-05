"""
Kullanıcıdan alınan boy ve kilo değerlerine göre
beden kitle indeksini hesaplayın ve şu kurallara göre şu yazıları yazdırın,
-----------------------------------------------------------------------------
Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

BKİ 18.5'un altındaysa -------> Zayıf

BKİ 18.5 ile 25 arasındaysa ------> Normal

BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

BKİ 30'un üstündeyse -------------> Obez
"""

print("""
---------------------------------------
Boy Kilo İndeksi Hesaplama
---------------------------------------
""")

boy = float(input("Boyunuzu Giriniz (m): "))
kilo = float(input("Kilonuzu Giriniz (kg): "))

indeks = kilo / (boy ** 2)

if indeks < 18.5:
    print("Boy Kilo indeksiniz: {} olduğu için Zayıfsınız".format(indeks))
elif 18.5 <= indeks < 25:
    print("Boy Kilo İndeksiniz: {} olduğu için Normal Kilodasınız".format(indeks))
elif 25 <= indeks < 30:
    print("Boy Kilo İndeksiniz: {} olduğu için Fazla Kilodasınız".format(indeks))
else:
    print("OBEZ")