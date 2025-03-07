print("""
----------------------------------------------------------------------
Bir dairenin alanını ve çevresini hesaplayan program.
----------------------------------------------------------------------
""")

p = 3.14
r = int(input("Yarıçap giriniz: "))

cevre = (2 * p) * r

alan = p * (r ** 2)

print("Dairenin çevresi: {} \nDairenin Alanı: {}".format(cevre, alan))