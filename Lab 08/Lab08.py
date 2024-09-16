#minta input data hubungan dari user
data_user = input("Masukkan data hubungan:\n")

#dictionary untuk menampung data
dict_data = {}

#minta input kembali selama input bukan "SELESAI" dan memasukkan data ke dictionary
while data_user!= "SELESAI":
    sub_data_user = data_user.split()
    nama_x = sub_data_user[0]
    kenalan_x = sub_data_user[1]
    jarak = float(sub_data_user[2])

    if nama_x not in dict_data:
        dict_data[nama_x] = kenalan_x, jarak

    data_user = input()

#minta input nama awal dan nama tujuan
nama_awal = input("\nMasukkan nama awal: ")
nama_tujuan = input("Masukkan nama tujuan: ")

#fungsi recursion
def hubungan(nama_awal, nama_tujuan):
    if nama_awal not in dict_data:
        raise KeyError
    
    distance = dict_data[nama_awal][1]
    dicari = dict_data[nama_awal][0]

    #base case 
    if nama_tujuan in dicari:
        return int(distance*10 // 1)

    #recursion case
    else:
        if nama_tujuan not in dict_data[nama_awal]:
            return int(distance*10 // 1) + hubungan(dicari, nama_tujuan)

try:
    #print output
    print(f"Jarak total: {hubungan(nama_awal, nama_tujuan)}")
    if hubungan(nama_awal, nama_tujuan) > 1000:
        print(f"{nama_awal} dan {nama_tujuan} tidak saling kenal.")

    elif 100 < hubungan(nama_awal, nama_tujuan) <= 1000:
        print(f"{nama_awal} dan {nama_tujuan} mungkin saling kenal.")
    
    elif 0 < hubungan(nama_awal, nama_tujuan) <= 100:
        print(f"{nama_awal} dan {nama_tujuan} kenal dekat.")

except KeyError:
    print(f"Tidak ada hubungan antara {nama_awal} dan {nama_tujuan}.")
