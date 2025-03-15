print(f"""
{"-" * 80}
Kullanıcıdan alınan basamak sayısı kadar Pascal üçgeninin basamaklarını hesaplayan kod.
{"-" * 80}
""")

basamak = int(input("Kaç basamaklı Pascal üçgeni istiyorsunuz? "))

ucgen = [[1]]  # İlk satırı ekle

for i in range(1, basamak):
    satir = [1]  # Yeni satırın ilk elemanı 1
    onceki_satir = ucgen[i - 1]  # Önceki satırı al

    for j in range(len(onceki_satir) - 1):
        satir.append(onceki_satir[j] + onceki_satir[j + 1])  # Yeni elemanları ekle

    satir.append(1)  # Yeni satırın son elemanı da 1 olacak
    ucgen.append(satir)  # Pascal üçgenine ekle

# Pascal üçgenini ekrana yazdır
for satir in ucgen:
    print(" ".join(map(str, satir)).center(basamak * 4))
