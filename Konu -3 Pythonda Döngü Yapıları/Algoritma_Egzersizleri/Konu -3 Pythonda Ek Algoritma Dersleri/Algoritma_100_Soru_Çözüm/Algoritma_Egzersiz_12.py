print(f"""
{"-" * 80}
Klavyeden girilen 10 sayıdan sadece negatif olanlarını çarpımını ekrana
yazdıran program yazınız.
{"-" * 80}
""")

carpim = 1

while True:
    sayi = [int(input(f"{i + 1}. Sayıyı Giriniz: ")) for i in range(3)]

    for i in sayi:
        if i < 0:
            print(f"Negatif Sayılar: {i}")
            carpim *= i
    print(f"Sayıların çarpımı {carpim}")
    break
