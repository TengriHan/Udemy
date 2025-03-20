print(f"""
{"*" * 80}
Kullanıcıdan ismini alarak harflere ayıran ve 
bu harflerle başlayan şehirleri sırasıyla ekrana yazdıran kodu yazınız. 
( Ğ , Ü gibi harfler için farklı bir bilgi yazdırabilirsiniz. )
{"*" * 80}
""")

sehirler = {
    "Adana": "A", "Adıyaman": "A", "Afyonkarahisar": "A", "Ağrı": "A", "Aksaray": "A",
    "Amasya": "A", "Ankara": "A", "Antalya": "A", "Ardahan": "A", "Artvin": "A", "Aydın": "A",
    "Balıkesir": "B", "Bartın": "B", "Batman": "B", "Bayburt": "B", "Bilecik": "B", "Bingöl": "B",
    "Bitlis": "B", "Bolu": "B", "Burdur": "B", "Bursa": "B", "Çanakkale": "Ç", "Çankırı": "Ç",
    "Çorum": "Ç", "Denizli": "D", "Diyarbakır": "D", "Düzce": "D", "Edirne": "E", "Elazığ": "E",
    "Erzincan": "E", "Erzurum": "E", "Eskişehir": "E", "Gaziantep": "G", "Giresun": "G",
    "Gümüşhane": "G", "Hakkari": "H", "Hatay": "H", "Iğdır": "I", "Isparta": "I", "İstanbul": "İ",
    "İzmir": "İ", "Kahramanmaraş": "K", "Karabük": "K", "Karaman": "K", "Kars": "K", "Kastamonu": "K",
    "Kayseri": "K", "Kırıkkale": "K", "Kırklareli": "K", "Kırşehir": "K", "Kilis": "K", "Kocaeli": "K",
    "Konya": "K", "Kütahya": "K", "Malatya": "M", "Manisa": "M", "Mardin": "M", "Mersin": "M",
    "Muğla": "M", "Muş": "M", "Nevşehir": "N", "Niğde": "N", "Ordu": "O", "Osmaniye": "O", "Rize": "R",
    "Sakarya": "S", "Samsun": "S", "Siirt": "S", "Sinop": "S", "Sivas": "S", "Şanlıurfa": "Ş",
    "Şırnak": "Ş", "Tekirdağ": "T", "Tokat": "T", "Trabzon": "T", "Tunceli": "T", "Uşak": "U",
    "Van": "V", "Yalova": "Y", "Yozgat": "Y", "Zonguldak": "Z"
}

isim = input("İsminizi giriniz: ").upper()  # Büyük harfe çevir ki eşleşme daha kolay olsun

for i in isim:
    bulunan_sehirler = [sehir for sehir in sehirler.keys() if sehir.startswith(i)]

    if bulunan_sehirler:
        print(f"{i} harfi için şehirler: {', '.join(bulunan_sehirler)}")
    else:
        print(f"{i} harfiyle başlayan şehir yok!")

