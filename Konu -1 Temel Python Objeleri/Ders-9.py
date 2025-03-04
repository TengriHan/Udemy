# İnput - Kullanıcıdan girdi alma,
space = "---------------------------------------------------"

print("İnput değer alma")
sayı_1 = input("Lütfen 1. Sayıyı Giriniz: ")
print("Kullanıcının Girdiği 1. Sayı: ", sayı_1)

""" 
İnputtan dönen değer string gelir bu sebeple *3 gibi bir 
işlemde integer olmadığından matematiksel işlem yapmaz. 
Değeri integer yapmamız gerekiyor"""
print("Hatalı kullanım input değer String olarak algılanıyor")
print("Sayı 1'in  3 ile çarpılmışı",sayı_1 * 3)
print(type(sayı_1))
print(space)

print("Doğru Kullanım input değer integer olarak algılanıyor")
sayı_2 = int(input("Lütfen 2. sayıyı giriniz: "))
print("Kullanıcının girdiği 2. Sayı", sayı_2)
print("Sayı 2'nin 3 ile çarpılmışı: ", sayı_2 * 3)
print(type(sayı_2))
print(space)

# Kullanıcıdan 3 farklı sayı alıp toplamını ekrana yazdırma.
a = int(input("1. Sayı Giriniz: "))
b = int(input("2. Sayı Giriniz: "))
c = int(input("3. Sayı Giriniz: "))

toplam = a + b + c

print("Kullanıcıların girdiği sayıların toplamı: ", a + b + c)
print("Kullanıcının girdiği sayıların toplamı: ", toplam)

print(space)

isim = input("Lütfen İsminizi Girin: ")
print("Merhaba", isim)
