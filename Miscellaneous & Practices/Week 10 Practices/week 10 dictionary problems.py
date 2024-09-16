#problem 1
# email = input("enter email: ")

# if "@" in email:
#     check_email = email.split("@")
#     domain = check_email[1]
    
#     if len(domain) == 0:
#         email = input("enter email: ")

#     elif domain == " ":
#         email = input("enter email: ")

# elif "@" not in email:
#     email = input("enter email: ")

# elif "." not in email:
#     email = input("enter email: ")


# def email_adress():
#     new_email = email.split("@")
#     username =  new_email[0]
#     domain = new_email[1]
#     my_tuple = username, domain
#     print(my_tuple)

# email_adress()

#problem 2
# user_input = input("enter a sentence: ")

# def word_count(user_input):
#     new_input = user_input.lower()
#     count = 0
#     dictionary = {}
#     lst_sentence = user_input.split()
    
#     for word in lst_sentence:
#         if word in dictionary:
#             count = dictionary[word]
#             count += 1
#             dictionary.update({word: count})
        
#         else:
#             count = 1
#             dictionary.update({word: count})
    
#     return dictionary

# print(word_count(user_input))

#problem 3
# user_input1, user_input2 = input("enter a string: "), input("enter a string: ")

# def sets_intersect(user_input1, user_input2):
#     word1 = user_input1.split()
#     word2 = user_input2.split()

#     set1 = set(word1)
#     set2 = set(word2)

#     return set1.intersection(set2)

# print(sets_intersect(user_input1, user_input2))

#problem 4
# d = {"ghana": 1, "daffa": 2, "dien":3}

# def dict_maker (dictionary, key, value):
#     if key in dictionary:
#         dictionary[key] = value
    
#     else:
#         dictionary.update({key: value})

#     return dictionary

# try:
#     key = int(input("enter key: "))
#     value = int(input("enter value: "))

# except:
#     key = input("enter key: ")
#     value = input("enter value: ")

# print(dict_maker(d, key, value))

#problem 5
# d = {"ghana": 18, "daffa": 18, "dien": 18, "widya": 18}
# e = {"andrew tate": 38, "messi": 10, "ronaldo": 37, "speed": 17}

# def dict_maker (dictionary, name):
#     if name in dictionary:
#         print(f"{name}'s age is {dictionary[name]}")
    
#     else:
#         age = int(input(f"enter {name}'s age: "))
#         dictionary.update({name: age})
#         print(f"here is the new dictionary: {dictionary}")

# name = input("enter name: ")

# dict_maker(d, name)

#problem 6
file = open("list_worst_cars.txt","r")
filelines = file.readlines()
d = {}

for line in filelines:
    word = line.split()
    year = word[0].strip()
    manufacturer = word[1].strip()
    model = line[line.find(word[1]) + len(word[1]):].strip()

    if manufacturer in d:
        d[manufacturer] += (year,model)

    else:
        d[manufacturer] = (year, model)

def max_cars(d):
    count = ""

    for key in d:
        if len(d[key]) > len(count):
            count = key

    return count

print()
print(f"this is the dictionary: {d}")
print()
print(f"this is the company that produced the most bad cars: {max_cars(d)}")
print()