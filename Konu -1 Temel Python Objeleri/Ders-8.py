# Sözlükler - Dictionary
# Sözlükler anahtar ve değer
space = "---------------------------------------------"
print("Sözlük oluşturma")
sozluk1 = {"bir": 1, "iki": 2, "üç": 3, "dört": 4}
print(type(sozluk1))
print(sozluk1)

print("Boş Sözlük oluşturma")
sozluk2 = {}
print(sozluk2)
sozluk3 = dict()
print(sozluk3)

print(space)

print(sozluk1["bir"])
print(sozluk1["dört"])

# Sözlüğe eleman ekleme
print("Sözlüğe eleman ekleme")
sozluk1["beş"] = 5
print(sozluk1)
print(space)

sozluk4 = {"bir": [1, 2, 3, 4], "iki": [[1, 2], [3, 4], [5, 6]], "üç": 15}
print(sozluk4)
print(sozluk4["iki"])
print(sozluk4["iki"][1][1])

# Sözlük elemanı değiştirme
print("Sözlük Elemanı değiştirme")
sozluk1["üç"] = 112
print(sozluk1)
sozluk1["üç"] += 1
print(sozluk1)
print(space)

# İç içe sözlükler
sozluk5 = {"sayılar": {"bir": 1, "iki": 2, "üç": 3}, "meyveler":{"kiraz": "yaz", "portakal": "kış", "erik": "yaz"}}
print(sozluk5["sayılar"])
print(sozluk5["sayılar"]["iki"])

print(sozluk5["meyveler"])
print(sozluk5["meyveler"]["kiraz"])
print(space)

# Sözlük metotları
print(sozluk1)
print("Sözlük anahtalarını görmek için .keys")
print(sozluk1.keys())
print("Sözlük değerlerini görmek için .values")
print(sozluk1.values())
print("Sözlük itemlerini görebilmek için .items")
print(sozluk1.items())