print(f"""
{"-" * 80}
Bir Sayının Tam bölenlerini bulma
{"-" * 80}
""")


def tam_bolen(sayi):
    tam_bolenler = []
    for i in range(2, sayi):
        if sayi % i == 0:
            tam_bolenler.append(i)
    return tam_bolenler

while True:
    sayi = input("Sayı Giriniz: ")
    if sayi == "q":
        print("Program Sonlandırılıyor...")
        break
    else:
        sayi = int(sayi)
        print("Tam Bölenler: ", tam_bolen(sayi))
