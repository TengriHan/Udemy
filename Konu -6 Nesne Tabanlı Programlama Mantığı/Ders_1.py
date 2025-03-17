print(f"""
{"-" * 80}
Object Oriented Programming en basit anlamıyla gerçek hayatı programlamaya uyarlamak
olarak düşünülebilir. Örneğin bir tane öğrenci otomasyon sistemi yazmak istiyoruz.
Bunun için öğretmenleri, öğrencileri ve kursları aslında birer nesne olarak oluşturmamız
gerekiyor. Böyle bir sistemi programlamayla gerçekleştirmek için aslında her bir nesnenin
yapısını tanımlayıp, daha sonra bu yapılardan nesneler üretmemiz gerekiyor.
{"-" * 80}
""")
# Liste Objesi
liste = [1, 2, 3, 4, 5]
print(liste)

#Listeye veri ekleme
liste.append(6)
print(liste)

def toplama(a, b):
    return a + b

print(type(toplama))

print("Bunların hepsi birer objedir.")
