"""
Metodlar

Metodlar bir obje üzerinde belli işlemleri gerçekleştiren objeler
obje.herhangi_bir_metod(değerler(opsiyonel))
"""

a = [1, 2, 3, 4, 5]
print(type(a))
print(a)

print("Seçilen indeksten sonra veri ekleme")
a.insert(1, "Murat")

print(a)

print("Listenin sonuna veri ekleme")
a.append("Deneme")
print(a)

print("Son Veriyi Silme")
a.pop()
print(a)

print("Metodun ne iş yaptığını öğrenmek isterseniz")
help(a.append)