# Import library math
import math

# Menyimpan harga kertas
harga_kertas = 0.40

# Menerima input user dan menyimpannya dalam variabel yang sesuai
nama = input("Nama: ")
sisi_persegi = float(input("Panjang persegi nametag (cm): "))
panjang_trapesium = float(input("Panjang trapesium nametag (cm): "))
banyak_nametag = int(input("Banyak nametag: "))
print()

# Menghitung luas persegi
luas_persegi = sisi_persegi * sisi_persegi

# Menghitung luas setengah_lingkaran
jari_lingkaran = sisi_persegi/2
luas_setengah_lingkaran = (1/2) * math.pi * jari_lingkaran * jari_lingkaran

# Menghitung luas segitiga
alas_segitiga = sisi_persegi
tinggi_segitiga = sisi_persegi
luas_segitiga = (1/2) * alas_segitiga * tinggi_segitiga

# Menghitung luas trapesium
tinggi_trapesium = sisi_persegi
luas_trapesium = (1/2) * (sisi_persegi + panjang_trapesium) * tinggi_trapesium

# Menghitung luas 1 nametag, luas total nametag, dan total harga nametag
luas_nametag = luas_persegi + luas_setengah_lingkaran + luas_segitiga + luas_trapesium
total_luas = banyak_nametag * luas_nametag
total_harga = total_luas * harga_kertas
total_harga = math.ceil(total_harga/1000) * 1000 # Pembulatan total harga ke ribuan ke atas

# Mencetak output sesuai perhitungan 
print(f"Halo, {nama}! Berikut informasi terkait nametag kamu: ")
print()
print(f"Luas 1 nametag: {luas_nametag:.2f} cm^2") # Pembulatan desimal 2 angka dengan fstring
print(f"Luas total nametag: {total_luas:.2f} cm^2") # Pembulatan desimal 2 angka dengan fstring
print(f"Uang yang diperlukan: Rp{total_harga}")
