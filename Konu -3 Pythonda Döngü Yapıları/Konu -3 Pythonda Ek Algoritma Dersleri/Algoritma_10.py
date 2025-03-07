print("""
------------------------------------------------------------------
Kullanıcıdan ismini ve soyadını alarak içersinde
kaç adet sesli ve sessiz harf olduğunu bulan program
------------------------------------------------------------------
""")

isim = input("İsim Giriniz:")
soyad = input("Soyad Giriniz:")
ad_soyad = ("{} {}".format(isim, soyad))
print("Ad Soyad: {}".format(ad_soyad))
sesli_harf = "aeıioöuü"
sesli_harf_sayaci = 0
sessiz_harf = "z, y, v, t, ş, s, r, p, n, r, m, l, k, h, j, ğ, g, d, ç, c, b"
sessiz_harf_sayaci = 0

for harf in ad_soyad:
    if harf in sesli_harf:
        sesli_harf_sayaci += 1
    elif harf in sessiz_harf:
        sessiz_harf_sayaci += 1

print("Sesli harf Sayısı: ", sesli_harf_sayaci)
print("Sessiz Harf Sayısı: ", sessiz_harf_sayaci)
