#data library
dict_kodemenu, dict_namamenu, dict_customer_meja = {}, {}, {} #dictionary untuk menyimpan nama customer dan menu
all_food, kode_menu, nama_menu, harga_menu, output_menu = [], [], [], [], [] #list untuk membuat dictionary dan validasi menu
check_namamenu, check_kode= set(), set() #set untuk validasi menu
desk_number = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10] #list nomor meja
dict_desk = {1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{}} #dictionary untuk menyimpan pesanan customer berdasarkan nomor meja

#membaca file menu.txt dan menyimpan output ke dalam list
menu_file = open("menu.txt", "r")
file_lines = menu_file.readlines()
for i in range(len(file_lines)):
    lines = file_lines[i].strip().split(";")
    for line in lines:
        if "===" in line:
            line = line[len("==="):]
            output_menu.append(f"{line}:")

        else:
            if lines not in all_food:
                try: #validasi menu jika harga bukan angka
                   price = int(lines[2])

                except:
                    print("Daftar menu tidak valid, cek kembali menu.txt!")
                    exit()
                
                if price <= 0: #validasi menu jika harga ada yang bilangan negatif atau nol
                    print("Daftar menu tidak valid, cek kembali menu.txt!")
                    exit()
                
                else: #memasukkan data menu ke dalam list
                    all_food.append(lines)
                    kode_menu.append(lines[0])
                    nama_menu.append(lines[1])
                    harga_menu.append(price)
                    check_namamenu.add(lines[1])
                    check_kode.add(lines[0])
                    output_menu.append(f"{lines[0]} {lines[1]}, Rp{price}")

#validasi menu jika ada nama makanan yang sama atau ada kode makanan yang sama
if len(check_namamenu) != len(nama_menu) or len(check_kode) != len(kode_menu):
    print("Daftar menu tidak valid, cek kembali menu.txt!")
    exit()

#memasukkan menu ke dalam dictionary
for i in range(len(kode_menu)):
    dict_kodemenu[kode_menu[i]] = nama_menu[i], harga_menu[i], kode_menu[i] #dictionary dengan key berdasarkan kode makanan
    dict_namamenu[nama_menu[i]] = kode_menu[i], harga_menu[i], nama_menu[i] #dictionary dengan key berdsarkan nama makanan

#fungsi untuk mencetak isi menu
def open_menu():
    for lines in output_menu:
        print(lines)

#fungsi mencetak ringkasan pesanan user
def ringkasan_pesanan(nomor_table):
    total_cost = 0
    for keys in dict_desk[nomor_table]:
        count = dict_desk[nomor_table][keys][1]
        total_menu_price = dict_desk[nomor_table][keys][2]*count
        total_cost += total_menu_price
        print(f"{keys} {count} buah, total Rp{total_menu_price}")
    print(f"\nTotal pesanan: Rp{total_cost}")

