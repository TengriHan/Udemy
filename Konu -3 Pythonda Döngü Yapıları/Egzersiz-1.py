print("""
-------------------------------------------------
Kullanıcı Girişi Programı
-------------------------------------------------
""")

sys_kullanici_adi = "tengrihan"
sys_parola = "12345"
giris_hakki = 3
while True:
    kullanici_adi = input("Kullanıcı Adı Giriniz:")
    parola = input("Parola Giriniz:")
    if kullanici_adi != sys_kullanici_adi and parola == sys_parola:
        print("Kullanıcı Adı Hatalı")
        giris_hakki -=1
    elif kullanici_adi == sys_kullanici_adi and parola != sys_parola:
        print("Parola Hatalı")
        giris_hakki -=1
    elif kullanici_adi != sys_kullanici_adi and parola != sys_parola:
        print("Kullanıcı Adı ve Parola Hatalı")
        giris_hakki -=1
    else:
        print("Sisteme Giriş Başarılı")
        break
    if giris_hakki == 0:
        print("Giriş Hakkınız Kalmamıştır...")
        break