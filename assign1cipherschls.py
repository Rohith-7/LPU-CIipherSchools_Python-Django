#Question 1 :-

s = "Hey i am from New Delhi"
print(len(s))
a = s.split()
print(a)


#Question 2 :-

s = "name is rahul"
print(s.capitalize())
print(s.title().replace("N","R"))
s.upper()


#Question 3 :-

l= float(input("Length : "))
b= float(input("breadth : "))
area = l*b
perimeter = 2*(l+b)
print("area = ",area)
print("perimeter = ",perimeter)


#Question 4 :-

d = float(input("Diameter:"))
pi = 3.14
perimeter = pi*d
area = (pi*d*d)/4
print("perimeter = ", perimeter)
print("area = ", area)


#Question 5 :-

import math
coffa=float(input("Enter the Coefficient a : "));
coffb=float(input("Enter the Coefficient b : "));
coffc=float(input("Enter the Coefficient c : "));
diss = math.sqrt((coffb**2)-4*coffa*coffc);
alpha=(-coffb + diss)/2*coffa;
beta=(-coffb - diss)/2*coffa;
print("The Roots of the Quadratic equation : ", "Alpha = ",alpha, "Beta = ",beta);


#Question 6 :-

r = float(input("Radius :"))
pi = 3.14
volume = (4*r*r*pi)/3
print("volume = ", volume)


#Question 7 :-

n =(input("number :"))
print("No. of digit is : ",len(n))


#Question 8 :-

s = (input("enter a string : "))
print(s.upper())


#Question 9 :-

s=input("Enter String : ")
n=int(input("Enter Index : "))
c=input("Enter Character : ")
temp=list(s)
temp[n]=c
s=" ".join(temp)
print(s)


#Question 10 :-

s ="My name is Rohith"
print(s[::-1])