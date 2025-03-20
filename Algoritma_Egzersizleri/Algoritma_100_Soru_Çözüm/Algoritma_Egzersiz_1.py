print("""
--------------------------------------------------------------------------------
Klavyeden girilen 5 adet not bilgisinin ortalamasını alan program yapınız.
--------------------------------------------------------------------------------
""")
#Furkan Çözüm
note_1 = int(input("Birinci notu giriniz: "))
note_2 = int(input("İkinci notu giriniz: "))
note_3 = int(input("Üçüncü notu giriniz: "))
note_4 = int(input("Dördüncü notu giriniz: "))
note_5 = int(input("Beşinci notu giriniz: "))

ortalama = (note_1 + note_2 + note_3 + note_4 + note_5) / 5

print("""
Girilen Notlar:
Not 1: {}
Not 2: {}
Not 3: {}
Not 4: {}
Not 5: {}
Ortalama: {}
""".format(note_1, note_2, note_3, note_4, note_5, ortalama))

print("------------------------------------------------------------")
#Chatgpt ile kısaltılmış Çözüm

notlar = [int(input(f"{+1}. notu giriniz: ")) for i in range(5)]
ortalama_2 = sum(notlar) / len(notlar)

print("\nGirilen Notlar:", notlar)
print(f"Orttalama: {ortalama_2:.2f}")