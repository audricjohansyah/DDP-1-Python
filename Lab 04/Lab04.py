te#welcome statement
print("Selamat datang di Pacil Mart!")
print()

try:
    file_name = input("Masukkan nama file input: ")#minta input file dari user
    print()
    file = open(file_name, 'r')
    filelines = file.readlines() 
    empty_file = False #variable untuk jika file ada tetapi kosong

    #conditionals untuk jika file ada tapi kosong
    if len(filelines) == 0:
        empty_file = True
    file.close()

    #conditionals untuk jika file ada dan tidak kosong
    if not empty_file:
        print("Berikut adalah daftar belanjaanmu:")
        print()
        print("{: <12s}|{: >8s}|{: >10s}". format("Nama Barang", "Jumlah", "Kembalian")) #mencetak header untuk output
        print("--------------------------------")

        for line in filelines: #membaca setiap line dalam file
            baris = line.split() #memisahkan string dan dimasukkan dalam list

            #meng-index setiap string
            items = baris[0]
            payment = int(baris[1])
            item_price = int(baris[2])

            #menghitung jumlah barang dan kembalian
            total_items = payment // item_price
            payback = payment - (total_items*item_price)
            
            print("{: <12s}|{: >8d}|{: >10d}". format(items, total_items, payback))

        print()
        print("Terima kasih sudah belanja di Pacil Mart!")
      
    else:
        print()
        print("File input ada tapi kosong :(")
    
#ouput jika file tidak ada
except FileNotFoundError:
    print()
    print("File tidak tersedia.")
            