#memulai infinite loop
condition = True
while condition:
    print("Selamat datang di Kafe Daun Daun Pacilkom")

    #memninta output perintah dari user
    command = input("Apa yang ingin Anda lakukan? ")

    #jika input perintah dari user adalah BUAT PESANAN
    if command == "BUAT PESANAN":

        #jika meja sudah penuh
        if len(desk_number) == 0:
            print("Mohon maaf meja sudah penuh, silakan kembali nanti.\n")
            print("---")

        #jika meja belum penuh 
        else:
            customer_name = input("Siapa nama Anda? ") #meminta nama customer

            #memasukkan nama customer ke dalam dictionary customer
            if customer_name not in dict_customer_meja.values():
                dict_customer_meja[desk_number[0]] = customer_name

            #jika ada nama yang sama, akan dimasukkan ke meja selanjutnya
            else:
                dict_customer_meja[desk_number[0]] = customer_name

            print("\nBerikut ini adalah menu yang kami sediakan:")
            open_menu() #mencetak isi menu

            pesanan = input("\nMasukkan menu yang ingin Anda pesan: ") #meminta menu yang ingin dipesan
            while pesanan != "SELESAI":

                #jika input pesanan dalam bentuk kode
                if pesanan in dict_kodemenu:
                    nama_pesanan = dict_kodemenu[pesanan][0] #mengubah kode menjadi nama makanan
                    kode_pesanan = dict_namamenu[nama_pesanan][0]
                    harga_pesanan = dict_namamenu[nama_pesanan][1]

                    if nama_pesanan not in dict_desk[desk_number[0]]: #memasukkan pesanan ke dictionary pesanan
                        dict_desk[desk_number[0]][nama_pesanan] = [kode_pesanan, 1, harga_pesanan]
                    
                    else: #menambahkan jumlah jika pesanan sudah ada di dictionary pesanan
                        dict_desk[desk_number[0]][nama_pesanan][1] += 1

                    pesanan = input(f"Behasil memesan {nama_pesanan}. Masukkan menu yang ingin anda pesan: ")
                
                #jika input pesanan dalam bentuk nama
                elif pesanan in dict_namamenu:
                    if pesanan not in dict_desk[desk_number[0]]: #memasukkan pesanan ke dictionary pesanan
                        kode_pesanan = dict_namamenu[pesanan][0]
                        harga_pesanan = dict_namamenu[pesanan][1]
                        dict_desk[desk_number[0]][pesanan] = [kode_pesanan, 1, harga_pesanan]

                    else: #menambahkan jumlah jika pesanan sudah di dictionary pesanan
                        dict_desk[desk_number[0]][pesanan][1] += 1

                    pesanan = input(f"Behasil memesan {pesanan}. Masukkan menu yang ingin anda pesan: ")

                #jika pesanan tidak ada di dictionary menu
                else:
                    pesanan = input(f"Menu {pesanan} tidak ditemukan. Masukkan menu yang ingin Anda pesan: ")

            #jika input buat pesanan user SELESAI
            if pesanan == "SELESAI":
                if len(dict_desk[desk_number[0]]) == 0: #customer belum memesan apapun
                    print("Anda belum memesan apa-apa!\n")
                    print("---")

                else:
                    print("\nBerikut adalah pesanan Anda:")
                    ringkasan_pesanan(desk_number[0]) #mencetak ringkasan pesanan nomor meja tersebut
                    #menghapus nomor meja yang sudah digunakan
                    print(f"Pesanan akan kami proses, Anda bisa menggunakan meja nomor {desk_number.pop(0)}. Terima kasih.\n")
                    print("---")

    #jika input perintah dari user UBAH PESANAN
    elif command == "UBAH PESANAN":

        #validasi nomor meja
        try:
            nomor_meja = int(input("Nomor meja berapa? ")) #meminta nomor meja dari user

        except:
           print("Nomor meja kosong atau tidak sesuai!\n")
           print("---")
           continue

        if nomor_meja > 10 or nomor_meja < 1:
           print("Nomor meja kosong atau tidak sesuai!\n")
           print("---")

        elif len(dict_desk[nomor_meja]) == 0:
            print("Nomor meja kosong atau tidak sesuai!\n")
            print("---")

        #jika nomor meja tidak salah dan ada pesanan di nomor meja tersebut
        else:
            print("\nBerikut ini adalah menu yang kami sediakan:")
            open_menu() #mencetak isi menu isi menu
            print("\nBerikut adalah pesanan Anda:")
            ringkasan_pesanan(nomor_meja) #mencetak ringkasan pesanan nomor meja tersebut
            print("\n---")
            ubah_pesanan = input("Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ") #meminta input perintah ubah pesanan dari user
            
            while ubah_pesanan != "SELESAI":
                #jika input ubah pesanan dari user GANTI JUMLAH
                if ubah_pesanan == "GANTI JUMLAH":
                    menu_diganti = input("Menu apa yang ingin Anda ganti jumlahnya: ") #meminta menu apa yang akan diganti

                    #validasi menu yang ingin diganti
                    if menu_diganti in dict_kodemenu: #jika menu berupa kode dan ada di dictionary menu
                        new_menu_diganti = dict_kodemenu[menu_diganti][0] #mengubah kode menjadi nama menu
        
                        if new_menu_diganti not in dict_namamenu: #jika nama menu tidak ada dalam dictionary menu
                            ubah_pesanan = input(f"Menu {menu_diganti} tidak ditemukan!. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                        elif new_menu_diganti not in dict_desk[nomor_meja]: #jika nama menu tidak ada dalam dictionary pesanan
                            ubah_pesanan = input(f"Menu {menu_diganti} tidak Anda pesan sebelumnya. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                        else: #jika menu ada di dictionary menu dan dictionary pesanan
                            jumlah_pesanan_baru = int(input("Masukkan jumlah pesanan yang baru: ")) #meminta jumlah pesanan baru

                            if jumlah_pesanan_baru <= 0:  #validasi jumlah pesanan harus bilangan bulat positif
                                ubah_pesanan = input("Jumlah harus bilangan positif! Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                            else: #jika input jumlah pesanan sudah benar
                                dict_desk[nomor_meja][new_menu_diganti][1] = jumlah_pesanan_baru #mengganti jumlah pesanan
                                ubah_pesanan = input(f"Berhasil mengubah pesanan {new_menu_diganti} {jumlah_pesanan_baru} buah. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                    else:
                        if menu_diganti not in dict_namamenu:#jika menu berupa nama makanan dan tidak ada di dictionary menu
                            ubah_pesanan = input(f"Menu {menu_diganti} tidak ditemukan! Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                        elif menu_diganti not in dict_desk[nomor_meja]: #jika menu berupa nama makanan dan tidak ada di dictionary pesanan
                            ubah_pesanan = input(f"Menu {menu_diganti} tidak Anda pesan sebelumnya. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                        else: #jika menu berupa nama makanan dan ada di dictionary menu dan dictionary pesanan
                            jumlah_pesanan_baru = int(input("Masukkan jumlah pesanan yang baru: ")) #meminta jumlah pesanan baru

                            if jumlah_pesanan_baru <= 0: #validasi jumlah pesanan harus bilangan bulat positif
                                ubah_pesanan = input("Jumlah harus bilangan positif! Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                            
                            else: #jika input pesanan sudah benar
                                dict_desk[nomor_meja][menu_diganti][1] = jumlah_pesanan_baru #mengganti jumlah pesanan
                                ubah_pesanan = input(f"Berhasil mengubah pesanan {menu_diganti} {jumlah_pesanan_baru} buah. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                #jika input ubah pesanan dari user HAPUS
                elif ubah_pesanan == "HAPUS":
                    menu_dihapus = input("Menu apa yang ingin Anda hapus dari pesanan: ") #meminta input menu yang akan dihapus

                    #validasi menu yang akan dihapus
                    if menu_dihapus in dict_kodemenu: #jika menu berupa kode dan ada di dictionary menu
                        new_menu_dihapus = dict_kodemenu[menu_dihapus][0] #mengubah kode menjadi nama menu
        
                        if new_menu_dihapus not in dict_namamenu: #jika nama menu tidak ada di dictionary menu
                            ubah_pesanan = input(f"Menu {menu_dihapus} tidak ditemukan! Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                        elif new_menu_dihapus not in dict_desk[nomor_meja]: #jika nama menu tidak ada di dictionary pesanan
                            ubah_pesanan = input(f"Menu {menu_dihapus} tidak Anda pesan sebelumnya. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                        else: #jika nama menu ada di dictionary pesanan dan dictionary menu
                            jumlah_dihapus = dict_desk[nomor_meja][new_menu_dihapus][1] #jumlah yang akan dihapus
                            ubah_pesanan = input(f"{jumlah_dihapus} buah {new_menu_dihapus} dihapus dari pesanan. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                            del dict_desk[nomor_meja][new_menu_dihapus] #menghapus pesanan dari dictionary pesanan

                    else:
                        if menu_dihapus not in dict_namamenu: #jika menu berupa nama dan tidak ada di dictionary menu
                            ubah_pesanan = input(f"Menu {menu_dihapus} tidak ditemukan! Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                        elif menu_dihapus not in dict_desk[nomor_meja]: #jika menu berupa nama dan tidak ada di dictionary pesanan
                            ubah_pesanan = input(f"Menu {menu_dihapus} tidak Anda pesan sebelumnya. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                        else: #jika menu berupa nama dan ada di dictionary pesanan dan dictionary menu
                            jumlah_dihapus = dict_desk[nomor_meja][menu_dihapus][1] #jumlah yang akan dihapus
                            ubah_pesanan = input(f"{jumlah_dihapus} buah {menu_dihapus} dihapus dari pesanan. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                            del dict_desk[nomor_meja][menu_dihapus]#menghapus pesanan dari dictionary pesanan

                #jika input ubah pesanan dari user TAMBAH PESANAN
                elif ubah_pesanan == "TAMBAH PESANAN":
                    menu_ditambah = input("Menu apa yang ingin Anda pesan: ") #meminta input menu yang ingin ditambah

                    #validasi menu yang akan ditambah
                    if menu_ditambah in dict_kodemenu: #jika menu berupa kode dan ada di dictionary menu
                        new_menu_ditambah = dict_kodemenu[menu_ditambah][0] #mengubah kode menjadi nama menu
                        kode_pesanan = dict_namamenu[new_menu_ditambah][0]
                        harga_pesanan = dict_namamenu[new_menu_ditambah][1]
        
                        if new_menu_ditambah not in dict_namamenu: #jika menu tidak ada di dictionary menu
                            ubah_pesanan = input(f"Menu {menu_ditambah} tidak ditemukan! Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                        elif new_menu_ditambah not in dict_desk[nomor_meja]: #jika menu tidak ada di dictionary pesanan
                            dict_desk[nomor_meja][new_menu_ditambah] = [kode_pesanan, 1, harga_pesanan] #menambahkan pesanan ke dictionary pesanan
                            ubah_pesanan = input(f"Berhasil memesan {new_menu_ditambah}. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                        
                        elif new_menu_ditambah in dict_desk[nomor_meja]: #jika menu ada di dictionary pesanan
                            dict_desk[nomor_meja][new_menu_ditambah][1] += 1 #menambahkan jumlah pesanan sebanyak 1 buah
                            ubah_pesanan = input(f"Berhasil memesan {new_menu_ditambah}. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                    else:
                        if menu_ditambah not in dict_namamenu: #jika menu berupa nama dan tidak ada di dictionary menu
                            ubah_pesanan = input(f"Menu {menu_ditambah} tidak ditemukan! Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                        elif menu_ditambah not in dict_desk[nomor_meja]: #jika menu berupa nama dan tidak ada di dictionary pesanan
                            dict_desk[nomor_meja][menu_ditambah] = [dict_namamenu[menu_ditambah][0], 1, dict_namamenu[menu_ditambah][1]] #menambahkan pesanan ke dictionary pesanan
                            ubah_pesanan = input(f"Berhasil memesan {menu_ditambah}. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                        elif menu_ditambah in dict_desk[nomor_meja]: #jika menu berupa nama dan ada di dictionary pesanan
                            dict_desk[nomor_meja][menu_ditambah][1] += 1 #menambahkan jumlah pesanan sebanyak 1 buah
                            ubah_pesanan = input(f"Berhasil memesan {menu_ditambah}. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

                else: #jika input ubah pesanan dari user tidak valid
                    ubah_pesanan = input("Perintah tidak valid. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")

            #jika input ubah pesanan dari user SELESAI
            if ubah_pesanan == "SELESAI":
                if len(dict_desk[nomor_meja]) == 0: #jika pesanan user menjadi kosong
                    print("Anda belum memesan apa-apa!\n")
                    print("---")

                else:
                    print("\nBerikut adalah pesanan terbaru Anda:") #mencetak ringkasan pesanan baru user
                    ringkasan_pesanan(nomor_meja)
                    print("\n---")

    #jika input perintah dari user SELESAI MENGGUNAKAN MEJA
    elif command == "SELESAI MENGGUNAKAN MEJA":

        #validasi nomor meja
        try:
            nomor_meja = int(input("Nomor meja berapa? ")) #meminta nomor meja dari user

        except:
           print("Nomor meja kosong atau tidak sesuai!\n")
           print("---")
           continue

        if nomor_meja > 10 or nomor_meja < 1:
           print("Nomor meja kosong atau tidak sesuai!\n")
           print("---")

        elif len(dict_desk[nomor_meja]) == 0:
            print("Nomor meja kosong atau tidak sesuai!\n")
            print("---")

        #jika nomor meja tidak salah dan ada pesanan di nomor meja tersebut
        else:
            #mencetak pesan untuk customer di nomor meja tersebut
            print(f"Pelanggan atas nama {dict_customer_meja[nomor_meja]} selesai menggunakan meja {nomor_meja}.\n")
            print("---")

            # menulis receipt untuk customer di nomor meja tersebut
            receipt = open(f"receipt_{dict_customer_meja[nomor_meja]}.txt", "w")
            total_cost = 0
            for keys in dict_desk[nomor_meja]:
                code_menu = dict_desk[nomor_meja][keys][0]
                count = dict_desk[nomor_meja][keys][1]
                menu_price = dict_desk[nomor_meja][keys][2]
                total_menu_price = dict_desk[nomor_meja][keys][2]*count
                total_cost += total_menu_price
                receipt.write(f"{code_menu};{keys};{count};{menu_price};{total_menu_price}\n") 
            receipt.write(f"\nTotal {total_cost}") #evaluasi dan menulis total pembayaran user ke receipt
            receipt.close()

            del dict_customer_meja[nomor_meja] #menghapus nama customer dari dictionary customer
            dict_desk[nomor_meja].clear() #menghapus isi dictionary pesanan customer
            desk_number.append(nomor_meja) #menambahkan nomor meja customer ke dalam list nomor meja
            desk_number.sort()

    #jika input perintah dari user tidak benar
    else:
        if command == "EXIT": #jika input EXIT program berhenti
            condition = False
            print("\nTerima kasih telah datang ke Kafe Daun Daun Pacilkom!\n")
            print("---")
            exit()

        else: #jika input dari user tidak valid
            print("---")
            print("\nPerintah tidak valid!\n")
            print("---")

#Collaborator: 2206082114 - Clement Samuel Marly, 2206082751 - Yosef Nuraga Wicaksana
#References: https://docs.python.org/3/tutorial/datastructures.html, https://www.w3schools.com/python/python_dictionaries.asp, https://www.geeksforgeeks.org/python-dictionary/, https://www.w3schools.com/python/python_ref_dictionary.asp