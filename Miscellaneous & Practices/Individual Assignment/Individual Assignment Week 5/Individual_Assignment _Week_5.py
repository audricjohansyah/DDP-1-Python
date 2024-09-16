#import random
import random

file_name = open(input("Masukkan file yang akan discramble: "),"r") #meminta input file
output_file = open("output.txt", "w") #output file
file = file_name.readlines() 

#set up variable
tanda_baca = (".", ";", "!", "?", ",")
new_word = ""
sentence = ""

for line in file:
    kata = line.split() #memisahkan string dan dimasukkan dalam list
    
    for word in kata: #mengambil string yang ada di list
        
        #jika kata-kata terdiri lebih dari 3 huruf
        if(len(word)) > 3:

            #jika kata-kata terdiri lebih dari 3 huruf dan diakhiri dengan tanda baca
            if word.endswith(tanda_baca):
                new_word = word[1:-2] #membuang huruf pertama, huruf terakhir, dan tanda baca
                new_word = random.sample(new_word, len(new_word)) #mengacak kata
                new_word.insert(0, word[0]) #memasukkan huruf pertama
                new_word.append(word[-2]) #memasukkan huruf terakhir
                new_word.append(word[-1]) #memasukkan tanda baca

            #jika kata-kata terdiri lebih dari 3 huruf dan tidak diakhiri dengan tanda baca
            else:
                new_word = word[1:-1] #membuang huruf pertama dan huruf terakhir
                new_word = random.sample(new_word, len(new_word)) #mengacak kata
                new_word.insert(0, word[0]) #memasukkan hurus pertama
                new_word.append(word[-1]) #memasukkan huruf terakhir
            
            sentence = sentence + ''.join(new_word) + " "
        
        #jika kata-kata tidak terdiri lebih dari 3 huruf
        else:
            sentence = sentence + word + " "   
    
    #agar setiap kalimat dicetak dibawah dan tidak satu baris
    sentence = sentence + "\n"

#mencetak output   
print(sentence, file = output_file)

#Collaborator: Kak Bryan Naufal