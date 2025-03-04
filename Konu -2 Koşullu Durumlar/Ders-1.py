# Mantıksal Değerler ve Karşılaştırma Operatörleri
# Mantıksal Değerler (Boolean)
# 2 değere sahiptirler True ve False
space = "---------------------------------------"

print("Boolean'ların veri tipleri")
a = True
print(type(a))

b = False
print(type(b))

print(space)

# Pythonda bir sayı değeri eğer 0'dan farklıysa True 0 ise False bool fonksiyonuyla dönüştürme yaparak görebiliriz.
print("Sayı değerine göre True False kontrolü")
print(bool(12.4))
print(bool(0.3))
print(bool(0))
print(bool(-121))

print(space)

# Bir sayıyla başka sayıyı kontrol etmek istersek
print(1 == 1)
print(1 == 2)

print(space)

# Bir değişkenin değerini sonradan belirlemek isterseniz None kullanırsanız veriyi sonradan değiştirebilirisiniz.
bos_deger = None
print(bos_deger)
print(space)

"""
Karşılaştırma Operatörleri
== İki değerin eşit olup olmadığını kontrol eder eğer 2 == 2 ise True 2 == 1 ise False
!= İki değer birbirine eşit değilse 2 != 1 True 2 != 2 False
> Soldaki değer sağdaki değerden büyük ise 3 > 2 True 3 > 5 False
< Soldaki değer sağdaki değerden küçük ise 3 < 5 True 3 < 2 False
>= Soldaki değer sağdaki değerden büyükse veya sağdaki değere eşitse 3 >= 2 True 3 >= 3 True 3 >= 5 False
<= Soldaki değer sağdaki değerden küçükse veya sağdaki değere eşitse 4 <= 5 True 4 <= 4 True 4 <= 3 False
"""
print("İki isim aynı mıdır?")
print("Mehmet" == "Mehmet")
print("Mehmet" == "Murat")

print("İki isim aynı farklı mıdır?")
print("Mehmet" != "Murat")

print("İki liste aynı mıdır?")
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] == [1, 2, 3, 4])

print("2 küçük müdür 4'ten")
print(2 < 4)

print("2.4 <= 1.8 midir?")
print(2.4 <= 1.8)