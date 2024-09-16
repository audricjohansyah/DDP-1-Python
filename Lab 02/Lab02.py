#print welcome statement
print("Selamat datang ke Dek Depe Holiday Tracker!")
print()

#minta input
jumlah_tempat = int(input("Masukkan banyak tempat wisata yang kamu kunjungi: "))

#minta input kembali jika input negatif atau nol
while jumlah_tempat <= 0:
    print("Input tidak valid. Silahkan masukkan input kembali!")
    jumlah_tempat = int(input("Masukkan banyak tempat wisata yang kamu kunjungi: "))

#tentukan nilai awal
total_rating = 0
highest_rated = 0
destination = 0 

#loop sebanyak jumlah tempat wisata
for i in range(1, jumlah_tempat+1):
    nama_tempat = input(f"Perjalanan {i}: ")
    rating = int(input(f"Rating perjalanan kamu ke {nama_tempat} (indeks 1-10): "))
    total_rating += rating
    
    #mencari perjalanan paling mengesankan
    if rating >= highest_rated:
        highest_rated = rating
        destination = nama_tempat
    print()

#hitung skala kebahagian
skala_kebahagian = total_rating / (jumlah_tempat)

#output
print("---Summary---")
print(f"Perjalanan paling mengesankan adalah ketika pergi ke {destination}")
print(f"Skala kebahagiaan Dek Depe adalah {skala_kebahagian:.2f}")

#conditional statement untuk skala kebahagian (mau mencetak pernyataan berdasarkan skala kebagiaan)
if 8 <= skala_kebahagian <= 10: 
    print("Dek Depe bahagia karena pengalamannya menyenangkan.")
elif 5 <= skala_kebahagian < 8:
    print("Dek Depe senang karena pengalamannya cukup baik.")
elif skala_kebahagian < 5:
    print("Dek Depe sedih karena pengalamannya buruk.")

print()
print("Terimakasih telah menggunakan Dek Depe Holiday Tracker!")