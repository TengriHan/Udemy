print("""
-----------------------------------------------------------------------------------------
Kullanıcıdan alınan bir cümlede kaç adet kelime olduğunu ve kaç adet harf
olduğunu bulan program yazın.
-----------------------------------------------------------------------------------------
""")

metin = input("Metin Giriniz: ")
bosluk_sayac = 0

for k in metin:
    if k == " ":
        bosluk_sayac += 1

print("Boşluk adeti: ",bosluk_sayac)
print("Kelime sayısı: ", bosluk_sayac + 1)
print("Harf sayısı: ", len(metin))