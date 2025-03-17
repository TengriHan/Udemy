print(f"""
{"-" * 80}
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen
bir tane fonksiyon yazın.
Bu siteden ne olduğuna bakabilirsiniz.
http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok
{"-" * 80}
""")

def Ekok(sayi_1, sayi_2):
    i = 2
    ekok = 1
    while True:
        if sayi_1 % i == 0 and sayi_2 % i == 0:
            ekok *= i

            sayi_1 //= i
            sayi_2 //= i
        elif sayi_1 % i == 0 and sayi_2 % i != 0:
            ekok *= i

            sayi_1 //= i
        elif sayi_1 % i != 0 and sayi_2 % i == 0:
            ekok *= i
            sayi_2 //= i
        else:
            i += 1

        if sayi_1 == 1 and sayi_2 == 1:
            break
    return ekok
sayi_1 = int(input("Sayı 1 Giriniz: "))
sayi_2 = int(input("Sayı 2 Giriniz: "))

print("Ekok", Ekok(sayi_1, sayi_2))
