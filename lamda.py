import math

# Lambda function untuk menghitung luas lingkaran
luas = lambda r: math.pi * r ** 2

# Input dari user
radius = float(input("Masukkan jari-jari lingkaran: "))

# Hasil perhitungan luas lingkaran
Luas = luas(radius)
print(f"Luas lingkaran dengan jari-jari {radius} adalah {Luas}")