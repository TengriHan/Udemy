print(f"""
{"-" * 80}
Klavyeden 5 adet yarıçapı verilen çemberlerin alanını ve çevresini hesaplayan program
{"-" * 80}
""")

yaricap = [int(input(f"{i + 1}. Dairenin Yarı Çapını Giriniz: ")) for i in range(5)]
pi = 3.14

for i in yaricap:
    alan = (i ** 2) * pi
    cevre = (2 * pi * i)
    print(f"Dairenin Alanı: {alan} , Dairenin Çevresi: {cevre:.2f}")