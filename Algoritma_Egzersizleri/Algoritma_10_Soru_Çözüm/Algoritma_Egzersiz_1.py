print("""
----------------------------------------------------------------------------
Girilen bir sayının pozitif veya negatif olduğunu gösteren program
----------------------------------------------------------------------------
""")

sayi = int(input("Sayı Giriniz: "))

if sayi == 0:
    print("Sayı Nötr Bir Sayıdır: ", sayi)
elif sayi < 0:
    print("Sayı Negatif Bir Sayıdır: ", sayi)
else:
    print("Sayı Pozitif Bir Sayıfıdır: ", sayi)