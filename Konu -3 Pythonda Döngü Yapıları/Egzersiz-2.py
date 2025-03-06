print("""
------------------------------------------------
ATM Makinesine Hoş Geldiniz.
------------------------------------------------
İşlemler
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
Programdan çıkmak için 'q'ya basın.
------------------------------------------------
"""
)

bakiye = 1000

while True:
    islem = input("İşlemi Seçiniz:")
    if islem == "q":
        print("Yine Bekleriz....")
        break
    elif islem == "1":
        print("Bakiyeniz {} tl'dir".format(bakiye))
    elif islem == "2":
        miktar = int(input("Miktar Giriniz:"))
        bakiye += miktar
    elif islem == "3":
        miktar =int(input("Miktar Giriniz:"))
        if bakiye - miktar < 0:
            print("Yetersiz Bakiye...")
            continue
        bakiye -= miktar

    else:
        print("Geçersiz İşlem")
