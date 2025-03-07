print("""
------------------------------------------------------------------------
Girilen bir sayının çift veya tek olduğunu bulan program yazınız.
------------------------------------------------------------------------
""")

sayi = int(input("Sayı Giriniz: "))

if sayi % 2 == 0:
    print("Sayı Çifttir, Sayı: ", sayi)
else:
    print("Sayı Tektir, Sayı: ", sayi)