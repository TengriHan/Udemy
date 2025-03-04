# Print fonksiyonu ve formatlama
from PIL.ImagePalette import sepia

space = "------------------------------------------"

print(35)
print(space)

print(3.14)
print(space)

print("Furkan")
print(space)

a = 4
b = 3
print(a + b)
print(space)

print("Furkan'ın bugün dersi var.")
print(space)

print(35, 4.54, "Merhaba", "Python")
print("Rabia", "Furkan", "Tengri")
print(space)

#Alt alta yazdırma \n
print("Merhaba \nNasılsın \nİyi misin?")
print(space)

#Bir tab boşluk Bırakma \t
print("Merhaba, \t iyi misin?")
print("Ocak \t Şubat \t Mart")
print(space)

#type fonksiyonu print içerisine gönderilen değerin tipinin ne olduğunu gösterir
a = 4
b = "Furkan"
c = 4.44
print(type(a))
print(type(b))
print(type(c))
print(space)

# sep parametresiyle aradaki boşlukları istediğimiz şekilde kullanabiliyoruz
print(35, 45, 54, 75)
print(35, 45, 54, 75, sep="/")
print(space)

print("Furkan", "Rabia", "Tengri", sep="\n")
print("06", "04", "2025", sep="/")
print(space)

# Karakterleri ayırmak için *
print("Python")
print(*"Python")

print(*"TBMM", sep=".")
print(space)

#Formatlama detaylı bilgi için https://pyformat.info/ sitesini ziyaret edebilirsiniz.
a = 3
b = 4
print("{} + {} 'nin toplamı {}'dır".format(3.15, 4.12, 7.321))