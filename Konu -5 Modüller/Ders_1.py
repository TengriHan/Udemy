print(f"""
{"-" * 80}
Pythonda aslında herbir dosya bir modüldür ve her bir modül içinde fonksiyonlar, sınıflar
ve objeler barındırır. Biz de bu modülleri programımıza dahil ederek içindeki fonksiyonlardan,
sınıflardan ve objelerden faydalanabiliriz.
{"-" * 80}
""")


# Modülü programa dahil etme import modül_adi

import math

# Modülün içindeki fonksiyonlar
print(dir(math))

# Modülün fonksiyonun anlatımı
print(help(math))


print(f"{"-" * 80}")


print(math.factorial(5))
print(math.factorial(6))
print(math.floor(5.6))
print(math.ceil(5.6))

print(f"{"-" * 80}")


import math as matematik
print("import math as matematik")
print(matematik.factorial(5))
print(matematik.factorial(6))
print(matematik.floor(5.6))
print(matematik.ceil(5.6))

print("from math import * ile tüm fonksiyonları çekebilirsiniz")

print(f"{"-" * 80}")
