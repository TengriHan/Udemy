print(f"""
{"-" * 80}
Bir sayının kendisi dışında bütün pozitif bölenlerinin 
toplamı kendisine eşit olan sayılara mükemmel sayı denir. 
Kullanıcıdan alınan sayının mükemmel sayı olup olmadığını kontrol eden kodu yazınız.
{"-" * 80}
""")

sayi = int(input("Sayı Giriniz: "))
toplam = 0

for i in range(1, sayi):
    if sayi % i == 0:
        toplam += i
if toplam == sayi:
    print("Sayı Mükemmel")
else:
    print("Sayı Mükemmel Değil")

