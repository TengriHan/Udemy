print(f"""
{"-" * 80}
Dik üçgende dik açının karşısındaki kenara hipotenüs denir. 
Hipotenüs formülü : a^2 + b^2 = c^2 olduğuna göre kullanıcıdan 
alınan A ve B kenarına göre hipotenüsü hesaplayan kodu yazınız.
{"-" * 80}
""")

a = int(input("Birinci Kenarı Giriniz: "))
b = int(input("İkinci Kenarı Giriniz: "))

c = ((a ** 2) + (b ** 2)) ** 0.5

print(f"a kenar uzunluğu: {a} \nb kenar uzunluğu: {b} \nHipotenüs (c) kenar uzunluğu: {c}")
