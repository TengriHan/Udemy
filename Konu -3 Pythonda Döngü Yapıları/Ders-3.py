"""
Range fonksiyonu
"""
space = "----------------------------------"
print("""
-----------------------------------
Range fonksiyonu
-----------------------------------
""")
print("Range kullanım türleri")
print("Yanlış Kullanım")
print(range (0, 20))

print("Doğru Kullanım")
print(*range (0, 20))

print(*range (1, 20))

print(*range (15))

print("Atlayarak kullanım")
print(*range (5, 100, 5))

print("Tersten çalıştırma")
print(*range(20, 0, -1))

print(space)
print("Normalde yaptığımız listeyi hazır verip for ile gezmek")
liste = [1, 2, 3, 4, 5]
liste_1 = []
for i in liste:
    print(i)

print(space)

for i in range (1, 10):
    print(i)

print(space)

print("Yıldız üçgen")
for i in range (1, 10):
    print("*" * i)
