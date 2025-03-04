# Matematik Operatörleri
space = "------------------------------------------"
# Önceki Dersin Tekrarı
print("Ders tekrarı")
k = 34
l = 45
m = 54
print(k + l + m)
print(k * l *m)
print(k / l)
print(space)

i = 3.4
j = 4.3

print(i + j)
print(i / j)
print(space)

# Tam Sayı Bölmesi (//) Ondalık kısımı atar ve tam sayı verir.
print("Tam Sayı Bölmesi // Kullanımı")
a = 345
b = 36
print(a / b)
print(a // b)
print(space)

print(22.7 / 11.4)
print(22.7 // 11.4)
print(space)


# Kalanı Bulma (%) Bir Sayıyı başka sayıya böldüğümüzde kalanı bulmamızı sağlar.
print("Kalan Bulma % kullanımı")
print(13 % 4)
print(a % b)
print(4 % 2)
print(space)

# Üs bulma (**)
print("Üs Bulma Kullanımı **")
print(2 ** 4)
print(3 ** 6)
print(space)

# Karakök bulmamızı da sağlar.
print("Karekök Kullanımı **")
print(64 ** 0.5)
print(25 ** 0.5)
print(space)

# Küp Kökünü de alabiliriz
print("Küp Kök bulma Kullanımı")
print(8 ** (1/3))
print(space)

# İşaret değiştirme
print("İşaret Değiştirme")
a = -4
print(a)
print(-a)
print(+a)
print(space)

# İşlem önceliği
# 1 - Parantez içi her zaman önce yapılır.
# 2 - Çarpma ve bölme her zaman Toplama ve Çıkarma işlemlerine göre önce yapılır.
# 3 - İşlemler soldan sağa değerlendirilir.
print("İşlem Önceliği")
print(8 + 4 * 3 / 2 - 18)
print(8 + ((4 * 3) / 2) - 18)
print((8 + 4) * 3 / 2 - 18)

# Quiz Sorusu
print(((10 ** 2) //3) / 3)