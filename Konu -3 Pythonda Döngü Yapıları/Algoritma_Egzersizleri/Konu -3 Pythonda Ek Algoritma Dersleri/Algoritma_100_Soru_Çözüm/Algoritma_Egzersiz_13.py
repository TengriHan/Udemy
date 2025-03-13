print(f"""
{"-" * 80}
Klavyeden girilen 10 sayıdan 5'ten büyük olanların yarısını,
5' eşit ve küçük olan sayıların 2 katını bulan program.
{"-" * 80}
""")

sayi = [int(input(f"{i + 1}. Sayıyı Giriniz: ")) for i in range(10)]

for i in sayi:
    if i > 5:
        yarim = i / 2
        print(f"Girilen Sayı: {i} Girilen Sayının Yarısı: {yarim}")
    else:
        kat = i * 2
        print(f"Girilen Sayı: {i}, Girilen Sayının 2 katı: {kat}")
