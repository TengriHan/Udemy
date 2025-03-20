print("""
-------------------------------------------------------------------------------
Klavyeden bir tam sayı okutunuz. Bu sayı ile klavyeden okunan diğer 10 sayıyı
çarpma işlemi uygulayınız. Sonuçları ekrana yazdırınız.
-------------------------------------------------------------------------------
""")

#Furkan Çözüm
tam_sayi = int(input("Çarpılmasını istediğiniz Sayıyı Giriniz: "))

while True:
    sayi = [int(input(f"{i + 1}. Çarpan Sayıyı Giriniz: ")) for i in range(10)]

    for i in sayi:
        print(f"Çarpılan Sayı: {tam_sayi} X Çarpan Sayı: {i} Sonuç: {i * tam_sayi}")
    break

"""
CHATGPT Çözümü

# Kullanıcıdan çarpılacak ana sayıyı alıyoruz
tam_sayi = int(input("Çarpılmasını istediğiniz Sayıyı Giriniz: "))

# Kullanıcıdan 10 adet çarpan sayısını alıyoruz
sayi = []
for i in range(10):
    while True:
        try:
            # Hata kontrolü ile geçerli bir sayı almak
            sayi.append(int(input(f"{i + 1}. Çarpan Sayıyı Giriniz: ")))
            break  # Geçerli bir sayı girildiyse döngüden çık
        except ValueError:
            print("Lütfen geçerli bir tam sayı giriniz.")

# Sonuçları yazdırıyoruz
print("\nÇarpma Sonuçları:")
print("-" * 60)  # Görsel bir ayrım çizgisi ekliyoruz
for i in sayi:
    print(f"Çarpılan Sayı: {tam_sayi} X Çarpan Sayı: {i} = Sonuç: {i * tam_sayi}")

print("-" * 60)
"""