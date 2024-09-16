data_kereta = input("Selamat datang! Silakan masukkan jadwal KA:\n")
daftar_kereta = {}

condition = True
while condition:
    if data_kereta != "selesai":
        sub_data_kereta = data_kereta.split()
        nomor_ka = sub_data_kereta[0]
        tujuan_akhir = sub_data_kereta[1]
        jam_keberangkatan = sub_data_kereta[2]
        harga_tiket = int(sub_data_kereta[3])
        daftar_kereta[nomor_ka] = [nomor_ka, tujuan_akhir, jam_keberangkatan, harga_tiket, nomor_ka]
        data_kereta = input()

    else:
        condition = False

def info_tujuan():
    data_tujuan = set()
    for data in daftar_kereta.values():
        data_tujuan.add(data[1])

    print("KA di stasiun ini memiliki tujuan akhir:")
    for destination in data_tujuan:
        print(destination)

def tujuan_kelas():
    tujuan = sub_command[1]
    kelas_kereta = sub_command[2]

    for data in daftar_kereta.values():
        if data[0][0] == "1":
            data[0] = "Eksekutif"

        elif data[0][0] == "2":
            data[0] = "Bisnis"

        elif data[0][0] == "3":
            data[0] = "Ekonomi"

    all_destination = []
    all_nomor_ka = []
    all_price = []
    all_time = []
    all_class= []

    for data in daftar_kereta.values():
        if tujuan in data and kelas_kereta in data:
            all_nomor_ka.append(data[-1])
            all_destination.append(data[1])
            all_price.append(data[3])
            all_time.append(data[2])
            all_class.append(data[0])

    if tujuan in all_destination and kelas_kereta in all_class:
        for i in range(len(all_nomor_ka)):
            print(f"KA {all_nomor_ka[i]} berangkat pukul {all_time[i]} dengan harga tiket {all_price[i]}")

    else:
        print("Tidak ada jadwal KA yang sesuai")

def tujuan_jam():
    tujuan = sub_command[1]
    jam = int(sub_command[2])

    all_destination = []
    all_nomor_ka = []
    all_price = []
    all_time = []

    for data in daftar_kereta.values():
        if tujuan in data and jam >= int(data[2]):
            all_nomor_ka.append(data[-1])
            all_destination.append(data[1])
            all_price.append(data[3])
            all_time.append(int(data[2]))

    if tujuan in all_destination and jam in all_time:
        for i in range(len(all_nomor_ka)):
            print(f"KA {all_nomor_ka[i]} berangkat pukul {all_time[i]} dengan harga tiket {all_price[i]}")

    else:
        print("Tidak ada jadwal KA yang sesuai")

def tujuan_kelas_termurah():
    tujuan = sub_command[1]
    kelas_kereta = sub_command[2]

    for data in daftar_kereta.values():
        if data[0][0] == "1":
            data[0] = "Eksekutif"

        elif data[0][0] == "2":
            data[0] = "Bisnis"

        elif data[0][0] == "3":
            data[0] = "Ekonomi"

    all_destination = []
    all_nomor_ka = []
    all_price = []
    all_time = []
    all_class= []

    for data in daftar_kereta.values():
        if tujuan in data and kelas_kereta in data:
            all_nomor_ka.append(data[-1])
            all_destination.append(data[1])
            all_price.append(data[3])
            all_time.append(data[2])
            all_class.append(data[0])

    harga_termurah = 9999999999999999999
    destinasi_haga_termurah= ""
    nomor_ka_harga_termurah = ""
    kelas_kereta_harga_termurah = ""
    waktu_harga_termurah = ""

    for i in range(len(all_price)):
        if all_price[i] < harga_termurah:
            harga_termurah = all_price[i]
            destinasi_haga_termurah = all_destination[i]
            nomor_ka_harga_termurah = all_nomor_ka[i]
            kelas_kereta_harga_termurah = all_class[i]
            waktu_harga_termurah = all_time[i]

    if tujuan == destinasi_haga_termurah and kelas_kereta == kelas_kereta_harga_termurah:
        print(f"KA {nomor_ka_harga_termurah} berangkat pukul {waktu_harga_termurah} dengan harga tiket {harga_termurah}")

    else:
        print("Tidak ada jadwal KA yang sesuai")

def tujuan_jam_termurah():
    tujuan = sub_command[1]
    jam = int(sub_command[2])

    all_destination = []
    all_nomor_ka = []
    all_price = []
    all_time = []

    for data in daftar_kereta.values():
        if tujuan in data and jam >= int(data[2]):
            all_nomor_ka.append(data[-1])
            all_destination.append(data[1])
            all_price.append(data[3])
            all_time.append(int(data[2]))

    harga_termurah = 9999999999999999999
    destinasi_haga_termurah= ""
    nomor_ka_harga_termurah = ""
    waktu_harga_termurah = ""

    for i in range(len(all_price)):
        if all_price[i] < harga_termurah:
            harga_termurah = all_price[i]
            destinasi_haga_termurah = all_destination[i]
            nomor_ka_harga_termurah = all_nomor_ka[i]
            waktu_harga_termurah = all_time[i]

    if tujuan == destinasi_haga_termurah and jam >= waktu_harga_termurah:
        print(f"KA {nomor_ka_harga_termurah} berangkat pukul {waktu_harga_termurah} dengan harga tiket {harga_termurah}")

    else:
        print("Tidak ada jadwal KA yang sesuai")

def keluar():
    print("Terima kasih sudah menggunakan program ini!")

print("\nPerintah yang tersedia:")
print("1. INFO_TUJUAN")
print("2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>")
print("3. TUJUAN_KELAS_TERMURAH <tujuan_akhir> <kelas_kereta>")
print("4. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>")
print("5. TUJUAN_JAM_TERMURAH <tujuan_akhir> <jam_keberangkatan>")
print("6. EXIT")

temp = True
while temp:
    command = input("\nMasukkan perintah: ")
    sub_command = command.split()

    if command == "INFO_TUJUAN":
        info_tujuan()

    elif sub_command[0] == "TUJUAN_KELAS":
        if len(sub_command) < 3:
            print("Perintah yang dimasukkan tidak valid")

        else:
            tujuan_kelas()

    elif sub_command[0] == "TUJUAN_KELAS_TERMURAH":
        if len(sub_command) < 3:
            print("Perintah yang dimasukkan tidak valid")

        else:
            tujuan_kelas_termurah()

    elif sub_command[0] == "TUJUAN_JAM":
        if len(sub_command) < 3:
            print("Perintah yang dimasukkan tidak valid")

        else:
            tujuan_jam()

    elif sub_command[0] == "TUJUAN_JAM_TERMURAH":
        if len(sub_command) < 3:
            print("Perintah yang dimasukkan tidak valid")

        else:
            tujuan_jam_termurah()

    elif command == "EXIT":
        temp = False
        keluar()

    else:
        print("Perintah yang dimasukkan tidak valid")