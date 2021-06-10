#QUESTION_1
n = int(input("enter the number : "))
a = []
for i in range(n):
    a.append(i + 1)
print(a)
a.reverse()
print(a)

#QUESTION_2
n = int(input("Enter the number: "))
if 1 < n < 100:

    print("Even nos. : ")
    for i in range(1, n + 1):
        if (i % 2 == 0):
            print(i, end=" ")
print(end="\n")
print("odd nos. : ")
for i in range(1, n + 1):
    if (i % 2 != 0):
        print(i, end=" ")

else:
    pass

#QUESTION_3
n = int(input())
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print("False")
            break
    else:
        print("True")
else:
    print("is not prime number")

#QUESTION_4
n = int(input("enter a number : "))
sum = 0
for i in range(n + 1):
    if (i % 3 == 0) or (i % 5 == 0):
        print(i, end=" ")

        sum = sum + i
print(end="\n")
print("sum : ", sum)

#QUESTION_5
n = int(input("Enter any number : "))
print("Please Choose any one the options : ")
print("Sum", end="\n")
print("Product", end="\n")

choice = input()
if (choice == "sum" or choice == "SUM" or choice == "Sum"):
    mysum()

elif (choice == "product" or choice == "PRODUCT" or choice == "Product"):
    product()

else:
    print("Wrong option ")


def mysum():
    count = 0
    for i in range(n + 1):
        count = count + i
    print(count)


def product():
    multiply = 1
    for i in range(n):
        multiply = multiply * (i + 1)
    print(multiply)


#QUESTION_6
sum = 0
for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        sum = sum + i
print("sum : ", sum)

#QUESTION_7
print("numbers : ")
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        print(i, end=" ")

#QUESTION_8
s = range(0, 101)
a = int(sum(s))
print(a * a - sum(i * i for i in s))

#QUESTION_9
n = int(input("Enter a number : "))
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)
print("Factorial of ", n, "is : ", fact(n))

#QUESTION_10
n = 5
for i in range(n + 1):
    for j in range(i):
        print(i, end=" ")
    print("\n")

n = 5
for i in range(n):
    for j in range(n):
        print(max(i + 1, j + 1, n - i, n - j), end=" ")
    print()
n = 5
for i in range(n + 1):
    print("")
    for j in range(i):
        print("*", end=" ")
print("")
n = 4
for i in range(n + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end="")
    print(" ")

n = 5
for i in range(n - 1):
    print("#" * n)
print("#" * (n))

#QUESTION_11
n = int(input("Enter a number : "))

n1 = str(n) * 1
n2 = str(n) * 2
n3 = str(n) * 3
n4 = str(n) * 4
print("The sum is : ", n1, "+", n2, "+", n3, "+", n4, "=")
mysum = int(n1) + int(n2) + int(n3) + int(n4)
print(mysum)

#QUESTION_12
n = input("Enter name : ")
def length(n):
    count = 0
    for i in n:
        count = count + 1
    return count
print(length(n))

#QUESTION_13
n = input("Sentence : ")
d = l = 0
for i in n:
    if i.isdigit():
        d = d + 1
    elif i.isalpha():
        l = l + 1
    else:
        pass
print("Letter : ", l)
print("Digits : ", d)

#QUESTION_14
n = input("String : ")
for i in n:
    if i.isalpha():
        print(i.capitalize(), end="")

#QUESTION_15
n = input("sentense : ")
u = l = 0
for i in n:
    if i.isupper():
        u = u + 1
    elif i.islower():
        l = l + 1
    else:
        pass
print("Upper Case :  ", u)
print("Lower Case :  ", l)

#QUESTION_16
n = input("Sentence : ")
m = input("Character : ")
count = 0
print("number of characters : ")
for i in n:
    if i == m:
        count = count + 1
print(str(count))

#QUESTION_17
n = input("String : ")
def mypalindrome(n):
    return n == n[::-1]
temp = mypalindrome(n)
if temp:
    print("Palindrome")
else:
    print("Not a Palindrome")

#QUESTION_18
s1 = input("String 1 : ")
s2 = input("String 2 : ")


def finder(s1, s2):
    if (s1.find(s2) == -1):
        print("Not a substring")
    else:
        print("It's a substring")
finder(s1, s2)

#QUESTION_19
print("While Registering please keep in mind the following\n")
print("Criteria for the password: \n",

      "1.Password should have At least 1 letter between [a-z] \n",

      "2.Password should have At least 1 number between [0-9] \n",

      "3.Password should have At least 1 letter between [@$#%&] \n")


def password_check(passwd):
    SpecialSym = ['@', '$', '#', '%', '&']
    val = True

    if not any(char.isdigit() for char in passwd):
        print("Password should have At least 1 number between [0-9] ")
        val = False

    if not any(char.isalpha() for char in passwd):
        print("Password should have At least 1 letter between [a-z] ")
        val = False

    if not any(char in SpecialSym for char in passwd):
        print("Password should have At least one of the symbols [@$#%&] ")
        val = False
    if val:
        return val


username = input("Enter Username Here: ")
passwd = input("Enter Password Here: ")

print(end="\n")
if (password_check(passwd)):
    print("Registeration Successful")
else:
    print("Invalid Password !!! Please Read the Criteria of Password Carefully ")

#QUESTION_20
s = "Hello how are you all"
list = []
for i in s:
    if i == 'a' or i == 'i' or i == 'e' or i == 'o' or i == 'u' or i == 'A' or i == 'I' or i == 'E' or i == 'O' or i == 'U':
        list.append(i)
print(" Vowels : ", list)
