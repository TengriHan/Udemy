print("""
----------------------------------------------------------------------
Klavyeden girilen 10 adet notun en büyük ve en küçüğünü bulunuz.
----------------------------------------------------------------------
""")

#Furkan Çözüm
notlar = [int(input(f"{i+1} Not Giriniz: ")) for i in range(5)]

en_kucuk = min(notlar)
en_buyuk = max(notlar)

print("Notlar: {} \nEn Küçük Not: {} \nEn Büyük Not: {}".format(notlar, en_kucuk, en_buyuk))
print("-" * 80)

#Chatgpt Çözüm
print(f"\nNotlar: {notlar}")
print(f"En Küçük Not: {min(notlar)}")
print(f"En Büyük Not: {max(notlar)}")