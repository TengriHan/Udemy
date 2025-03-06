"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayı kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
Örnek 6 Mükemmel Sayıdır (1 + 2 + 3 = 6)
"""

print("""
--------------------------------------------------------------------------------------------
Mükemmel sayı bulma programına Hoş Geldiniz.
--------------------------------------------------------------------------------------------
Bir sayı kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
Örnek 6 Mükemmel Sayıdır (1 + 2 + 3 = 6)
--------------------------------------------------------------------------------------------

""")

sayi = int(input("Sayı Giriniz:"))
mukemmel = 1
toplam = 0

while mukemmel < sayi:
    if sayi % mukemmel == 0:
        toplam += mukemmel
    mukemmel +=  1

if toplam == sayi:
    print(sayi, "Mükemmel Sayıdır.")
else:
    print(sayi, "Mükemmel Sayı değildir.")