print(f"""
{"-" * 80}
Aracın gittiği toplam km'deki yakıt masrafını hesaplayan kodu yazın.
{"-" * 80}
""")

yol = float(input("Gidilen Yol (km): "))
litre = float(input("Kaç litre yakıt(L): "))
yakıt = 5

masraf = litre * yakıt  # ✅ Doğru hesaplama

print(f"Gidilen Yol (km): {yol} "
      f"\nGiden Benzin (L): {litre} "
      f"\nGüncel Yakıt Fiyatı: {yakıt} "
      f"\nToplam Harcama: {masraf} TL")