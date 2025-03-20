print(f"""
{"-" * 80}
Nesne Tabanlı Programlama - Özel Metodlar
Özel metodların çoğu biz tanımlamasak bile her classa ait metodlardır. 
Örnek init
{"-" * 80}
""")


print("Biz tanımlamasak bile var olan metodlar")
class Kitap():
    pass

# __init__ metodu
kitap = Kitap()

# __str__ metodu
print(kitap)

# __del__ metodu
del kitap
# print(kitap) hata verecektir.

print(f"{"-" * 80}")

class Kitaplar():
    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        print("İnit Fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

    def __str__(self):
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTürü: {}".format(self.isim, self.yazar, self.sayfa_sayisi, self.tur)

    def __len__(self):
        return self.sayfa_sayisi

    def __del__(self):
        print("Kitap objesi siliniyor...")

kitap = Kitaplar("İstanbul Hatırası", "Ahmet Ümit", 561, "Polisiye")

print(f"Kitap içeriği STR fonksiyonuyla kullanım \n{kitap}")
print(f"Len fonksiyonuyla kitap objesinin sayfa sayısı. \n{len(kitap)}")

#Obje silme
del kitap
print(kitap)
