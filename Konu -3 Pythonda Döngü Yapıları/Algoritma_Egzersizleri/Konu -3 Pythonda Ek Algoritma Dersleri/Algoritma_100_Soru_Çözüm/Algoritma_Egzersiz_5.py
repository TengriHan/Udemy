print("""
-----------------------------------------------------------
30 kişilik sınıfta yaşı 13 ile 15 arasında olanların 
sayısını bulan programı yazınız
-----------------------------------------------------------
""")
#Furkan Çözüm
yas = [int(input(f"{i + 1} Yaş Giriniz: ")) for i in range(30)]
aralik = []

for i in yas:
    if 13 <= i <= 15:
        aralik.append(i)

print("13 ile 15 yaş aralığında olan öğrenci sayısı:", len(aralik))

"""
ChatGpt Çözüm
---------------------------------------------------------------------------
yas = [int(input(f"{i+1}. Yaşı Giriniz: ")) for i in range(30)]

# 13 ile 15 yaş arasında olanların sayısını direkt hesapla
kac_kisi = sum(1 for i in yas if 13 <= i <= 15)

print(f"\n13 ile 15 yaş aralığında olan öğrenci sayısı: {kac_kisi}")
----------------------------------------------------------------------------
"""