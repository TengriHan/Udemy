print(f"""
{"-" * 80}
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel sayıdır. 
Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6)
{"-" * 80}
""")

def mukemmel_mi(sayi):
    toplam = 0

    for x in range(1, sayi):
        if sayi % x == 0:
            toplam += x
    return toplam == sayi

for i in range(1, 1001):
    if mukemmel_mi(i):
        print("Mükemmel Sayı: ", i)

