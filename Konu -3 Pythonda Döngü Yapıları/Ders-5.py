"""
List Comprehension
"""
space = "-------------------------------------"
print("Listeye veri ekleme hatırlatma")
liste = [1, 2, 3, 4]
print(liste)
liste.append(5)
print(liste)

print(space)

print("For döngüsü kullanarak boş listeye veri ekleme")
liste_1 = [1, 2, 3, 4, 5]
liste_2 = list()

for i in liste_1:
    liste_2.append(i)
print(liste_2)

print(space)

print("""
-------------------------------------------------
List Comprehension Kullanımı
-------------------------------------------------
""")
liste_3 = [1, 2, 3, 4, 5]
liste_4 = [i for i in liste_3]
print(liste_4)

print(space)

liste_5 = [3, 4, 5]
print(liste_5)
liste_6 = [i * 2 for i in liste_5]
print(liste_6)

print(space)

liste_7 = [(1, 2), (3, 4), (5, 6)]
print(liste_7)
liste_8 = [i * j for i, j in liste_7]
print(liste_8)

print(space)

metin_1 = "Python"
print(metin_1)
metin_2 = [i * 3 for i in metin_1]
print(metin_2)

print(space)

print("List Comprehension Kullanmadan liste içindeki listeyi liste halinde farklı listeye ekleme")
liste_exercise = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]]
liste_exercise_1 = list()
for i in liste_exercise:
    print(i)

for i in liste_exercise:
    for x in i:
        liste_exercise_1.append(x)
print(liste_exercise_1)

print(space)
print("List comprehension Kullanarak liste içindeki listeyi boş listeye ekleme")
liste_exercise_2 = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]]
liste_exercise_3 = [x for i in liste_exercise_2 for x in i]
print(liste_exercise_3)