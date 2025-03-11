print("""
------------------------------------------------------------
Kullanıcıdan ismini alıp ekrana tersten yazan program.
------------------------------------------------------------
""")

isim = input("İsim Giriniz: ")

print("1. Yol Tersine Çevirme")
isim = isim[::-1]
print(isim)

print("----------------------------------")
print("2. Yol Algoritmik")

isim_2 =input("İsim Giriniz: ")

uzunluk = len(isim_2)
print(uzunluk)
ters = ""

for i in range(uzunluk-1, -1, -1):
    ters += isim_2[i]
print(ters)