"""
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
Ekrana yazdırma işlemini "format" metoduyla yapmaya çalışın.
"""

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

carpim = a * b * c

print("Değişkene atayarak çarpma:", carpim)
print("1. Sayı: {} \n2. Sayı: {} \n3. Sayı: {} \nSayıların çarpımı: {} \n".format(a, b, c, a*b*c))


