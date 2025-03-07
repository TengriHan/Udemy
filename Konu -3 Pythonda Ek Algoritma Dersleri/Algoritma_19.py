print("""
-----------------------------------------------------------------------------------------
Tersten yazıldığında da aynı değeri olan sayılara Palindrom sayılar denir.
Örnek olarak 1991 veya 34543 sayıları tersten yazılsa bile aynı değerde olurlar.
1000- 100000 sayıları arasındaki palindromları bulan programı yazınız.
-----------------------------------------------------------------------------------------
"""
)

for i in range(1000, 100000):
    sayi = str(i)
    ters_sayi = sayi[::-1]
    if sayi == ters_sayi:
        print(sayi)