#import sys dan os
import os
import sys

#minta input user di terminal dan import ke program
user_input = sys.argv

#function untuk mencetak output jika error
def argumen_error():
    print("Argumen program tidak benar.")
    exit()

#function untuk mengecek input wildcard
def wildcard_check():
    if "*" in kata:
        check_kata = kata.split("*")
        
        if len(check_kata) > 2:
            argumen_error()

#memvalidasi input dari user
if len(user_input) <= 4:
    if "-w" in user_input and "-i" in user_input:
        argumen_error()
    
    elif "-w" in user_input or "-i" in user_input:
        #meng-index input user
        if len(user_input) == 4:
            py_file = user_input[0]
            options = user_input[1]
            kata = user_input[2]
            file_input = user_input[3]
            wildcard_check()

        else:
            argumen_error()

    elif "-w" not in user_input and "-i" not in user_input:
        #mengindex input user
        if len(user_input) == 3:
            py_file = user_input[0]
            options = "no option"
            kata = user_input[1]
            file_input = user_input[2]
            wildcard_check()

        else:
            argumen_error()

    else:
        argumen_error()

elif len(user_input) < 3:
   argumen_error()

elif len(user_input) > 4:
    argumen_error()

#function cetak output
def print_output():
    print(f"{location[:40]:<40}     line {i + 1:<3}     {new_line[:40]:<40}")

#function untuk mengecek file 
def scanning ():
    #jika tidak ada * dalam kata (bukan wildcard)
    if "*" not in kata:
    #jika argumen no option
        if options == "no option":
            if kata in new_line:
                print_output() #jika kata yang kita cari ada, akan diprint kalimat (case sensitive)

        #jika argumen option -i
        elif options == "-i":
            if kata.lower() in new_line.lower(): #membuat kata dan kalimat menjadi case insensitive
                print_output() #jika kata yang kita cari ada, akan diprint kalimat

        #jika argumen option -w
        if options == "-w":
            for word in new_line.split(): #dicek per wholeword (kata diantara whitespace) secara case sensitive
                if kata == word:
                    print_output() #jika kata yang kita cari ada, akan diprint kalimat

    #jika ada * dalam kata (wildcard)
    if "*" in kata:
        new_kata = kata.split("*")
        kata_1 = new_kata[0]
        kata_2 = new_kata[1]

        #jika argumen no option
        if options == "no option":
            #mencari index kata yang ingin dicari secara case sensitive
            index_1 = new_line.find(kata_1)
            index_2 = new_line.find(kata_2)
            if kata_1 in new_line and kata_2 in new_line and (index_1 + len(kata_1) -1) < index_2:
                print_output() #jika kata yang kita cari ada, akan diprint kalimat
        
        #jika argumen option -i
        elif options == "-i":
            #membuat kata dan kalimat menjadi case insensitive
            kata_1 = kata_1.lower()
            line_caseinsensitive = new_line.lower()
            kata_2 = kata_2.lower()
            #mencari index kata yang ingin dicari
            index_1 = line_caseinsensitive.find(kata_1)
            index_2 = line_caseinsensitive.find(kata_2)

            if kata_1 in line_caseinsensitive and kata_2 in line_caseinsensitive and (index_1 + len(kata_1) -1) < index_2:
                print_output() #jika kata yang kita cari ada, akan diprint kalimat

        #jika argumen option -w
        elif options == "-w":    
            for word in new_line.split(): #dicek per kata (wholeword: kata diantara whitespace) secara case sensitive
            
                #slicing kata yang mau dicari
                word_1 = word[:len(kata_1)]
                word_2 = word[:-(len(kata_2))-1:-1]
                word_2 = word_2[::-1]

                if kata_1 == word_1 and kata_2 == word_2:
                    print_output() #jika kata yang kita cari ada, akan diprint kalimat

try:
    #jika input directory
    if os.path.isdir(file_input):
    #loop untuk membuka file
        for dirpath, dirnames, filenames in os.walk(file_input):
            #membaca setiap file
            for file in filenames:
                location = os.path.join(dirpath, file)
                file = open(location, "r")
                file_lines = file.readlines() 
                
                #membaca setiap line di dalam file    
                for i in range (len(file_lines)):
                    file_read = file_lines[i].split()
                    file_read = " ".join(file_read)
                    new_line = file_read

                    scanning()

    #jika input bukan directory
    else:
        #membuka file
        location = file_input
        file = open(location, "r")
        file_lines = file.readlines()

        #membaca setiap line di dalam file 
        for i in range (len(file_lines)):
            file_read = file_lines[i].split()
            file_read = " ".join(file_read)
            new_line = file_read
            
            scanning()

except FileNotFoundError: #jika file tidak ditemukan
    print(f"Path {location} tidak ditemukan")

#Collaborator: 2206082114 - Clement Samuel Marly, 2206082751 - Yosef Nuraga Wicaksana
#Referensi: (https://docs.python.org/3/library/os.html), (https://www.geeksforgeeks.org/os-module-python-examples/), (https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/), (https://www.w3schools.com/python/ref_string_find.asp)