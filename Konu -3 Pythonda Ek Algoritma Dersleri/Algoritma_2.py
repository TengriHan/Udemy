print("""
-----------------------------------------------------------------------------
Kullanıcıdan iki sayı alarak toplamını ve ortalamasını yazdıran program
-----------------------------------------------------------------------------
"""
)

sayi_1 = float(input("Birinci Sayıyı Giriniz: "))
sayi_2 = float(input("İkinci Sayıyı Giriniz: "))

toplam = sayi_1 + sayi_2
ortalama = toplam / 2

print("Birinci sayı: {}, İkinci Sayı: {} \nSayıların Toplamı: {} \nSayıların Ortalaması: {}"
      .format(sayi_1, sayi_2, toplam, ortalama))

