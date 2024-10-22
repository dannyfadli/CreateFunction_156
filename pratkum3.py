def konversiSuhu(value, unit):
    if unit == 'C':
        # Konversi dari Celsius ke Fahrenheit
        return (value * 9/5) + 32
    elif unit == 'F':
        # Konversi dari Fahrenheit ke Celsius
        return (value - 32) * 5/9
    else:
        return "Unit tidak valid. Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."

# Input dari user
suhu = float(input("Masukkan nilai suhu: "))
unit = input("Masukkan unit suhu ('C' untuk Celsius, 'F' untuk Fahrenheit): ").upper()

# Hasil konversi
konversi = konversiSuhu(suhu, unit)
print(f"Hasil konversi: {konversi}")