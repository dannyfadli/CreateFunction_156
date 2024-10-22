import math  # Mengimpor modul math untuk menggunakan fungsi matematika seperti pi.

# Lambda function untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r * r  # Mendefinisikan fungsi lambda yang menghitung luas lingkaran berdasarkan jari-jari r.

jari_jari = 7  # Mendefinisikan variabel jari_jari dengan nilai 7.

area = luas_lingkaran(jari_jari)  # Menghitung luas lingkaran dengan memanggil fungsi lambda 'luas_lingkaran' menggunakan nilai jari_jari.

# Menampilkan hasil perhitungan
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")  # Mencetak hasil luas lingkaran ke layar dengan format dua desimal menggunakan f-string.