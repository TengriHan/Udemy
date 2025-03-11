print("""
----------------------------------------------------------------
Kullanıcının istediği kadar sayıyı, kullanıcıdan alarak
bir diziye aktaran bu sayıların toplamını ve ortalamasını bulan
programı yazınız
----------------------------------------------------------------
""")

adet = int(input("Kaç adet sayı girmek istiyorsunuz: "))

dizi = []

for i in range(adet):
    dizi.append(int(input("Sayıyı Giriniz:")))

print(dizi)

toplam = 0

for x in dizi:
    toplam += x

print("Kullanıcıdan alınan değerlerin toplamı ", toplam)
print("Kullanıcıdan alınan değerlerin ortalaması ", toplam / adet)

