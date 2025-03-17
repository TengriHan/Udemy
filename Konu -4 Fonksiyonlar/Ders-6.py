print(f"""
{"-" * 80}
Lambda İfadeleri
Lambda ifadelerini(expression) fonksiyonlarımızı oluşturmak için Pythonda bulunan
pratik bir yöntemdir. Listeleri oluşturmak için list comprehension yöntemini kullanabiliyorduk.
Hatırlayım
{"-" * 80}
""")

print("Eskileri hatırlama List Comprehension kullanımı")
liste_1 = [1, 2, 3, 4, 5]
liste_2 = [i * 2 for i in liste_1]

print(liste_2)


print(f"{"-" * 80}")
print("Lambda kullanımı")

def ikiylecarp(x):
    return x * 2
print(ikiylecarp(3))


iki_ile_carp = lambda x : x * 2
print(iki_ile_carp(3))

print(f"{"*" * 80}")

def toplama(x, y, z):
    return x + y + z
print(toplama(10, 11, 13))

toplam = lambda x, y, z : x + y + z
print(toplam(3, 4, 5))

print(f"{"*" * 80}")

def ters_cevir(s):
    return s[::-1]
print(ters_cevir("Python Programlama"))

ters = lambda s : s[::-1]
print(ters("Python"))

print(f"{"*" * 80}")

def cift_tek(sayi):
    return sayi % 2 == 0
print(cift_tek(14))

tek_cift = lambda sayi : sayi % 2 == 0

print(tek_cift(13))