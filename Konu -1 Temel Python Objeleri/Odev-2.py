"""
Kullanıcıdan alınan boy ve kilo değerlerine göre kullanıcın beden
kitle indeksini bulunuz.
"""

# Kilo / Boy(m) * Boy(m)

kilo = float(input("Kilonuzu Giriniz: "))
boy = float(input("Boyunuzu (m) Giriniz: "))

kilo_boy_indeksi = kilo / (boy ** 2)

print("Kilo boy indeksiniz: ", kilo_boy_indeksi)
print("Kilonuz: {} \nBoyunuz: {} \nKilo Boy İndeksiniz: {}".format(kilo, boy, kilo_boy_indeksi))

