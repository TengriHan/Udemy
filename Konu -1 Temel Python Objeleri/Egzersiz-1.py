# Oyuncu Kaydetme Programı
print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı: ")
soyad = input("Oyuncunun Soyadı: ")
takım = input("Oyuncunun Takımı: ")

bilgiler = [ad, soyad, takım]

print("Bilgiler kaydediliyor....")

print("Oyuncu Adı: {} \nOyuncunun Soyadı: {} \nOyuncunun Takımı: {}".format(bilgiler[0], bilgiler[1], bilgiler[2]))
print("Bilgiler Kaydedildi.")