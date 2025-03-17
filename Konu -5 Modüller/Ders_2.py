print(f"""
{"-" * 80}
Kendi modülümüzü yazmak
1- Herhangi bir klasör oluştur.
2- Modülümüz ve deneme Python dosyamız aynı dizinde olması gerektiği için 2 tane
Python dosyasını da bu klasör altında oluşturuyoruz.
3- Konu-5 Modüller / Ders-2.py ve Konu-5 Modüller / Ders-2-settings.py dosyası oluşturuyoruz.
4- Konu-5 Modüller / Ders-2-settings.py dosyasının içine istediğimiz kadar fonksiynou yazıyoruz.
5- Son olarak da deneme.py dosyasının içinde bu modul1.py modulünü kullanıyoruz.
{"-" * 80}
""")

import Ders_2_Settings

print(Ders_2_Settings.toplama(3, 4 ,5))

print(Ders_2_Settings.selamla("Furkan"))

print(Ders_2_Settings.programlama_dilleri)

print(dir(Ders_2_Settings))
print(help(Ders_2_Settings))