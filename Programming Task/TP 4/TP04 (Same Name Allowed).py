# import modul
import random
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkmsg

#data library, set up awal
desk_number = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10] #list nomor meja
temp_desk_list, check_menu = [], [] #list perantara nomor meja dan list check menu
dict_desk = {1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:""} #menyimpan customer
dict_menu, dict_jumlah_pesanan = {}, {} #dictionary menu dengan key kode dan dictionary untuk menampung jumlah pesanan

#main window
class Main(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.geometry("400x200")
        self.pack()
        master.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        button1 = tk.Button(self, text="Buat Pesanan", width=30, command=self.buat_pesanan, bg="#4472C4", fg="white") #tombol buat pesanan
        button2 = tk.Button(self, text="Selesai Gunakan Meja", width=30, command=self.selesai_gunakan_meja, bg="#4472C4", fg="white") #tombol selesai gunakan meja
        button1.grid(row=0, column=0, padx=10, pady=40)
        button2.grid(row=1, column=0)
        
    def buat_pesanan(self): #fungsi untuk menjalankan command buat pesanan
        BuatPesanan(self.master)

    def selesai_gunakan_meja(self): #fungsi untuk menjalankan command buat pesanan
        SelesaiGunakanMeja(self.master)

#buat pesanan
class BuatPesanan(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("400x175")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.lbl_nama = tk.Label(self, text="Siapa nama Anda?")
        self.lbl_nama.grid(column=0, row=0, pady=(50,0), padx=(50,0))
        self.nama_customer = tk.StringVar() #meminta input nama dari user
        self.entry_name = tk.Entry(self, textvariable=self.nama_customer) #memasukkan nama melalui entry widget
        self.entry_name.grid(column=1, row=0, padx=(30,0), pady=(50,0))
        self.lanjut_button = tk.Button(self,text= "Lanjut", bg= "#4472C4", fg="white",width=20, command=self.lanjut) #tombol lanjut
        self.lanjut_button.grid(column=1, row=1, padx=(30,0), pady=(30,0))
        self.kembali_button = tk.Button(self,text="Kembali", bg="#4472C4", fg="white", width=20, command=self.kembali) #tombol kembali
        self.kembali_button.grid(column=0, row=1, padx=(30,0), pady=(30,0))
        self.mainloop()

    def kembali(self): #fungsi untuk menjalankan command kembali
        self.destroy()

    def lanjut(self): #fungsi untuk menjalankan command lanjut
        if len(desk_number) == 0: #mengecek meja penuh atau tidak
            tkmsg.showinfo(title="Kafe Daun-Daun Pacilkom v2.0 🌿", message="Mohon maaf, meja sedang penuh. Silakan datang kembali di lain kesempatan.")
            self.destroy()

        else:
            # if self.nama_customer.get() not in dict_desk.values(): #mengecek jika user memasukkan nama yang sama dengan user lainnya
            nomor_meja = random.choice(desk_number) #dapat nomor meja dari list nomor meja yang tersedia
            temp_desk_list.append(nomor_meja) #menambahkan nomor meja ke list perantara
            desk_number.remove(nomor_meja) #menghapus nomor meja dari list nomor meja tersedia
            dict_desk[nomor_meja] = self.nama_customer.get() #memasukkan customer ke dalam dictionary berdasarkan nomor meja
            self.destroy()
            Table(self.master, list_menu) #memanggil table menu
            # else:
            #     tkmsg.showinfo(title="Kafe Daun-Daun Pacilkom v2.0 🌿", message="Mohon gunakan nama yang berbeda.")

class Table(tk.Toplevel):
    def __init__(self, master, data):
        super().__init__(master)
        self.geometry("800x350")
        self.total = 0 #variable untuk total harga
        self.data = data #list menu
        self.total_rows = len(self.data)
        self.total_columns = 5
        self.generate_table()

    def generate_table(self):
        self.entry_name = tk.Label(self, text=f"Nama pemesan: {dict_desk[temp_desk_list[0]]}", font="Helvetica 10 bold") #menunjukkan nama pemesan
        self.entry_name.grid(column = 0, row = 0)
        self.entry_desk = tk.Label(self, text=f"No Meja: {temp_desk_list[0]}", font="Helvetica 10 bold") #menunujukkan nomor meja
        self.entry_desk.grid(column = 4, row= 0)
        self.total_harga = tk.Label(self, text=f"Total harga: {self.total}", font="Helvetica 10 bold") #menunjukkan total harga
        self.total_harga.grid(column=(5//2 +2), row=len(self.data)+1)
        self.ubah_meja = tk.Button(self, text="Ubah", bg="#4472C4", fg="white", command=self.ubahmeja, width=10) #tombol ubah nomor meja
        self.ubah_meja.grid(column=5, row=0)
        self.kembali_command = tk.Button(self, text="Kembali", bg="#4472C4", fg="white", width=20, command=self.kembali) #tombol kembali
        self.kembali_command.grid(column=(5//2 - 1), row=len(self.data)+3)
        self.lanjut_command = tk.Button(self, text="OK", bg="#4472C4", fg="white", width=20, command=self.lanjut) #tombol ok (lanjut)
        self.lanjut_command.grid(column=(5//2 + 1), row=len(self.data)+3)

        #mencetak table menu
        for i in range(self.total_rows):
            if isinstance(self.data[i], list): #mengecek list menu yang bukan header
                if len(self.data[i]) != 5:
                    for j in range(self.total_columns - 1):
                        kode = self.data[i][0] #kode menu
                        entry = tk.Entry(self, width = 20)
                        entry.grid(row = i+1, column = j)
                        entry.insert(tk.END, self.data[i][j])
                        entry['state'] = 'readonly'
                        values = tuple([k for k in range(11)])
                        opsi_jumlah = ttk.Combobox(self, values = values, width=20)
                        opsi_jumlah.bind("<<ComboboxSelected>>", lambda event, x=kode:self.combobox(event, x))
                        opsi_jumlah.grid(row = i+1, column = self.total_columns - 1)
                else:
                    for j in range(self.total_columns):
                        entry = tk.Entry(self, width = 20)
                        entry.grid(row = i+1, column = j)
                        entry.insert(tk.END, self.data[i][j])
                        entry['state'] = 'readonly'
                        
            else: #header dari list menu (meals, drinks, sides)
                entry = tk.Label(self, text= self.data[i], width = 20)
                entry.grid(column = 0, row=i+1)
    
    #fungsi combobox untuk mencetak total harga
    def combobox(self, event, x):
        self.total = 0 #mereset total harga
        jumlah = int(event.widget.get())
        dict_jumlah_pesanan[x] = jumlah
        for key in dict_jumlah_pesanan:
            harga = dict_menu[key][1] #mendapatkan harga menu
            sum = dict_jumlah_pesanan[key] #mendapatkan jumlah menu
            self.total += harga*sum #evaluasi harga total
        self.total_harga["text"] = f"Total harga: {self.total}" #mengupdate label total harga

    #fungsi untuk menjalankan command OK
    def lanjut(self):
        if self.total == 0: #mengecek jika kita belum memesan apa-apa
            tkmsg.showwarning(title="Kafe Daun-Daun Pacilkom v2.0 🌿", message="Anda belum memesan apa-apa.")
        else:
            temp_desk_list.remove(temp_desk_list[0]) #menghapus nomor meja dari list perantara
            self.destroy()

    #fungsi untuk menjalankan command Kembali
    def kembali(self):
        dict_desk[temp_desk_list[0]] = "" #menghapus nama customer dari dictionary customer
        desk_number.append(temp_desk_list[0]) #mengembalikkan nomor meja customer
        desk_number.sort() #mengurutkan list nomor meja
        temp_desk_list.remove(temp_desk_list[0]) #menghapus nomor meja dari list perantara
        self.destroy()
    
    #fungsi untuk menjalankan command ubah meja
    def ubahmeja(self):
        Meja(self.master, self.entry_desk)

#mengubah nomor meja
class Meja(tk.Toplevel):
    def __init__(self, master, entry_desk):
        super().__init__(master)
        self.geometry("475x400")
        self.meja_awal = temp_desk_list[0] #menyimpan meja awal
        self.entry_desk = entry_desk #label tampilan nomor meja
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.customer = dict_desk[temp_desk_list[0]] #nama customer
        self.change_table()

    def change_table(self):
        global list_button
        list_button = [] #membuat suatu list berisi object button
        for key in dict_desk: #membuat button meja
            if dict_desk[key] == "": #jika meja belum ditempati
                self.color = "grey"
                self.state = "normal"
                button = tk.Button(self, text=f"{key}", width=10, bg=self.color, command=lambda x=key: self.ubah_nomor(x), state=self.state, fg="black")
                if key <= 5:
                    button.grid(column=0, row=key, padx=(10,0),pady=(10,0))
                else:
                    button.grid(column=1, row=key-5, padx=(0,10),pady=(10,0))

            elif key == temp_desk_list[0]: #jika meja ditempati customer
                self.color = "#4472C4"
                self.state = "disabled"
                button = tk.Button(self, text=f"{key}", width=10, bg=self.color, command=lambda x=key:self.ubah_nomor(x), state=self.state, fg="black")
                if key <= 5:
                    button.grid(column=0, row=key, padx=(10,0),pady=(10,0))
                else:
                    button.grid(column=1, row=key-5, padx=(0,10),pady=(10,0))

            else: #jika meja ditempati customer lain
                self.color = "red"
                self.state = "disabled"
                button = tk.Button(self, text=f"{key}", width=10, bg=self.color, command=lambda x=key: self.ubah_nomor(x), state=self.state, fg="black")
                if key <= 5:
                    button.grid(column=0, row=key, padx=(20,0),pady=(20,0))
                else:
                    button.grid(column=1, row=key-5, padx=(0,20),pady=(20,0))

            list_button.append(button)

        self.info_header =tk.Label(self, text= "Silahkan klik meja kosong yang diinginkan:")
        self.info_header.grid(column=0, row=0, pady=(10,0),padx=(30,0))

        #label keterangan meja
        self.info_label =tk.Label(self, text= "Info", font="Helvetica 8 bold")
        self.info_label.grid(column=0, row=7, pady=(20,0), padx=(30,0), columnspan=2)
        self.info_merah =tk.Label(self, text= "Merah = Terisi", font="Helvetica 8 bold")
        self.info_merah.grid(column=0, row=8, padx=(30,0), columnspan=2)
        self.info_abu =tk.Label(self, text= "Abu-abu = Kosong", font="Helvetica 8 bold")
        self.info_abu.grid(column=0, row=9, padx=(30,0), columnspan=2)
        self.info_biru =tk.Label(self, text= "Biru = Meja anda", font="Helvetica 8 bold")
        self.info_biru.grid(column=0, row=10, padx=(30,0), pady=(0,20), columnspan=2)

        self.kembali_option = tk.Button(self, text="Kembali", bg="#4472C4", fg="white", width=20,command=self.kembali) #tombol kembali
        self.kembali_option .grid(column=0, row=25, padx=(20,10))
        self.lanjut_option  = tk.Button(self, text="OK", bg="#4472C4", fg="white", width=20, command=self.ok) #tombol ok
        self.lanjut_option .grid(column=1, row=25, padx=(10,20))

    #fungsi untuk menjalankan command dari button meja
    def ubah_nomor(self, n):
        list_button[n-1]["bg"] = "#4472C4" #mengubah warna button meja yang dipilih menjadi biru
        list_button[n-1]["state"] = "disabled" #mengubah kondisi button yang dipilih menjadi disabled
        list_button[temp_desk_list[0]-1]["bg"] = "grey" #mengubah warna button lama menjadi abu-abu
        list_button[temp_desk_list[0]-1]["state"] = "normal" #mengubah kondisi button lama menjadi normal
        desk_number.append(temp_desk_list[0]) #mengembalikkan nomor meja lama ke dalam list nomor meja
        temp_desk_list[0] = n #mengubah nomor meja awal menjadi baru
        desk_number.remove(temp_desk_list[0]) #menghapus nomor meja baru dari list nomor meja
        desk_number.sort() #mengurutkan list nomor meja
        dict_desk[self.meja_awal] = "" #membuang customer dari dictionary customer di nomor meja awal

    #fungsi untuk menjalankan command ok
    def ok(self):
        dict_desk[temp_desk_list[0]] = self.customer #menyimpan customer di dictionary customer
        self.entry_desk["text"] = f"No Meja: {temp_desk_list[0]}" #mengupdate label nomor meja
        self.destroy()

    #fungsi untuk menjalankan command kembali
    def kembali(self): #mengecek
        if self.meja_awal != temp_desk_list[0]: #mengecek jika user mengubah nomor mejanya (user mengubah nomor meja tetapi memencet tombol kembali)
            desk_number.append(temp_desk_list[0]) #mengembalikkan nomor meja baru ke dalam list nomor meja
            dict_desk[temp_desk_list[0]] = "" #membuang customer dari dictionary customer di nomor meja baru
            temp_desk_list[0] = self.meja_awal #mengubah nomor meja baru menjadi awal
            dict_desk[temp_desk_list[0]] = self.customer #memasukkan customer ke dictionary customer di nomor meja awal
            desk_number.remove(temp_desk_list[0]) #membuang nomor meja awal dari list nomor meja
            desk_number.sort() #mengurutkan list
            self.destroy()

        else: #user tidak mengubah nomor meja dan memencet tombol kembali
            self.destroy()

#selesai menggunakan meja
class SelesaiGunakanMeja(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.geometry("450x350")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.lbl_command = tk.Label(self, text="Silakan klik meja yang selesai digunakan:") 
        self.lbl_command.grid(column=0, row=0, padx=(20,0), pady=(10,0))
        self.show_table()
        self.mainloop()

    #fungsi membuat button meja
    def show_table(self):
        global list_button
        list_button = [] #membuat list button
        for key in dict_desk: #membuat button meja
            if dict_desk[key] == "": #mengecek meja kosong atau tidak
                self.color = "grey"
                self.state = "disabled"
                button = tk.Button(self, text=f"{key}", width=10, bg=self.color, state=self.state, fg="black")
                if key <= 5:
                    button.grid(column=0, row=key, padx=(10,0),pady=(10,0))
                else:
                    button.grid(column=1, row=key-5, padx=(0,10),pady=(10,0))

            else: #jika meja ditempati
                self.color = "red"
                self.state = "normal"
                button = tk.Button(self, text=f"{key}", width=10, bg=self.color, command=lambda x=key: self.selesai_nomor(x), state=self.state, fg="black")
                if key <= 5:
                    button.grid(column=0, row=key, padx=(10,0),pady=(10,0))
                else:
                    button.grid(column=1, row=key-5, padx=(0,10),pady=(10,0))

            list_button.append(button)

        #label keterangan
        self.info_label =tk.Label(self, text= "Info", font="Helvetica 10 bold")
        self.info_label.grid(column=0, row=7, pady=(20,0), padx=(10,0))
        self.info_merah =tk.Label(self, text= "Merah = Terisi", font="Helvetica 10 bold")
        self.info_merah.grid(column=0, row=8, padx=(10,0))
        self.info_abu =tk.Label(self, text= "Abu-abu = Kosong", font="Helvetica 10 bold")
        self.info_abu.grid(column=0, row=9, padx=(10,0))

        self.kembali_btn = tk.Button(self, text="Kembali", bg="#4472C4", fg="white", width=20, command=self.kembali) #tombol untuk kembali
        self.kembali_btn.grid(column=1, row=8, padx=(0,20))

    #fungsi untuk menjalankan command button meja
    def selesai_nomor(self, n):
        desk_number.append(n) #mengembalikkan nomor meja ke dalam list nomor meja
        desk_number.sort() #mengurutkan list
        dict_desk[n] = "" #membuang customer dari dictionary customer berdasarkan nomor meja
        self.destroy()

    #fungsi untuk menjalankan command kembali
    def kembali(self):
        self.destroy()

def main():
    global list_menu
    list_menu = [] #membuat suatu list berisi menu
    with open('menu.txt', 'r') as f: #membuka file menu txt
        lines = f.read().splitlines()
        try: #validasi menu
            for line in lines:
                if "===" in line:
                    kategori = line[3:]
                    list_menu.append(kategori) #memasukkan kategori ke dalam list menu
                    #memasukkan header dalam list menu
                    if kategori == "MEALS":
                        list_menu.append(["Kode", "Menu", "Harga", "Kegurihan", "Jumlah"]) 
                    elif kategori == "DRINKS":
                        list_menu.append(["Kode", "Menu", "Harga", "Kemanisan", "Jumlah"])
                    elif kategori == "SIDES":
                        list_menu.append(["Kode", "Menu", "Harga", "Keviralan", "Jumlah"])

                else:
                    kode_menu, nama_menu, harga, info_menu = line.split(";")
                    harga = int(harga)

                    if harga <= 0:
                        print("Daftar menu tidak valid, cek kembali menu.txt!")
                        exit()
                    if kode_menu not in check_menu and nama_menu not in check_menu: #memasukkan makanan ke dalam list menu
                        dict_menu[kode_menu] = [nama_menu, harga, info_menu, kategori] #memasukkan makanan dalam dictionary
                        list_menu.append([kode_menu, nama_menu, harga, info_menu])
                        check_menu.extend((kode_menu, nama_menu))
                    else:
                        print("Daftar menu tidak valid, cek kembali menu.txt!")
                        exit()
        except:
             print("Daftar menu tidak valid, cek kembali menu.txt!")
             exit()

    window = tk.Tk()
    cafe = Main(window)
    window.mainloop()

if __name__ == '__main__':
    main()

#Collaborator: 2206082114 - Clement Samuel Marly, 2206082751 - Yosef Nuraga Wicaksana
#References: https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/, https://www.geeksforgeeks.org/python-grid-method-in-tkinter/, https://www.geeksforgeeks.org/combobox-widget-in-tkinter-python/, https://www.etutorialspoint.com/index.php/347-python-tkinter-ttk-combobox-event-binding, https://stackoverflow.com/questions/40641130/how-to-use-a-comboboxselected-virtual-event-with-tkinter, https://zetcode.com/python/lambda/