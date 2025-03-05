"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın
"""

a = int(input("Birinci sayıyı Giriniz: "))
b = int(input("İkinci sayıyı Giriniz: "))
c = int(input("Üçüncü sayıyı Giriniz: "))


if a >= b and a >= c:
    print("En büyük sayı:", a)
elif b >= a and b >= c:
    print("En büyük sayı:", b)
elif c >= a and c >= b:
    print("En büyük sayı:", c)
