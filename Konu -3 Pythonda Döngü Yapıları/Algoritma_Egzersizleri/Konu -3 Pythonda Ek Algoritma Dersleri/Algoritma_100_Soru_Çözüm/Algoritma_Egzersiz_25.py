print(f"""
{"-" * 80} 
Beden kütle endeksi kilo/boy^2 formulü ile hesaplanarak bireyin kilolu
normal zayıf veya obez sınıfına girdiği ile ilgili sonuç verir.
Kütle Endeksi (KE) < 18.5 ise Zayıf , 18.5 < (KE) <=25 ise Normal , 
25 < (KE) <= 30 ise Kilolu , (KE) > 25 ise birey obez sınıfına girmektedir. Kütle endeksi kodunu yazınız.
{"-" * 80}
""")

kilo = float(input("Kilonuzu Giriniz: "))
boy = float(input("Boyunuzu Giriniz: "))

kutle_endeksi = kilo / (boy ** 2)

if kutle_endeksi < 18.5:
    print("Zayıfsınız...")
elif 18.5 < kutle_endeksi <= 25:
    print("Normal Kilodasınız...")
elif 25 < kutle_endeksi <= 30:
    print("Kilolusunuz...")
else:
    print("Obezsiniz...")
