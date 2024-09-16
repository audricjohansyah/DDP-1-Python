#import math
import math

#ask input
name = input("Nama: ")
n = float(input("Panjang persegi nametag (cm) "))
m = float(input("Panjang trapesium nametag (cm) "))
s = int(input("Banyak nametag: "))

#equations for area of nametag
square =(n*n)
sq = round(square,2)

half_circle = 0.5*math.pi*((0.5*n)**2)
hc = round(half_circle,2)
        
trapezium =((n+m)*n)/2
tz = round(trapezium,2)

triangle =(n*n)/2
tr = round(triangle,2)

total_area_1 = sq + hc+ tz + tr
total_area_all = round(s*total_area_1,2)

#counting the money
pay_me = math.ceil((total_area_all*0.40) / 1000)*1000

#output
print(" ")
print("Halo, " + name + "! Berikut informasi terkait nametag kamu: ")
print("Luas 1 nametag: " + str(total_area_1) + " cm^2")
print("Luas total nametag: " + str(total_area_all) + " cm^2")
print("Uang yang diperlukan: Rp" + str(pay_me))




