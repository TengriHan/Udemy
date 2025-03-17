"""
Fonksiyonlarda Return
Fonksiyon işlemi bittikten sonra yazdığımız değeri almamızı sağlar
"""
print("Return Kullanımı")
#Hatalı kullanım
# def toplama(a, b, c):
#     print("Toplamları", a + b + c)
#
# def iki_kati(a):
#     print("İki Katı", a * 2)


def toplama(a, b, c):
    return a + b + c

def iki_kati(a):
    return  a * 2


toplam = toplama(3, 4, 5)
print(toplam)
print(iki_kati(toplam))

print(f"{"-" * 80}")

def uc_kati(a):
    print("1. Fonksiyon çalıştı")
    return a * 3

def ikiyle_topla(a):
    print("2. Fonksiyon çalıştı")
    return a + 2

def dorde_bol(a):
    print("3. Fonksiyon çalıştı")
    return a / 4

print(dorde_bol(17))

#Return kullandıktan sonra herhangi bir işlem çalışmaz.
# Return kullanılmayan fonksiyonlara void fonksiyonlar denir. (Dış dünyaya herhangi bir değer döndürmez.)

