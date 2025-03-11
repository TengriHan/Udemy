print("""
----------------------------------------------------------------------------
Vize notunun %40'ını Final Notunun %60'ını alarak ortalama notu hesaplayan,
ortalama 50'den büyükse "Geçti" küçükse "Kaldı" yazan program.
----------------------------------------------------------------------------
""")

vize = int(input("Vize Notunu giriniz: "))
final = int(input("Final Notunu giriniz: "))

ortalama = ((vize * 40) / 100) + ((final * 60) / 100)
print("Ortalama: ", ortalama)
if ortalama < 50:
    print("Kaldınız...")
else:
    print("Geçtiniz...")