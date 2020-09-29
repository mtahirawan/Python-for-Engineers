"""
===================================================
Basics of Python Programming
Example Python Script

Dr. Muhammad Tahir
EE Department, CUST, Islamabad
===================================================
"""

#===================================================
# Python : print()
print("Helo World !!!")

name = input("Enter your name :")
print("Hello ", name)
print("Hellow "+ name)

first = 'Muhammad'
last = 'Tahir'
Name = first +' '+ last  # Concatenation String
print(Name)

#---------------------------------------------------
# Variant of print()

x = 3.25
y = 100

print("Value of x = " + str(x))
print("Value of x = " , x)
print(f'Value of x = {x}')
print('X = ', x, "Y = ", y)
print(f' X = {x}, Y = {y}')

#===================================================
# Program to compute area of a circle

PI = 3.14 # Pi value

radius =  float(input("Enter value of radious = "))   

area = PI * radius* radius # area
area1 = PI * (radius ** 3) # area
circum = 2 * PI * radius # circumference

print("Circumference =", circum)
print("Area =  ", area1)

#=====================================================
# Python : Nested if-else 

a = 55
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
#======================================================
# Python : Nested if-else

# Temprature of a Patient
tmp = input("Enter Temprature = ")
tmp = float(tmp)

if(tmp > 103):
    print("High Fever")
elif(tmp > 98.6 and tmp < 103):
    print("Low Fever")
else:
    print("No Fever")      

#======================================================
# Python : While Loop

LC = 0
while LC < 3:
    marks = float(input("Enter marks of student = "))
    
    if marks >= 50:
        print("Studnet has passed the course.")
    else:
        print("Student did not pass the course.")
    LC += 1
    
#============================================
# Python : While Loop
 
# Factorial of a number
Num = int(input("Enter a Number = "))
Number = Num
Fact = 1
while Num > 0:
    Fact = Fact*Num
    Num -= 1
    
print('Factorial of '+ str(Number) + ' is ' + str(Fact) )      
    
#=============================================
# Python : For Loop 

# Variants of For Loop
for i in range(10):
    print(i)

accum = 0
for i in range(10, 20):
    accum += i
print(accum)


accum = 0
for i in range(1, 20, 2):
    accum += i
    if accum == 10:
        break        
print(accum)

#==============================================
# Python : For Loop

X = int (input('Enter value of X = '))
Y = int (input('Enter value of Y = '))

for i in range (X,Y):
    if(i%2 == 0):
        print(i,' is Even')
    else:
        print(i , ' is Odd')        

#==============================================
# Python : String Patterns

x = int(input("Enter a number = "))
star = '#'
for i in range(5):
    print(star*x)

#x = int(input("Enter a number = "))
star = '#'
#for i in range(10):
for j in range(x):
   print(star*j)

#x = int(input("Enter a number = "))
star = '#'
#for i in range(10):
for j in range(x,0,-1):
   print(star*j)
   
#==============================================   

