"""
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın.
Bu işlemi continue ile yapmaya çalışın.
"""

for i in range(1, 100):
    if i % 3 == 0:
        print(i)