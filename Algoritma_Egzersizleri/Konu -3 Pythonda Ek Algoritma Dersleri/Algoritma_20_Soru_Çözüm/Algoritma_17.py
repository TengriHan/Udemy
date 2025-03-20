import random

print("""
----------------------------------------------------------
Kullanıcının girdiği mXn boyutta bir matris oluşturup
bu matrisi rastgele sayılarla doldurunuz. Bu matrisin
transpozesini oluşturunuz.
----------------------------------------------------------
""")

satir = int(input("Satır Sayısını Giriniz: "))
sutun = int(input("Sütun Sayısını Giriniz: "))

matris_1 = [[0 for x in range(sutun)] for y in range(satir)]
matris_transpoze = [[0 for x in range(satir)] for y in range(sutun)]

for i in range(satir):
    for j in range(sutun):
        matris_1[i][j] = random.randint(0, 9)
        matris_transpoze[j][i] = matris_1[i][j]

print(matris_1)
print(matris_transpoze)

