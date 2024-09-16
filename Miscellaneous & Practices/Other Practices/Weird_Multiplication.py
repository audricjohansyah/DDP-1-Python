#welcome statement
print("Russian Peasant / Ancient Egyptian multiplication")

#asking for input
a = int(input("Please enter a number: ")) #mau dikali 2
b = int(input("Please enter another number: ")) #mau dibagi 2
product = 0

#looping with conditional statements
while b > 0:
    if b%2 != 0:
        product += a
    a *= 2
    b = b // 2
print(product) #output