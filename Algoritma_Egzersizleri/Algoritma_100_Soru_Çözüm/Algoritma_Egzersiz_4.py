print("""
----------------------------------------------------------------------
Klavyeden 0 girilene kadar sayılar okutunuz.
Girilen sayıların 2 katını alarak ekrana sonucu yazdırın.
----------------------------------------------------------------------
""")

#Furkan Çözüm
sayilar = []
while True:
    sayi = int(input("Sayı Giriniz: "))
    if sayi == 0:
        print("Program Sonlandırılıyor...")
        break
    else:
        sayilar.append(sayi * 2)
print("Girilen Sayıların 2 Katı: ", sayilar)

#ChatGpt Çözüm
# while True:
#     sayi = int(input("Sayı Giriniz: "))
#     if sayi == 0:
#         print("Program Sonlandırılıyor...")
#         break  # 0 girildiğinde çık, listeye ekleme!
#     sayilar.append(sayi * 2)  # Sayının 2 katını listeye ekle
#
# # Liste boş değilse yazdır
# if sayilar:
#     print("\nGirilen Sayıların 2 Katı:", ", ".join(map(str, sayilar)))
# else:
#     print("\nHiç sayı girilmedi.")