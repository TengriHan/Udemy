print("""
----------------------------------------------------------
0 ile 1000 arasındaki Fibonacci sayılarını bulan program.
----------------------------------------------------------
""")

a = 1
b = 1
c = 0

while c < 1000:
    print(b)
    c = a + b
    a = b
    b = c
