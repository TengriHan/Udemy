print(f"""
{"-" * 80}
Sayı Tahmin Oyunu
- 1 ile 40 arasındaki sayıyı tahmin edin.
{"-" * 80}
""")

import random
import time

rastgele_sayi = random.randint(1, 1000)
tahmin = 7

while True:
    tahmin = int(input("Tahmininiz: "))

    if tahmin < rastgele_sayi:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Daha Yüksek Bir Sayı Giriniz...")
        tahmin -= 1

    elif tahmin > rastgele_sayi:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Daha Küçük Bir Sayı Giriniz...")
        tahmin -= 1

    else:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler Doğru Tahmin Ettiniz: ", rastgele_sayi)
        break
    if tahmin == 0:
        print("Tahmin Hakkınız Bitmiştir!!!")
        print("Sayı: ",rastgele_sayi)
