print(f"""
{"-" * 80}
Fiyat ve KDV oranı ayrı ayrı girilen 5 malın toplam fiyatını hesaplayınız.
{"-" * 80}
""")

urunler = ["Patates", "Makarna", "Ekmek", "Tavuk", "Et"]

kdv_oranlari = []
fiyatlar = []
toplam_fiyat = 0

for urun in urunler:
    fiyat =float(input(f"{urun} için fiyat giriniz: "))
    kdv = float(input(f"{urun} için KDV oranı giriniz (% olarak): "))

    fiyatlar.append(fiyat)
    kdv_oranlari.append(kdv)

    kdv_fiyat = fiyat + (fiyat * kdv / 100)
    toplam_fiyat += kdv_fiyat

print(f"\nToplam KDV dahil fiyat: {toplam_fiyat:.2f} TL")
