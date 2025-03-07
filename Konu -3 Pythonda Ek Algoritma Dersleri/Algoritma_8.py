print("""
----------------------------------------------------------------------------
n'den m'ye kadar olan sayılardan 7'ye tam bölünenlerinin toplamını bulunuz.
n başlangıç ve m bitiş sayısı kullanıcıdan alınacaktır.
----------------------------------------------------------------------------
""")

while True:
    n = int(input("Başlangıç Sayısını Giriniz: "))
    m = int(input("Bitiş Sayısını Giriniz: "))
    toplam = 0

    if n >= m:
        print("Hatalı Giriş yaptınız Başlangıç Bitişten küçük olamaz...")
        print("Tekrar sayı giriniz...")
    else:
        for i in range (n, m):
            if i % 7 == 0:
                toplam += i
        print("Yediye Tam Bölünen Sayıların Toplamı: ", toplam)
        break