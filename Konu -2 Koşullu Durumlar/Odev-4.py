"""
Şimdi de geometrik şekil hesaplama işlemi yapalım.
İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi ,
dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı ,
eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın.
Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için,
Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
abs(-4)
4
abs(5)
5

*Not: Bu problem sizin algoritma kurma becerinizi bir hayli geliştirecektir.*


"""

şekil = input("Hangi Şekli Öğrenmek istiyorsunuz? ")

if şekil == "Dörtgen":
    print("Kenarları Sırasıyla Giriniz:")
    kenar_1 = int(input("Birinci Kenarı Giriniz: "))
    kenar_2 = int(input("İkinci Kenarı Giriniz: "))
    kenar_3 = int(input("Üçüncü Kenarı Giriniz: "))
    kenar_4 = int(input("Dördüncü Kenarı Giriniz: "))
    if kenar_1 == kenar_2 == kenar_3 == kenar_4:
        print("Kare")
    elif kenar_1 == kenar_3 and kenar_2 == kenar_4:
        print("Dikdörtgen")
    else:
        print("Sıradan Dörtgen")

elif şekil == "üçgen":
    print("Kenarları Sırasıyla Giriniz")
    kenar_1 = int(input("Birinci Kenarı Giriniz: "))
    kenar_2 = int(input("İkinci Kenarı Giriniz: "))
    kenar_3 = int(input("Üçüncü Kenarı Giriniz: "))
    if abs(kenar_1 + kenar_2) > kenar_3 and abs(kenar_1 + kenar_3) > kenar_2 and abs(kenar_2 + kenar_3) > kenar_1:
        if kenar_1 == kenar_2 and kenar_1 == kenar_3:
            print("Eşkenar üçgen")
        elif (kenar_1 == kenar_2 and kenar_1 != kenar_3) or (kenar_1 == kenar_3 and kenar_1 != kenar_2) or (kenar_2 == kenar_3 and kenar_2 != kenar_1):
            print("İkizkenar Üçgen")
        else:
            print("Çeşitkenar Üçgen")

    else:
        print("Geçersiz Şekil")
