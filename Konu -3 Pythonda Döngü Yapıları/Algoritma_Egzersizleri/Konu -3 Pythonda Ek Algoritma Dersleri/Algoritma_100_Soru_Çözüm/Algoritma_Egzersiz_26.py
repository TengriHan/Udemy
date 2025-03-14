print(f"""
{"-" * 80}
Çarpım tablosunu ekrana yazan kodu yazınız.
{"-" * 80}
""")


for i in range(1, 11):
    print(f"\nÇARPIM TABLOSU - {i}")
    print(f"{"*" * 50}")
    for x in range(1, 11):
        print(f"{i} x {x} = {i * x}")  # Daha düzenli format


