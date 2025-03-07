"""
1'den 10'a kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
"""

for i in range(1, 11):
    print("*************************************")
    for x in range(1, 11):
        print("{} x {} = {}".format(i, x, i * x))
