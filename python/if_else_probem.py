#Question 1 : take a number from user and check if it is even or odd
"""a=int(input("a :"))
if(a==0):
    print("zero")
elif(a%2==0):
    print("even")
    
else:
    print("odd")"""
#Question 2 : positive , negative , zero
"""num=int(input("num :"))
if(num<0):
    print("negative") 
elif(num>0):
    print("positive")
else:
    print("zero")"""
#Question 3 :divisible by 5 and 11
"""num=int(input("enter a number :"))
if(num%5==0 and num%11==0):
    print("divisible")   
else:
    print("not divisible")"""
    
#Question 4 :leap year
"""year=int(input("Enter an year :"))
if((year%4==0 and year%100!=0) or year%400==0):
    print("leap year")
else:
    print("not an leap year")"""
    
#Question 5 : maximum of two
"""num1=int(input("enter first number :"))
num2=int(input("enter second number :"))
if(num1>num2):
    print("num 1st greater")
elif(num1<num2):
    print("num 2nd greater")
else:
    print("both are equal")"""

#Question 6 :maximum of three number
"""num1=int(input("enter 1st digit : "))
num2=int(input("enter 2nd digit : "))
num3=int(input("enter 3rd digit : "))
if(num1>num2 and num1>num3):
    print("1st is greter : ")
elif(num2>num1 and num2>num3):
    print("2nd digit greater")
elif(num3>num1 and num3>num2):
    print("3rd digit greter")
else:
    print("all are equal ")"""
    
#Question 7 :vowel or consonant
"""ch=input("enter a char. : ")
if(ch in 'aeiou'):
    print("vowel")
elif (ch.isalpha()):
    print("consonant")"""
    
#Question 8 : Alphabet , Digit or Special
"""ch=input("Enter a character : ")
if (ch.isalpha()):
    print("Alphabet")
elif (ch.isdigit()):
    print("Digit")
else:
    print("Special character")"""
 
#Question 9 :Uppercase or Lowercase
"""ch=input("Enter a char.")
if(ch.isupper()):
    print("uppercase")
elif(ch.islower()):
    print("lowercase")
else:
    print("not an letter")""" 
    
#Question 10 : Day of week
"""num=int(input("Enter an Number 1 to 7 : "))
if(num==1):
    print("Sunday")
elif(num==2):
    print("Monday")
elif(num==3):
    print("Tuesday")
elif(num==4):
    print("Wedenesday")
elif(num==5):
    print("Thursday")
elif(num==6):
    print("Friday")
elif(num==7):
    print("Saturday")
else:
    print("Invalid day")"""                
 
#Question 11 : Take marks(0-100) and display grade (A/B/C...) using if else ladder
"""marks=int(input("Take an marks 0-100 : "))
if(marks>=90):
    print("A")
elif(marks>=80):
    print("B")
elif(marks>=70):
    print("C")
elif(marks>=60):
    print("D")
elif(marks>=33):
    print("Pass")
else:
    print("Fail")"""
    
#Question 12 :Triangle valid or not
"""a=float(input("Enter 1st side of triangle : "))
b=float(input("Enter 2nd side of triangle : "))
c=float(input("Enter 3rd side of triangle : "))
if(a+b>c and b+c>a and c+a>b):
    print("Valid triangle")
else:
    print("Invalid triangle")"""
                