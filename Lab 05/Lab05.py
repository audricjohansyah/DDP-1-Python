#import math
import math

#cetak welcome statement
print("Selamat datang di Depot Minuman Dek Depe!")
print("==========================================")

#set up variable awal
volume_balok = 0
volume_kerucut = 0
total_volume = 0
total_harga = 0

#function untuk menghitung volume balok
def vol_balok (p,l,t):
	volume_balok = p * l * t
	return volume_balok

#function untuk menghitung volume kerucut
def vol_kerucut(r,t):
	volume_kerucut = (1/3) * math.pi * (r**2) * t
	return volume_kerucut


#minta input shape dari user selamanya
while True:
	shape = input("Masukkan bentuk galon yang diinginkan (STOP untuk berhenti): ")

	#jika user memilih bentuk BALOK
	if shape == "BALOK":
		panjang = float(input("Masukkan panjang balok : "))
		lebar = float(input("Masukkan lebar balok : "))
		tinggi = float(input("Masukkan tinggi balok : "))
		print()
		volume_balok = vol_balok(panjang,lebar,tinggi)
	
	#jika user memilih bentuk KERUCUT
	elif shape == "KERUCUT":
		radius = float(input("Masukkan jari-jari kerucut : "))
		tall = float(input("Masukkan tinggi kerucut : "))
		print()
		volume_kerucut = vol_kerucut(radius,tall)
		
	#jika input STOP akan mencetak output dan stop loop
	elif shape == "STOP":

		#menghitung total volume dan total harga
		total_volume = volume_balok + volume_kerucut
		total_harga = total_volume * 700

		#jika kita input STOP tanpa memilih bentuk apapun terlebih dahulu
		if total_volume == 0:
			print()
			print("====================================================")
			print("Anda tidak memasukkan input satupun :(")
			print("Terima kasih telah menggunakan Depot Air Minum Dek Depe")
			print("====================================================")
			print()
			break

		#jika kita input STOP setelah memilih bentuk
		else:
			print()
			print("====================================================")
			print(f"Total volume air yang dikeluarkan adalah : {total_volume:.2f}")
			print(f"Total harga yang harus dibayar adalah : Rp{total_harga:.2f}")
			print("====================================================")
			print()
			print("Terima kasih telah menggunakan Depot Air Minum Dek Depe")
			print()
			break

	#output jika input salah atau input case sensitive
	else:
		print("Input tidak benar, masukkan kembali")
		print()