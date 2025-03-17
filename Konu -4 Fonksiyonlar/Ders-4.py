print("""
Foknisyonlardaki Parametre Türleri
""")

def selamla(isim):
    print("Merhaba", isim)

print(selamla("Furkan"))

print("Varsayılan olarak ayarlama")
def selam(isim = "İsimsiz"):
    print("Merhaba", isim)

print(selam())

print(f"{"-" * 80}")

def bilgiler(ad = "Bilgi Yok", soyad = "Bilgi Yok", numara = "Bilgi Yok"):
    print("Ad: ", ad, "Soyad: ", soyad, "Numara: ", numara)

print(bilgiler("Furkan", "Bayraktar", "25144845058"))

print(bilgiler())

print(bilgiler("Furkan", "Bayraktar"))

print(bilgiler(numara="25144845058"))

print(f"{"-" * 80}")

def toplama(a, b, c):
    print(a + b + c)

toplama(3, 4, 5)

def toplam(*a):
    print(a)

print(toplam(1, 2, 3))

def toplam_hepsi(*a):
    toplama_2 = 0
    for i in a:
        toplama_2 += i

    print(toplama_2)

print(toplam_hepsi(1, 2, 3, 4))
