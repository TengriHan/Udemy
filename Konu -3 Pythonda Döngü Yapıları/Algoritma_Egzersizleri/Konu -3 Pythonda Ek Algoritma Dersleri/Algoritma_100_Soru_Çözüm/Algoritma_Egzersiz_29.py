print(f"""
{"*" * 80}
Kullanıcıdan alınan dört kenarın bilgisine göre şeklin 
kare,dikdörtgen veya diğer dörtgenlerden olduğunu belirten kodu yazınız.
{"*" * 80}
""")

a = int(input("Birinci kenarı giriniz: "))
b = int(input("İkinci kenarı giriniz: "))
c = int(input("Üçüncü kenarı giriniz: "))
d = int(input("Dördüncü kenarı giriniz: "))

if a == b == c == d:
    print("Kare")
elif len({a, b, c, d}) == 2:
    print("Dikdörtgen")

else:
    print("Dörtgen")