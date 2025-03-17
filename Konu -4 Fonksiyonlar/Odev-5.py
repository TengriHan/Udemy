from math import sqrt

print(f"""
{"-" * 80}
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon
a <= 100, b <= 100
{"-" * 80}
""")

def pisagor():
    for a in range(1, 101):
        for b in range(1, 101):
            c = sqrt(a ** 2 + b ** 2)
            if c.is_integer():
                print(f"{a}, {b}, {int(c)}")

pisagor()