# var_1 = int("5")
# var_2 = int("7")

# if (var_1 < 1 and var_1 > 3) or var_1 == 5:
#     print("Wadaw")
# else:
#     print("Wadidaw")

# if var_1 < 1 and (var_2 > 3 or var_1 == 5):
#     print("Wadaw")
# else:
#     print("Wadidaw")

# if var_1 < 1 and var_2 > 3 or var_1 == 5:
#     print("Wadaw")
# else:
#     print("Wadidaw")

# CASE 1
# def make_bricks(small,big,goal):
#     if ( small*1 ) + (big*5) >= goal :
#         return True
#     else: return False

# print(make_bricks(3, 1, 8))
# print(make_bricks(3, 1, 9))
# print(make_bricks(3, 2, 10))

# CASE 2
# def lone_sum(a,b,c):
#     if a != b and a != c and b != c:
#         return a+b+c
#     elif a == b == c:
#         return 0
#     elif a == b:
#         return c
#     elif a == c:
#         return b
#     elif b==c:
#         return a

# print(lone_sum(1, 2, 3))
# print(lone_sum(3, 2, 3))
# print(lone_sum(3, 3, 3))
# print(lone_sum(1, 4, 4))

# CASE 3
# def close_fat(a,b,c):
#     if abs(a-b) < 2 and abs(c-b) >2 :
#         return True
#     elif  abs(a-c) < 2 and ( abs(b-c) > 2 or abs(b-a) > 2):
#         return True
#     elif abs(b-c) < 2 and ( abs(a-b) > 2 or abs(c-b) >2): 
#         return True
#     else: return False

# print(close_fat(1, 2, 10))
# print(close_fat(1, 2, 3))
# print(close_fat(4, 1, 3))
# print(close_fat(5, 8, 9))

# CASE 5
# def make_chocolate(small,big,goal):
#     if small*1 + big*5 >= goal:
#         return goal - (big*5)
#     else: return -1

# print(make_chocolate(4, 1, 9))
# print(make_chocolate(4, 1, 10))
# print(make_chocolate(4, 1, 7))

def fix_teen(n):
    if n == 15:
        return 15
    elif n == 16:
        return 16
    elif n>=13 and n<=19:
        return 0
    else: return n

def no_teen_sum(a,b,c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))