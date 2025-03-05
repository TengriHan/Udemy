"""
Mantıksal Bağlaçlar
İki veya daha fazla koşulu kontrol ediyorsak kullanılır.
"""

space = "----------------------------"

"""
and Operatörü bütün karşılaştırma işlemlerinin sonucunun True olmasına bakar. Bir tanesi bile farklıysa False çıkar.
"""
print("and Operatörü")
print(1 < 2)
print("Murat" == "Murat")
print(1 < 2 and "Murat" == "Murat")
print(1 < 2 and "Murat" == "Mehmet")
print(1 > 2 and "Murat" == "Mehmet")
print(1 < 2 and "Araba" == "Zula" and "Mehmet" == "Murat")

print(space)

"""
or operatörü en az birinin True olmasına bakar. En az bir tanesi True ise True çıkar hiçbiri True değilse False çıkar.
"""
print("or Operatörü")
print(1 < 2 or "Mehmet" == "Murat")
print(1 < 2 or "Mehmet" == "Mehmet")
print(1 > 2 or "Mehmet" == "Murat")
print(1 < 2 or "Araba" < "Zula" or "Mehmet" == "Murat" or 1.2 > 0.6)

print(space)

"""
not operatörü karşılaştırma işleminin tam tersi sonuca çevirir. 
Yani True olan bir sonucu False, False olan sonucu True yapar
"""
print("not Operatörü")
print(2 == 2)
print(not 2 == 2)
print("Mehmet" == "Murat")
print(not "Mehmet" == "Murat")

print(space)

"""Bu 3 operatörü beraber kullanılabilri ama karmaşıklığa yol açabileceği için parantez kullanabiliriz"""
print("3 operatörü aynı anda kullanma")
print(not (2.14 > 3.49 or (2 != 2 and "Murat" == "Murat")))
print("Araba" < "Zula" and ("Bebek" < "Çocuk" or (not 12 == 13)))