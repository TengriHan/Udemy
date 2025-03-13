print(f"""
{"-" * 80}
Sayısal olarak girilen bir ay bilgisini ekrana 
“Ocak, Şubat, Mart veya diğer aylardan biri…” 
şeklinde yazan programı yapınız.
{"-" * 80}
""")

deger = int(input("Kaçıncı Ay: "))

aylar = {"Ocak": 1, "Şubat": 2, "Mart": 3,
         "Nisan": 4, "Mayıs": 5, "Haziran": 6,
         "Temmuz": 7, "Ağustos": 8, "Eylül": 9,
         "Ekim": 10, "Kasım": 11, "Aralık": 12}

for ay, rakam in aylar.items():
    if deger == rakam:
        print(f"Girilen ay {deger} karşılığı {ay}")


