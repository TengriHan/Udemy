"""
While Döngüleri
While döngüleri belli bir koşul sağlandığı sürece bloğundaaki işlemleri
gerçekleştirmeye devam eder.
Döngünün sona ermesi için bir süre sonra False olması gerekir.

while(koşul):
    İşlem-1
    İşlem-2
    İşlem-3
    ...
"""
space = "------------------------------------"
print("""
----------------------------------------------
While Döngüleri
---------------------------------------------
""")

i = 0
while i < 10:
    print("i'nin değeri:", i)
    i += 1

print(space)

x = 0
while x < 20:
    print("x'in değeri:", x)
    x += 2

print(space)

a = 0
while a < 40:
    print("Python öğreniyorum.")
    a += 1

print(space)

liste = [1, 2, 3, 4, 5]

for i in liste:
    print(i)

print(space)

index = 0

while index < len(liste):
    print("index: ",index,"Liste elemanı",liste[index])
    index += 1