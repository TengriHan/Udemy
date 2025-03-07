"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam"
isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana
"toplam değişkenini" bastırın
İpucu: while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.
"""
toplam = 0
while True:
    sayi = (input("Sayı Giriniz (Çıkmak için q'ya basınız): "))
    if sayi == "q":
        print("Program sonlandırılıyor...")
        break
    sayi = int(sayi)
    toplam += sayi
    print("Kullanıcının girdiği Sayıların Toplamı: ", toplam)



