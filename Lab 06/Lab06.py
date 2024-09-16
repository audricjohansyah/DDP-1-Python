#import math untuk menghitung nilai
import math

#welcome statement
print("Selamat mencoba Program Pemeriksa Nilai Dek Depe!")
print("=================================================\n")

#minta input kunci jawaban dari user
kunci_jawaban = input("Masukkan kunci jawaban:\n")
list_kunci_jawaban = []

#fungsi untuk meminta input kunci jawaban dan menyimpan di list
condition = True
while condition:
    if kunci_jawaban != "STOP":
        list_kunci_jawaban.append(kunci_jawaban)
        kunci_jawaban = input()

    else:
        if len(list_kunci_jawaban) == 0: #jika input pertama dari user adalah STOP, program akan berhenti
            exit()
        condition = False

#meminta input jawaban dari user
jawaban_user = print("\nMasukkan jawaban kamu:")
list_jawaban_user = []

#meminta input jawaban user sebanyak jumlah kunci jawaban dan menyimpan di listdef answer_user():
nomor = 0
while nomor != (len(list_kunci_jawaban)):
    jawaban_user = input()
    list_jawaban_user.append(jawaban_user)
    nomor += 1

#untuk mengecek nilai benar atau salah
nilai_benar = 0
nilai_salah = 0
for i in range(len(list_kunci_jawaban)):
    if list_kunci_jawaban[i] == list_jawaban_user[i]:
        nilai_benar += 1

    else:
        nilai_salah += 1

#menghitung nilai akhir
nilai = math.floor((nilai_benar / len(list_kunci_jawaban)) * 100)

#conditional statement nilai untuk mencetak output
if nilai >= 85:
    print("\nSelamat :D")

elif 55 <= nilai < 85:
    print("\nSemangat :)")

elif nilai < 55:
    print("\nnt")

#mencetak output
total_soal = len(list_kunci_jawaban)
print(f"Total jawaban benar adalah {nilai_benar} dari {total_soal} soal")
print(f"Nilai yang kamu peroleh adalah {nilai}")