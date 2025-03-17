print(f"""
{"-" * 80}
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen
bir tane fonksiyon yazın.
Bu siteden ne olduğuna bakabilirsiniz.
http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok
{"-" * 80}
""")

def Ebob(sayi_1, sayi_2):
    sayi_1_bolen = [i for i in range(1, sayi_1 + 1) if sayi_1 % i == 0]
    sayi_2_bolen = [i for i in range(1, sayi_2 + 1) if sayi_2 % i == 0]

    ortak_bolenler = list(set(sayi_1_bolen) & set(sayi_2_bolen))
    return max(ortak_bolenler)

while True:
    sayi_1 = input("Birinci Sayıyı Giriniz: ")
    sayi_2 = input("İkinci Sayıyı Giriniz: ")


    if sayi_1 == "q":
        print("Program Sonlandırılıyor...")
        break
    else:
        sayi_1 = int(sayi_1)
        sayi_2 = int(sayi_2)

        print(f"EBOB({sayi_1}, {sayi_2}) = {Ebob(sayi_1, sayi_2)}")

print(f"""
Hocanın Çözümü
{"-" * 80}
def ebob_bulma(sayı1,sayı2):
    
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2 ):

        if ( not (sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob
sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ebob:",ebob_bulma(sayı1,sayı2))
{"-" * 80}
""")

