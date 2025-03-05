"""
Hesap makinesi
"""
print("""
------------------------------------------------------
Hesap Makinesi Programı                              

İşlemler;
1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
------------------------------------------------------
""")
a = int(input("Birinci Sayıyı giriniz: "))
b = int(input("İkinci Sayıyı giriniz: "))

islem = input("İşlem giriniz: ")

if islem == "1":
    print("{} ile {} in toplamı {}'dir".format(a, b, a + b))
elif islem == "2":
    print("{} ile {} in çıkarılmışı {}'dir".format(a, b, a - b))
elif islem == "3":
    print("{} ile {} in çarpılmışı {}'dir".format(a, b, a * b))
elif islem == "4":
    print("{} ile {} in bölünmesi {}'dir".format(a, b, a / b))
else:
    print("Geçersiz işlem")
