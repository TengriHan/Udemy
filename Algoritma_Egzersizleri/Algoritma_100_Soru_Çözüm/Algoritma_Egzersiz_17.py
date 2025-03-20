print(f"""
{"-" * 80}
İç içe döngüler ile 
saat: dakika: saniye 
olarak saat yapınız.  
Saat 0 ile 23, dakika 0 ile 59 ve saniye de 0 ile 59 arasında ilerleyecektir.
{"-" * 80}
""")

for saat in range(0, 24):
    for dakika in range(0,60):
        for saniye in range(0,60):
            print(f"{saat}:{dakika}:{saniye}")



