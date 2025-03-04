# Demetler (Tuplelar)
# Demetlerin listelerden farkı demetler asla değiştirilemez.
space = "-------------------------------------"

print("Tupleları yazdırma")
demet = (1, 2, 3, 4, 5, 6, 7)
print(type(demet))
print(demet)
print(demet[4])
print(demet[-1])
print(demet[0])
print(demet[:4])
print(demet[::-1])
print(space)

# Demetlerin sadece 2 fonksiyonu vardır.
print("Bir değerin kaç kere geçtiğini görme count")
demet2 = (1, 1, 1, 1, 2, 2, 2, 4, 5)
print(demet2)
print(demet2.count(1))
print(demet2.count(5))
print(demet2.count(15))
print(space)

# Değerin hangi indekste olduğunu bulma
print("Değerin indeksini bulma")
demet3 = ("Python", "PhP", "C", "Java")
print(demet3.index("Python"))
print(demet3.index("C"))
