#import turtle and random
import turtle
import random

#set up screen turtle
turtle.getscreen()
turtle.screensize(2560,1440)
turtle.speed(0) #set up turtle pace to fastest
turtle.bgcolor("green") 

#meminta input dari user melalui text box turtle
lower_bricks = (turtle.numinput("Input", "Masukkan jumlah batu bata lapisan bawah (maksimal 25)", minval=1, maxval=25))
#memvalidasi input user (jika float akan minta input lagi)
while lower_bricks %1 != 0: 
    lower_bricks = (turtle.numinput("Input", "Masukkan jumlah batu bata lapisan bawah (maksimal 25)", minval=1, maxval=25))

upper_bricks = (turtle.numinput("Input", "Masukkan jumlah batu bata lapisan atas (minimal 1)", minval=1, maxval=lower_bricks))
#memvalidasi input user (jika float akan minta input lagi)
while upper_bricks %1 != 0:
    upper_bricks = (turtle.numinput("Input", "Masukkan jumlah batu bata lapisan atas (minimal 1)", minval=1, maxval=lower_bricks))

brick_length = (turtle.numinput("Input", "Masukkan panjang satu batu bata (maksimal 35 piksel)", minval=1, maxval=35))
#memvalidasi input user (jika float akan minta input lagi)
while brick_length %1 != 0:
    brick_length = (turtle.numinput("Input", "Masukkan panjang satu batu bata (maksimal 35 piksel)", minval=1, maxval=35))

brick_width = (turtle.numinput("Input", "Masukkan lebar satu batu bata lapisan bawah (maksimal 25 piksel)", minval=1, maxval=25))
#memvalidasi input user (jika float akan minta input lagi)
while brick_width %1 != 0:
    brick_width = (turtle.numinput("Input", "Masukkan lebar satu batu bata lapisan bawah (maksimal 25 piksel)", minval=1, maxval=25))

#convert input ke integer
lower_bricks = int(lower_bricks)
upper_bricks = int(upper_bricks)
brick_length = int(brick_length)
brick_width = int(brick_width)

#set up variable untuk output jumlah batu bata
total_bricks = 0

#set up posisi turtle setiap naik layer dan mulai membuat candi
for i in range (0, lower_bricks - upper_bricks + 1):
    turtle.penup()
    turtle.setposition(((-(lower_bricks - i) * brick_length) // 2), (-((lower_bricks - upper_bricks) // 2 - i) * brick_width ))
    turtle.pendown()

    #loop membuat batu bata bagian bawah
    if(lower_bricks - i == lower_bricks):
        for b in range (0, lower_bricks - i):
            turtle.fillcolor("#BC4A3C")
            turtle.begin_fill()
            turtle.forward(brick_length)
            turtle.left(90)
            turtle.forward(brick_width)
            turtle.left(90)
            turtle.forward(brick_length)
            turtle.left(90)
            turtle.forward(brick_width)
            turtle.left(90)
            turtle.forward(brick_length)
            turtle.end_fill()

    #loop untuk membuat batu bata warna warni
    elif(lower_bricks - i != upper_bricks):
        #berawal dari batu bata warna merah bata
        turtle.fillcolor("#BC4A3C")
        turtle.begin_fill()
        turtle.forward(brick_length)
        turtle.left(90)
        turtle.forward(brick_width)
        turtle.left(90)
        turtle.forward(brick_length)
        turtle.left(90)
        turtle.forward(brick_width)
        turtle.left(90)
        turtle.forward(brick_length)
        turtle.end_fill()

        #membuat batu bata tengah warna warni
        for b in range(0, (lower_bricks-i) - 2):
            #membuat variabel untuk generate random number untuk mendapatkan random color
            turtle.colormode(255)
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            rand_color = r,g,b

            turtle.fillcolor(rand_color)
            turtle.begin_fill()
            turtle.forward(brick_length)
            turtle.left(90)
            turtle.forward(brick_width)
            turtle.left(90)
            turtle.forward(brick_length)
            turtle.left(90)
            turtle.forward(brick_width)
            turtle.left(90)
            turtle.forward(brick_length)
            turtle.end_fill()
        
        #diakhiri dengan batu bata warna merah
        turtle.fillcolor("#BC4A3C")
        turtle.begin_fill()
        turtle.forward(brick_length)
        turtle.left(90)
        turtle.forward(brick_width)
        turtle.left(90)
        turtle.forward(brick_length)
        turtle.left(90)
        turtle.forward(brick_width)
        turtle.left(90)
        turtle.forward(brick_length)
        turtle.end_fill()

    #loop membuat batu bata bagian atas
    elif(lower_bricks - i == upper_bricks):
        for b in range (0, lower_bricks - i):
            turtle.fillcolor("#BC4A3C")
            turtle.begin_fill()
            turtle.forward(brick_length)
            turtle.left(90)
            turtle.forward(brick_width)
            turtle.left(90)
            turtle.forward(brick_length)
            turtle.left(90)
            turtle.forward(brick_width)
            turtle.left(90)
            turtle.forward(brick_length)
            turtle.end_fill()

    turtle.penup()

#menghitung jumlah batu bata
for b in range (0, lower_bricks - upper_bricks + 1):
    total_bricks += lower_bricks
    lower_bricks -= 1

#mencetak output total batu bata
turtle.setposition (0,(-(brick_width * ((lower_bricks - upper_bricks) // 2 + 10)) - 30)) #set up posisi akhir turtle untuk mencetak output
turtle.write(f"Candi warna-warni dengan {total_bricks} batu bata", align = "center", font = ("Times New Roman","20"))
turtle.hideturtle()
turtle.done()

#Collaborator: 2206082114 - Clement Samuel Marly, 2206082751 - Yosef Nuraga Wicaksana                                           