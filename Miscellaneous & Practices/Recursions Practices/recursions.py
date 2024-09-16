# practice 1
def power(a, b):
    if b == 0:
        return 1

    return a*(power(a,b-1))

a = int(input("number plis: "))
b = int(input("number again plis: "))
print(power(a, b))

# practice 2
def length_list(lst):
    if lst == []:
        return 0

    else:
        return 1 + length_list(lst[1:])

lst = ["speed", "lol", "andrew tate", "steven", "messi", "harry", "josh", "simon"]
print(length_list(lst))

# practice 3
def sum_digit(a):
    if a == 0:
        return 0

    return a%10 + sum_digit(a//10)

print(sum_digit(198826))

# practice 4
def palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    elif word[0] != word [-1]:
        return False
    else:
        return palindrome(word[1:-1])
    
print(palindrome("hannah"))

#practice 5
def gcd(a,b):
    if a == 0:
        return b

    else:
        return gcd(b%a, a)

print(gcd(36,60))

# practice 6
def reverse(word):
    if len(word) == 1 or len(word) == 0:
        return word[::-1]

    else:
        return word[-1] + reverse(word[:-1])

print(reverse("flash"))

# practice 7
def max (lst):
    if lst == []:
        return None

    if len(lst) == 1:
        return lst[0]

    if lst[0] > lst[1]:
        lst[1] = lst[0]

    return (max(lst[1:]))

lst = [3,4,6,7,9,2,1]
print(max(lst))