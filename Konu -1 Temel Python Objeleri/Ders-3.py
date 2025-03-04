# Karakter Dizileri (Stringler)
space = "-------------------------------------------"
print("3 Farklı String oluşturma")
print("Furkan Bayraktar")

print('Furkan Bayraktar')

print("""Furkan Bayraktar""")

print(space)

# Birden fazla Tırnak kullanımı.
print("Furkan'ın bugün dersi var")
print("""Furkan Rabia'ya "Nasıl bunu yaparsın" diye söylendi. """)
print(space)

x = "Merhaba"
print(x)
print(space)

# String İndeksleme ve Parçalama
""" 
Örnek "ali" stringi a, l ve i karakterlerinden oluşur yerleri 
indeks olarak adlandırılır. İndeksleme 0'dan başlar
"""
print("String İndeksleme")
a = "ali"
print(a[0])
print(a[1])
print(a[2])

print("Geriden indeksleme")
print(a[-1])
print(a[-2])
print(a[-3])

print(space)

# [Başlama indeksi : Bitiş İndeksi : Atlama Değeri]
print("String Parçalama")
b = "Python Programlama Dili"
print(b)
print(b[4: 10])
print(b[4: 10: 2])
print(b[:10])
print(b[4:])
print(b[:])

print(b[:-1])
print(b[::2])
print(b[::-1])

print(space)

#String Uzunluğu Bulma "len"
print("String Uzunluğu")
string = "Merhaba"
print(len(string))
print(space)

# Değişken olarak Stringleri toplama
k = "Python "
j = "Programlama "
l = "Dili"
print(k + j +l)
print(k * 3)