#print welcome statement
print("Selamat Datang di Bunker Hacker!")
print()

#meminta input dari user
banyak_konversi = int(input("Masukkan berapa kali konversi yang ingin dilakukan: "))

#loop sebanyak berapa kali mau konversi angka
for i in range (1, banyak_konversi + 1):
    dec_number = int(input(f"Masukkan angka ke-{i} yang ingin dikonversikan (dalam desimal): "))

    #nilai awal untuk output
    base_8 = ''

    #mencari panjang angka desimal
    n = len(str(dec_number))

    #loop untuk mencari basis 8    
    for i in range (n+1):
        base_8 += str(dec_number % 8)
        dec_number = dec_number // 8

        # if dec_number == 0:
        #     break

    #mencetak output diurutin dari yang terakhir (reversed)
    print(f"Hasil konversi desimal ke basis 8 : {base_8[::-1]}")
    print()

#print goodbye statement
print("Terima kasih telah menggunakan Bunker Hacker!")