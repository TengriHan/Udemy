"""
Kullancının girdiği vize1, vize2, final notlarına göre harf notu hesaplayın

Vize 1 toplam notu %30'una etki edecek
Vize 2 toplam notu %30'una etki edecek
Final toplam notu %40'una etki edecek

    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""

note_1 = int(input("Birinci notu giriniz: "))
note_2 = int(input("İkinci notu giriniz: "))
note_3 = int(input("Üçüncü notu giriniz: "))

vize_1 = (note_1 * 30) / 100
vize_2 = (note_2 * 30) / 100
final = (note_3 * 40) / 100

toplam_not = vize_1 + vize_2 + final

if toplam_not >= 90:
    print("AA")
elif toplam_not >= 85:
    print("BA")
elif toplam_not >= 80:
    print("BB")
elif toplam_not >= 75:
    print("CB")
elif toplam_not >= 70:
    print("CC")
elif toplam_not >= 65:
    print("DC")
elif toplam_not >= 60:
    print("DD")
elif toplam_not >= 55:
    print("FD")
else:
    print("FF")