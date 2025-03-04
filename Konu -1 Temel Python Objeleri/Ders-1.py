# Pythonda Sayı Veri Tipleri - Integer ve Float Veri tipleri

space = "----------------------------------------------------"
#Toplama
print(3 + 4)

print(space)
#Çıkarma
print(3 - 4)
print(space)


#Bölme
print( 9 / 3)
print(space)

#Çarpma
print(4 * 4 * 4)
print(space)

#Değişken ismi ve Değişken Değeri
furkan = 10
print(furkan)
print(space)

print(furkan * furkan * furkan)
print(space)

a = 4
b = 3
c = a + 2 * b
print(c)
print(space)

# 1 - Değişken isimleri bir sayıyla başlayamaz
# 2 - Değişken ismi kelimelerden oluşuyorsa boşluk olamaz.
# 3 - :'",<>()!@^$%^&*-+ Semboller değişken ismi içerisinde kullanılamaz. (Sadece _ sembolü kullanılabilir)
# 4 - Pythonda tanımlı anahtar kelimeler değişken ismi olarak kullanılamaz. (while, not vs.)


pi_sayisi = 3.14
cap = 4
cevre = pi_sayisi * cap
print(cevre)
print(space)


x = 4
y = 3
print(x)
print(y)
print(space)
#Değerleri değiştirme
x, y = y, x

print(x)
print(y)
print(space)


#Değeri arttırma azaltma vb.
i = 5
i = i + 1
print(i)
# İki kullanımda kabul edilebilir ama += daha verimli bir kullanım türüdür
i += 1
print(i)
print(space)

b = 3
b *= 4
print(b)