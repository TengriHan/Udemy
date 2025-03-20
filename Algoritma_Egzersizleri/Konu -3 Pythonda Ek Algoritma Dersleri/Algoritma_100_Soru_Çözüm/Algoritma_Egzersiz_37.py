print(f"""
{"-" * 80}
Klavyeden dakika olarak girilen 
5 şarkının toplam süresini saat ve dakika olarak hesaplayan program.
{"-" * 80}
""")

# 5 şarkının süresini listeye alıyoruz
sarki_sureleri = [float(input(f"{i + 1}. Şarkıyı Giriniz (dakika): ")) for i in range(5)]

# Toplam süreyi hesapla
toplam_dakika = sum(sarki_sureleri)

# Saat ve dakika olarak ayır
saat = int(toplam_dakika // 60)  # Kaç saat olduğunu bul
dakika = int(toplam_dakika % 60)  # Kalan dakikayı bul

# Çıktıyı yazdır
print(f"\nToplam Süre: {saat} saat {dakika} dakika")
