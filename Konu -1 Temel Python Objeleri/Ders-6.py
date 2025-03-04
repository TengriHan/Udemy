# Listeler
# Liste içerisinde istediğiniz tipte veri saklayabilirsiniz.
# Liste oluşturma
space = "------------------------------"

print("Liste Oluşturma")
liste = [3, 4, "Elma", 5, 6]
listx = []

print(liste)
print(listx)
print(type(liste))
print(space)

# Farklı şekilde liste oluşturma
print("Liste Oluşturma")
listex = list()
print(listex)
print(space)

# Liste içindeki eleman sayısı
print("Liste içerisindeki eleman sayısı")
liste2 = [1,2,3,4,5,6]
print(len(liste2))
print(space)

# Liste içerisindeki değerleri parçalama
liste3 = list("Merhaba")
print(liste3)
print(len(liste3))
print(space)

# İndeksleme ve Parçalama
liste4 = [5, 6, 7, 8, 9, 10, 11]
print("Liste Parçalama")
print(liste4[3])
print(liste4[-1])
print(liste4[0])

# Listedeki eleman sayıları
print("Eleman Sayıları")
print(len(liste4) -1)
print(space)

print("Liste Sayma")
print(liste4[2:])
print(liste4[:5])
print(liste4[0::2])
print(liste4[2:6:3])
print(space)

# Listeler stringler gibi birbiriyle toplanabilir.
print("Liste Toplama")
liste5 = [1, 2, 3]
liste6 = [4, 5, 6]
listetoplam = liste5 + liste6
print(listetoplam)
print(space)

# Liste içeriğini çarpma
print("Liste içeriğini çarpma")
liste7 = [11, 12, 13]
listecarpma = liste7 * 3
print(listecarpma)
print(space)

# Liste elamanları değiştirilebilri
print("Liste Elemanı değiştirme")
liste8 = ["deneme", 1, 2, 5, 6]
print(liste8)
liste8[1] = 11
print(liste8)

liste8[:2] = ["At", 121]
print(liste8)
print(space)

# Metotlar
print("Liste metotları 1 - Append")
liste_metot = ["deneme", 14, 15, 16, 17, 121, 13]
print(liste_metot)

# append metotu ekleme
print("Listeye veri ekleme")
liste_metot.append("Python")
print(liste_metot)
liste_metot.append(12)
print(liste_metot)

# pop liste içerisindeki elemanı atma eğer () içerisine hiçbir değer girilmezse son eleman atılır.
print("Listenin elamanını silme")
liste_metot.pop()
print(liste_metot)
liste_metot.pop(1)
print(liste_metot)
print(space)

# Liste elemanlarını sıralama .sort
print("Liste elemanlarını sıralama")
liste_metot_2 = [100, 11, 2, 565, 21, 13, 151]
print(liste_metot_2)
liste_metot_2.sort()
print(liste_metot_2)

print("Liste elmanlarını tersten sıralama .sort(reverse = True)")
liste_metot_2.sort(reverse = True)
print(liste_metot_2)

# Eğer String ise alfabetik olarak sıralanır
print("Stringleri .sort metoduyla sıralama Alfabetik olarak")
liste_metot_3 = ["PhP", "Python", "C", "Deneme"]
print(liste_metot_3)
liste_metot_3.sort()
print(liste_metot_3)
liste_metot_3.sort(reverse = True)
print(liste_metot_3)
print(space)

# Liste içinde liste
liste_metot_4 = [[1,2],[3,4], [5,6]]
print(liste_metot_4)
print(liste_metot_4[1])
print(liste_metot_4[1][1])