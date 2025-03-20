print(f"""
{"-" * 80}
Kullanıcıdan kısa ve uzun kenar 
bilgisini aldığı dikdörtgenin alan ve çevre hesaplamasını yapan kodu yazınız.
{"-" * 80}
""")

kısa_kenar = int(input("Kısa Kenarı Giriniz: "))
uzun_kenar = int(input("Uzun Kenarı Giriniz: "))

alan = kısa_kenar * uzun_kenar
cevre = (kısa_kenar * 2) + (uzun_kenar * 2)

print(f"Çevresi: {cevre} \nAlanı: {alan}")
