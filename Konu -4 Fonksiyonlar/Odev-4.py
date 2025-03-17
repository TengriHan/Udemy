print(f"""
{"-" * 80}
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
Örnek: 97 Doksan Yedi
{"-" * 80}
""")

birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayi):
    birinci = sayi % 10
    ikinci = sayi // 10


    return onlar[ikinci] + " " + birler[birinci]

sayi = int(input("Sayı: "))
print(okunus(sayi))