"""
Kullanıcı girişi
"""

print("""
------------------------------------------------
Kullanıcı Girişi
------------------------------------------------
""")

sys_kullanici_adi = "tengrihan"
sys_parola = "12345"

kullanici_adi = input("Kullanıcı Adı Giriniz: ")
parola = input("Parola: ")

if kullanici_adi == sys_kullanici_adi and sys_parola != parola:
    print("Parola Hatalı!")
elif kullanici_adi != sys_kullanici_adi and parola == sys_parola:
    print("Kullanıcı Adı Hatalı!")
elif kullanici_adi != sys_kullanici_adi and parola != sys_parola:
    print("Kullanıcı Adı ve Parola Hatalı!!!")
else:
    print("Sisteme Başarıyla Giriş Yapıldı.")
