print("""
-------------------------------------------------------------------------
Girilen bir metnin sayının polindromik olup olmadığını kontrol edin.
-------------------------------------------------------------------------
""")

icerik = input("Bir metin veya Sayı Giriniz: ")
ters_icerik = icerik[::-1]

if icerik == ters_icerik:
    print("Girilen içerik Polindromiktir. \nİçerik:", icerik)
else:
    print("Girilen içerik Polindromik Değildir. \nİçerik:", icerik)
