print(f"""
{"-" * 80}
Kullanıcının girdiği sayının pozitif tam bölenlerini bulan kodu yazın
{"-" * 80}
""")

sayi = int(input("Sayı Giriniz: "))

for i in range(1, sayi + 1):
    if sayi % i == 0:
        print(f"Girilen Sayı: {sayi}, Bölenleri:{i}")
