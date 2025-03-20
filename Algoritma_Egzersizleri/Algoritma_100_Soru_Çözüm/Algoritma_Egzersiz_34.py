import math

print(f"""
{"-" * 80}
Kullanıcıdan alınan iki sayı arasındaki asal sayıları bulan kod.
{"-" * 80}
""")

baslangic_sayi = int(input("Başlangıç Sayısını Giriniz: "))
bitis_sayi = int(input("Bitiş Sayısını Giriniz: "))

print(f"\n{baslangic_sayi} ile {bitis_sayi} arasındaki asal sayılar:")

for num in range(baslangic_sayi, bitis_sayi + 1):
    if num < 2:
        continue

    asal = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            asal = False
            break

    if asal:
        print(num, end=" ")
