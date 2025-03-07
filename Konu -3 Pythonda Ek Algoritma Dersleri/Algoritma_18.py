print("""
-------------------------------------------------------------------
Kullanıcıdan alınan 4 basamaklı bir sayıyı yazı ile yazınız.
Kullanıcı 3215 girmiş olsun "üç bin iki yüz on beş" ekrana yazılsın.
-------------------------------------------------------------------
""")

birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
yuzler = ["", "yüz", "iki yüz", "üç yüz", "dört yüz", "beş yüz", "altı yüz", "yedi yüz", "sekiz yüz", "dokuz yüz"]
binler = ["", "bin", "iki bin", "üç bin", "dört bin", "beş bin", "altı bin", "yedi bin", "sekiz bin", "dokuz bin"]

sayi = int(input("Dört Basamaklı Bir sayı giriniz: "))

sayi_string = str(sayi)

print(binler[int(sayi_string[0])], yuzler[int(sayi_string[1])], onlar[int(sayi_string[2])], birler[int(sayi_string[3])])