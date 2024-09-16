print("Selamat datang di program Mengenal Angkatan!")
print("===========================================")

#minta input
data_siswa = input("Masukkan identitas mahasiswa:\n") 

#membuat dictionary
daftar_siswa = {}

#masukkin input ke dictionary
while data_siswa != "STOP":
    sub_data_siswa = data_siswa.split()
    nama = sub_data_siswa[0]
    npm = sub_data_siswa[1]
    bulan_lahir = sub_data_siswa[4]
    
    #masukkan input ke dictionary dengan key = bulan lahir
    if bulan_lahir not in daftar_siswa.keys():
        daftar_siswa[bulan_lahir] = (nama, npm)

    else:
        daftar_siswa[bulan_lahir] += (nama, npm)
    
    data_siswa = input()

#minta input bulan mahasiswa yg dicari
bulan = input("\nCari mahasiswa berdasarkan bulan: ")

while bulan != "STOP":

    #conditionals jika mahasiswa tidak ditemukan
    if bulan not in daftar_siswa.keys():
        print("================= Hasil ================")
        print(f"Tidak ditemukan mahasiswa dan NPM yang lahir di bulan {bulan}.\n")
        bulan = input("\nCari mahasiswa berdasarkan bulan: ")

    #conditionals jika mahasiswa ditemukan
    else:
        #set untuk store nama dan npm siswa yang ditemukan
        nama_ditemukan = set()
        npm_ditemukan = set()

        #print output jika ditemukan
        print("================= Hasil ================")
        for i in range(len(daftar_siswa[bulan])):
            if i%2 == 0:
                nama_ditemukan.add(daftar_siswa[bulan][i])
            else:
                npm_ditemukan.add(daftar_siswa[bulan][i])
        
        print(f"Terdapat {len(nama_ditemukan)} nama yang lahir di bulan {bulan}")
        for name in nama_ditemukan:
            print(f"- {name}")

        print(f"\nTerdapat {len(npm_ditemukan)} NPM yang lahir di bulan {bulan}:")
        for npms in npm_ditemukan:
            print(f"- {npms}")

        bulan = input("\nCari mahasiswa berdasarkan bulan: ")

#print output jika stop
if bulan == "STOP":
    print()
    print("Terima kasih telah menggunakan program ini, semangat PMB-nya!")
