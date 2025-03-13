print(f"""
{"-" * 80}
Bir komisyoncu sattığı mallardandan fiyatı 50TL'ye kadar olanlardan %3,
daha fazla olanlardan ise %2 komisyon almaktadır.
Klavyeden girilen 5 malın komisyonlarını bularak toplam komisyonu hesaplayın
{"-" * 80}
""")

sayi = [int(input(f"{i + 1}. Malın Fiyatını Giriniz: ")) for i in range(5)]

toplam = 0

for i in sayi:
    if i <= 50:
        komisyon = i * 0.03
        print(f"Ürün Fiyatı: {i} %3'lük komisyon fiyatı: {komisyon}")
        toplam += komisyon
    else:
        komisyon = i * 0.02
        print(f"Ürün Fiyatı: {i} %3'lük komisyon fiyatı: {komisyon:.2f}")
        toplam += komisyon
print(toplam)


