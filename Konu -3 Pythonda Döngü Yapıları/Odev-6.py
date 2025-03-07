"""
Buradaki problemin çözümünü derslerimzde özellikle öğrenmedik. Burada mantık yürüterek ve list
comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye
atmaya çalışın.
Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da
öğrendiğimiz şeyler olur. Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu
durumlarla kullanımını öğreneceksiniz.
"""


liste = [i for i in range(1, 100)]

for i in liste:
    if i % 2 == 0:
        print(i)


liste_2 = [x for x in range(1,101) if x % 2 == 0]

print(liste_2)