import math

print(f"""
{"-" * 80}
Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirin.
{"-" * 80}
""")


def hesap_makinesi():
    while True:
        print("""
        🔢 Hesap Makinesi İşlemleri:
        1 - Toplama
        2 - Çıkarma
        3 - Çarpma
        4 - Bölme
        5 - Üs Alma
        6 - Karekök
        7 - Faktöriyel
        8 - Sinüs
        9 - Kosinüs
        10 - Logaritma (10 tabanında)
        0 - Çıkış
        """)

        secim = input("Bir işlem seçin: ")

        if secim == "0":
            print("Hesap makinesi kapatılıyor...")
            break

        elif secim in ["1", "2", "3", "4", "5"]:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))

            if secim == "1":
                print(f"Sonuç: {sayi1 + sayi2}")
            elif secim == "2":
                print(f"Sonuç: {sayi1 - sayi2}")
            elif secim == "3":
                print(f"Sonuç: {sayi1 * sayi2}")
            elif secim == "4":
                if sayi2 == 0:
                    print("Hata: Sıfıra bölme hatası!")
                else:
                    print(f"Sonuç: {sayi1 / sayi2}")
            elif secim == "5":
                print(f"Sonuç: {math.pow(sayi1, sayi2)}")

        elif secim == "6":
            sayi = float(input("Sayıyı girin: "))
            print(f"Sonuç: {math.sqrt(sayi)}")

        elif secim == "7":
            sayi = int(input("Sayıyı girin: "))
            print(f"Sonuç: {math.factorial(sayi)}")

        elif secim == "8":
            sayi = float(input("Açı (derece) girin: "))
            print(f"Sonuç: {math.sin(math.radians(sayi))}")

        elif secim == "9":
            sayi = float(input("Açı (derece) girin: "))
            print(f"Sonuç: {math.cos(math.radians(sayi))}")

        elif secim == "10":
            sayi = float(input("Sayıyı girin: "))
            print(f"Sonuç: {math.log10(sayi)}")

        else:
            print("Geçersiz seçim! Lütfen 0-10 arasında bir değer girin.")


# Hesap makinesini başlat
hesap_makinesi()
