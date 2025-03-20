print("""
-------------------------------------------------------------------------
Klavyeden girilen 5 adet sayının 10'dan büyük olanlarını sayan program
-------------------------------------------------------------------------
""")
#Furkan Çözüm
sayi = [int(input(f"{i+1} Sayı Giriniz: ")) for i in range(5)]

for i in sayi:
    if i >= 10:
        print("10'dan büyük sayılar: ", i)

print("-" * 80)

#Chatgpt Çözüm
buyuk_sayilar = [i for i in sayi if i >  10]

if buyuk_sayilar:
    print("\n10'dan büyük sayılar:", ", ".join(map(str, buyuk_sayilar)))
else:
    print("\n10'dan büyük sayı yok!")
