"""
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""

sayi_1 = int(input("1. Sayıyı Giriniz: "))
sayi_2 = int(input("2. Sayıyı Giriniz: "))

print("Kullanıcıdan alınan \n1. Sayı: {} \n2. Sayı: {}".format(sayi_1, sayi_2))

sayi_1_güncel = sayi_2
sayi_2_güncel = sayi_1

print("Güncel 1. Sayı: {} \nGüncel 2. Sayı: {}".format(sayi_1_güncel, sayi_2_güncel))