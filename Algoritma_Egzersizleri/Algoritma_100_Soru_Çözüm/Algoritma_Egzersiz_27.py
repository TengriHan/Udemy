print(f"""
{"*" * 80}
Öğrencilerine 12 haneli öğrenci numarası veren üniversitenin verdiği numaranın 
ilk 4 hanesi giriş yılı 
5. ve 6.  hanesi okuduğu fakültenin numarası 
7. ve 8. hane bölüm numarası 
9. hanesi öğrenim numarası 
11. ve 12. hane ise öğrencinin üniversiteye giriş sırasıdır. 
12 haneli öğrenci kodunu kullanıcıdan alarak anlamlı şekilde ayıran kodu yazınız.
{"*" * 80}
""")

numara = input("12 haneli okul numaranızı giriniz: ")

if len(numara) == 12:
    print(f"Okul numaranız {numara}")
    giris_yili = numara[0:4]
    fakulte_no = numara[4:6]
    bolum_no = numara[6:8]
    ogrenim_no = numara[8:9]
    giris_sirasi = numara[9:12]

    print(f"Giriş Yılı: {giris_yili}"
          f"\nFakulte No: {fakulte_no}"
          f"\nBolum No: {bolum_no}"
          f"\nOgrenim Turu: {ogrenim_no}"
          f"\nGiris Sirası: {giris_sirasi}")

else:
    print("Yanlış Girdiniz...")