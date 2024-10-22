def konversisuhu(temperature, value):  # Mendefinisikan fungsi konversisuhu yang mengambil dua parameter: temperature dan value.
    if value == 'c':  # Jika value adalah 'c', maka fungsi akan mengkonversi suhu dari Fahrenheit ke Celsius.
        tempraturesuhu = (temperature - 32) * 5/9  # Menghitung suhu dalam Celsius menggunakan rumus konversi.
        return tempraturesuhu, 'c'  # Mengembalikan hasil konversi dan unit 'c' untuk Celsius.
    else:  # Jika value bukan 'c', maka diasumsikan bahwa value adalah 'f' untuk Fahrenheit.
        tempraturesuhu = (temperature * 9/5) + 32  # Menghitung suhu dalam Fahrenheit menggunakan rumus konversi.
        return tempraturesuhu, "f"  # Mengembalikan hasil konversi dan unit 'f' untuk Fahrenheit.

celsius_temperature = 30  # Mendefinisikan suhu dalam Celsius.
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'f')  # Mengkonversi suhu dari Celsius ke Fahrenheit menggunakan fungsi konversisuhu.
print(f"{celsius_temperature}°c dikonversi ke farenheit adalah {temperaturesuhu}°{target_value}")  # Mencetak hasil konversi ke layar.

fahrenheit_temperature = 86  # Mendefinisikan suhu dalam Fahrenheit.
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'c')  # Mengkonversi suhu dari Fahrenheit ke Celsius menggunakan fungsi konversisuhu.
print(f"{fahrenheit_temperature}°f dikonversi ke celcius adalah {temperaturesuhu}°{target_value}")  # Mencetak hasil konversi ke layar.