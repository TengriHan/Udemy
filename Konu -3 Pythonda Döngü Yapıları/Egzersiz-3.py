print("""
--------------------------------------------
Faktoriyel Bulma

Çıkmak için q'ya basın.
--------------------------------------------
"""
)

while True:
    sayi = input("Sayı Giriniz:")
    if sayi == "q":
        print("Program Sonlandırılıyor...")
        break
    else:
        sayi = int(sayi)

        faktoriyel = 1

        for i in range (2, sayi + 1):
            print("Faktoriyel", faktoriyel, "i:", i)
            faktoriyel *=i
        print("Faktoriyel: ", faktoriyel)