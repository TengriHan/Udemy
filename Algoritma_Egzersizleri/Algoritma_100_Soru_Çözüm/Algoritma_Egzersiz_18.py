print(f"""
{"-" * 80}
Klavyeden girilen 100'lük sistemdeki 5 notu;
0, 1, 2, 3, 4 ve 5 olacak şekilde ekrana yazanp program yazınız.
{"-" * 80}
""")

sayi = [int(input(f"{i + 1}. Notu Giriniz: ")) for i in range(5)]

for i in sayi:
    if 85 <= i <= 100:
        print("5 Aldınız...")
    elif 70 <= i < 85:
        print("4 Aldınız...")
    elif 50 <= i < 70:
        print("3 Aldınız...")
    elif 40 <= i < 50:
        print("2 Aldınız...")
    elif 1 <= i < 40:
        print("1 Aldınız...")
    elif i == 0:
        print("0 Aldınız!!!!!!!")
    else:
        print("Geçersiz Not Girdiniz.....")

