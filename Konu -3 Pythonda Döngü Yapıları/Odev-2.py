"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan her birinin.
4. kuvvetinin toplamı (3basamaklı sayılar için 3. kuvveti) o sayıya eşitse bu sayıya
"Armstrong" sayısı denir.
Örnek Olarak: 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

sayi = int(input("Sayı Giriniz:"))
gecici_sayi = list()

if 1000 <= sayi <= 9999:
    print("4 basamaklı sayı girdiniz: {}".format(sayi))
    for i in "sayi":
        gecici_sayi.append(sayi)
        print(gecici_sayi)

elif 100 <= sayi <= 999:
    print("3 Basamaklı sayı girdiniz: {}".format(sayi))
else:
    print("Sayı 3 basmaklı veya 4 basamaklı değil. Sayı: {} ".format(sayi))