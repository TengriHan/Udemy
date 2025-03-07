print("""
----------------------------------------------------------------
3x3 rastgele sayılardan oluşan 2 matris oluşturun.
Bu matrislerin toplamını hesaplayın.
----------------------------------------------------------------
""")

import random

matris_1 = [[0 for x in range(3)] for y in range(3)]
matris_2 = [[0 for x in range(3)] for y in range(3)]
matris_toplam = [[0 for x in range(3)] for y in range(3)]


print("1. Matris: {}\n2. Matris: {}\nMatrislerin Toplamı: {}".format(matris_1, matris_2, matris_toplam))

print("Rastgele Sayılarla doldurma")
for i in range(3):
    for j in range(3):
        matris_1[i][j] = random.randint(0, 5)
        matris_2[i][j] = random.randint(0, 5)
        matris_toplam[i][j] = matris_1[i][j] + matris_2[i][j]
print("1. Matris: {}\n2. Matris: {}\nMatrislerin Toplamı: {}".format(matris_1, matris_2, matris_toplam))
