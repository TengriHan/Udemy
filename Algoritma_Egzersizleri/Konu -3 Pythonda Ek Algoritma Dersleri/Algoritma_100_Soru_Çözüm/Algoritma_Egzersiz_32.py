print(f"""
{"-" * 80}
Kullanıcıdan alınan basamak sayısı kadar Pascal üçgeninin basamaklarını hesaplayan kod.
{"-" * 80}
""")

basamak = int(input("Kaç basamaklı Pascal üçgeni istiyorsunuz? "))

ucgen = [[1]]

for i in range(1, basamak):
    satir = [1]
    onceki_satir = ucgen[i - 1]

    for j in range(len(onceki_satir) - 1):
        satir.append(onceki_satir[j] + onceki_satir[j + 1])

    satir.append(1)
    ucgen.append(satir)

for satir in ucgen:
    print(" ".join(map(str, satir)).center(basamak * 4))
