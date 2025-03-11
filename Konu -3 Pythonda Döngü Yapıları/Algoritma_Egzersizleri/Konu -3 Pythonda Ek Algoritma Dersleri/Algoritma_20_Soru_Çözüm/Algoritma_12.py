print("""
---------------------------------------------
0 ile 1000 arasındaki Asal sayıları bulan
programı yazınız.
---------------------------------------------
"""
)
bolen_sayac = 0

for j in range(3, 1000):
    bolen_sayac = 0
    for i in range(2, j):
        if j % i == 0:
            bolen_sayac += 1

    if bolen_sayac == 0:
        print(j)