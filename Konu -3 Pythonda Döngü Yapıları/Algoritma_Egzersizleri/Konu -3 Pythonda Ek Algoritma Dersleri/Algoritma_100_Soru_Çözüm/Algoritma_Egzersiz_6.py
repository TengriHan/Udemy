print("""
----------------------------------------------------------------------------
30 kişilik sınıfta yaşı 13, 14, 15 ve 16 olanların sayısını ayrı ayrı bulan
program yazınız.
----------------------------------------------------------------------------
""")

yas = [int(input(f"{i + 1} Yaş Giriniz: ")) for i in range(30)]

for i in yas:
    if 13 <= i <= 16:
        print("Yaş: ", i)
    else:
        print("13, 14, 15 ve 16 yaşında öğrenci yok!!!")
