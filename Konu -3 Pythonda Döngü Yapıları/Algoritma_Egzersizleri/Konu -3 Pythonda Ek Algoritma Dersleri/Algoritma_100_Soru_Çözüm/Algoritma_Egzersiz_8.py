print("""
-----------------------------------------------------------------------
Klavyeden 3 not girilir. İlk Notun %30 ikinci notun %30 son notun %40
sonuç olarak da 3 notun yüzdelerini toplayıp ekrana yazdırın
-----------------------------------------------------------------------
""")

notlar = [int(input(f"{i + 1}. Notu Giriniz: ")) for i in range(3)]

yuzde = (notlar[0] * 0.30) + (notlar[1] * 0.30) + (notlar[2] * 0.40)

print(f"1. Not: {notlar[0]}, 2.Not: {notlar[1]}, 3.Not: {notlar[2]} \n\nYüzdeleri toplamı: {yuzde}")

"""
ChatGpt Çözüm
************************************************************************************
# Notları al
notlar = [int(input(f"{i+1}. Notu Giriniz: ")) for i in range(3)]
weights = [0.30, 0.30, 0.40]  # Ağırlık yüzdeleri

# Yüzde hesaplaması
yuzde = sum(n * w for n, w in zip(notlar, weights))

# Sonuçları ekrana yazdır
print(f"\n1. Not: {notlar[0]}, 2. Not: {notlar[1]}, 3. Not: {notlar[2]}")
print(f"\nYüzdeleri toplamı: {yuzde:.2f}")

************************************************************************************
"""