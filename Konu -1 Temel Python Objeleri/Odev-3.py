"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın.
Sürücünün toplam ne kadar ödemesi gerektiğini hesaplayın.
"""

kilometre_yakma = float(input("Araç kilometrede ne kadar yakıyor : "))
yapılan_kilometre = float(input("Kaç km yol gidildi: "))

hesap = kilometre_yakma * yapılan_kilometre

print("100 Kilometrede: {:.2f} yakıyor \nGidilen Kilometre: {:.2f} \nÖdenmesi gereken tutar: {:.2f} TL ".format(kilometre_yakma, yapılan_kilometre, hesap))

