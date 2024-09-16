#print welcome statement
print("Selamat datang di program Mengenal Angkatan!")
print("===========================================")

#minta input data siswa dari user
data_siswa = input("Masukkan identitas mahasiswa:\n")

#dictionary untuk menampung jawaban dari user
daftar_siswa = {}

#tanya ulang hingga input = stop dan masukkin jawaban ke dictionary
condition = True
while condition:
    if data_siswa != "STOP":
        sub_data_siswa = data_siswa.split()
        nama = sub_data_siswa[0]
        npm = sub_data_siswa[1]
        bulan_lahir = sub_data_siswa[4]
        daftar_siswa[npm] = nama, npm, bulan_lahir
        data_siswa = input()

    else:
        condition = False

#minta input bulan lahir mahasiswa yang mau dicari
bulan = input("\nCari mahasiswa berdasarkan bulan: ")

#set up variable
tuple_data = () #untuk menampung value
nama_found = set() #untuk menampung nama
npm_found = set() #untuk menampung npm

temp = True
while temp:
    if bulan != "STOP":

        #iterasi data yang ada di daftar siswa
        for data in daftar_siswa.values():
            if bulan in data:
                tuple_data += data
                nama_found.add(data[0].upper()) #menampung nama yang ditemukan
                npm_found.add(data[1]) #menampung npm yang ditemukan

        #mencetak output jika tidak ditemukan mahasiswa dan npm
        if bulan not in tuple_data:
            print("================= Hasil ================")
            print(f"Tidak ditemukan mahasiswa dan NPM yang lahir di bulan {bulan}.\n")
            bulan = input("Cari mahasiswa berdasarkan bulan: ")

        #mencetak output jika ditemukan mahasiswa dan npm
        else:
            print("================= Hasil ================")

            print(f"Terdapat {len(nama_found)} nama yang lahir di bulan {bulan}:")
            for name in nama_found:
                name = name[0] + name[1:].lower()
                print(f"- {name}")

            print(f"\nTerdapat {len(npm_found)} NPM yang lahir di bulan {bulan}:")
            for npms in npm_found:
                print(f"- {npms}")

            bulan = input("\nCari mahasiswa berdasarkan bulan: ") 

    #jika input stop program berhenti
    else:
        temp = False
        print("\nTerima kasih telah menggunakan program ini, semangat PMB-nya!") 