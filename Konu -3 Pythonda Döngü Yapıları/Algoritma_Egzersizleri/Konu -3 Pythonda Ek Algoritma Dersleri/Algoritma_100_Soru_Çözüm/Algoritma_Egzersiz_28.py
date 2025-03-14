print(f"""
{"*" * 80}
Kullanıcının girdiği üç kenar bilgisine göre üçgenin 
tipini belirleyen eğer girilen kenarları uzunlukları 
bir üçgen oluşturmuyorsa bunu bildiren kodu yazınız. 
( mutlak değer içinde iki kenarın farkı alınır eğer fark 
diğer kenardan büyükse girilen değerler üçgen oluşturmaz. Bu işlem tüm kenarlar için yapılır.
{"*" * 80}
""")

a = int(input("a Kenarını Giriniz: "))
b = int(input("b Kenarını Giriniz: "))
c = int(input("c Kenarını Giriniz: "))

if a + b > c and a + c > b and b + c > a:
    print("Geçerli Üçgen Kenarları")
    if a == b == c:
        print("Eş Kenar Üçgen")
    elif a == b or b == c or a == c:
        print("İkiz Kenar Üçgen")
    elif a != b != c:
        print("Çeşit Kenar Üçgen")
    else:
        print()
else:
    print("Üçgen için Geçersiz Değerler")

