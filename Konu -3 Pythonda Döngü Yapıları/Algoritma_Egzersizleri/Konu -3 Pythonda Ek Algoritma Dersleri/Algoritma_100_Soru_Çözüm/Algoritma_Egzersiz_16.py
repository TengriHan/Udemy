print(f"""
{"-" * 80}
Klavyeden girilecek N sayısı kadar nottan en büyük ve en küçük olanı
bulan programı yazın.
{"-" * 80}
""")


N = int(input("Girilecek not sayısı: "))

sayi = [int(input(f"{i + 1}. Notu Giriniz: ")) for i in range(N)]

print(f"Girilen Not Sayısı: {N} \nEn Büyük Not: {max(sayi)} \nEn Küçük Sayı: {min(sayi)}")
