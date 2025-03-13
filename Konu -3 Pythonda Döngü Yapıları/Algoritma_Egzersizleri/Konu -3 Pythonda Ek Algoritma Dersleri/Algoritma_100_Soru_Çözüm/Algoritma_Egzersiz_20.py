print(f"""
{"-" * 80}
İki vize ve bir final sınavına girilen üniversitede harf notuna 
vizeler %30 final ise %40 etkilidir. 
Bu üniversitenin harf ortalamasını hesaplayan kodu yazınız.
{"-" * 80}
""")

vize_1 = int(input("Birinci Vize Notunu Giriniz: "))
vize_2 = int(input("İkinci Vize Notunu Giriniz: "))
final = int(input("Final Notunu Giriniz: "))

ortalama = (vize_1 * 0.30) + (vize_2 * 0.30) + (final * 0.40)

if 85 <= ortalama <= 100:
    print("AA Aldınız...")
elif 70 <= ortalama < 85:
    print("BA Aldınız...")
elif 60 <= ortalama < 70:
    print("BB Aldınız...")
elif 50 <= ortalama < 60:
    print("CB Aldınız...")
elif 45 <= ortalama < 50:
    print("CC Aldınız...")
elif 40 <= ortalama < 45:
    print("DC Aldınız...")
else:
    print("FF Aldınız....")