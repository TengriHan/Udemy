print(f"""
{"-" * 80}
Global ve Yerel Değişkenler
Pythonda her bir değişkenin, fonksiyonun ve ileride göreceğimiz sınıfların(class) aslında
bir kapsamı(scope) bulunur ve Python herbir değişkeni bir isim alanında (namespace)
tanımlar. Değişkenlerin isim Alanı ise, bu değişkenlerin nerelerde var olduğnu ve kullanabileceğini
gösterir.
{"-" * 80}
""")

def fonksiyon():
    a = 10
    print(a)

print(fonksiyon())
#Hatalı Kullanım
# print(a)

b = 5
def fonksiyon():
    print(b)

print(fonksiyon())

print(f"{"*" * 80}")

# 2 tane aynı isimde değişken varsa fonksiyon içerisindeki local fonksiyon dışındaki global olur
print("Global olmadan kullanım")

c = 10
def fonksiyon_3():
    c = 2
    print(c)
fonksiyon_3()
print(c)

print(f"{"*" * 80}")

print("Global kullanım")

d = 5

def fonksiyon_4():
    global d
    d = 3
    print(d)

print(fonksiyon_4())
print(d)

print(f"{"*" * 80}")

if True:
    e = 4
    print(e)
print(e)