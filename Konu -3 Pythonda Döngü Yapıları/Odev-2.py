"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan her birinin.
4. kuvvetinin toplamı (3basamaklı sayılar için 3. kuvveti) o sayıya eşitse bu sayıya
"Armstrong" sayısı denir.
Örnek Olarak: 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

sayi = input("Sayı Giriniz:")
basamak_sayisi = len(sayi)
sayi = int(sayi)
basamak = 0
toplam = 0

gecici_sayi = sayi

while gecici_sayi > 0:
    basamak = gecici_sayi % 10

    toplam += basamak ** basamak_sayisi
    gecici_sayi //= 10
if toplam == sayi:
    print(sayi, "bir armstrong sayıdır.")
else:
    print(sayi, "bir armstrong sayısı değildir.")