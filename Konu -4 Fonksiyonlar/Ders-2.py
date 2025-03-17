"""
Fonksiyonlar
Belli işlevleri olan ve tekrar tekrar kullandığımız yapılardır.
Kod tekrarını azaltır

def fonksiyon_adı(parametre_1, parametre_2, ...(opsiyonel)
    #Fonksiyon bloğu
    Yapılacak işlemler
    #Dönüş Değeri - Opsiyonel
"""

def selamla():
    print("Merhaba...")
    print("Nasılsınız?")

print(type(selamla()))

print(selamla())

print(f"{"-" * 80}")
print("Argümanlar")
def selam(isim):
    print("İsminiz: ", isim)

print(selam("Furkan"))
print(f"{"-" * 80}")

def toplama(a, b, c):
    print("Toplamları: ", a + b + c)

print(toplama(3, 4, 5))

print(toplama(10, 20, 30))

print(f"{"-" * 80}")

def faktoriyel(sayi):
    faktoriyel = 1
    if sayi == 0 or sayi == 1:
        print("Faktoriyel: ", faktoriyel)
    else:
        while(sayi >= 1):
            faktoriyel *= sayi
            sayi -= 1
        print("Faktoriyel: ", faktoriyel)

print(faktoriyel(1))

print(faktoriyel(0))

print(faktoriyel(5))

print(faktoriyel(10))
