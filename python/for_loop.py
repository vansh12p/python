# Practice question 
#1
"""list=[1,2,3,4]
for num in list :
    print(num)"""
    
# Question 1 : print the elements of the following list using a loop:
"""list=[1,4,9,16,25,36,49,64,81,100]
for num in list :
    print(num)"""
# Question 2 : search for a numer x in this tuple using loop:
"""nums=(1,4,9,16,25,36,49,64,81,100,1)
x=int(input("Enter an searching num : "))
idx=0
for val in nums :
    if (val==x):
        print("num is found idx " , idx)
    idx+=1"""
        
# Question 3 : print from 1 to 100
"""for i in range (1,101):
    print(i)"""
    
# Question 4 : print numbers from 100 to 1
"""for i in range (100,0,-1):
    print(i) """
    
# Question 5 : print the multiplication table of a number n
"""n=int(input("Enter an number : "))
for i in range (1,11):
    print(i*n)"""
    
# Question 6 : WAP to find the sum of first n natural number.
"""n=int(input("Enter the number : "))
sum=0
for i in range(1,n+1,1):
    sum+=i
print("the sum of number ",n, " is ", sum)"""
    
# Question 7 : WAP to find the factorial of first n numbers .
"""n=int(input("Enter the number : "))
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial of ",n, "is " , fact)""" 


# Question 8 : Numbers 1 to 10:
"""for i in range(1,10):
    print(i)"""  
    

# Question 9 : Odd numbers 1 to 100:
"""for i in range (1,101,2):
        print(i)"""
        

# Question 10 : Sum 1 to n:
"""n=int(input("Enter the number : "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)"""


# Question 11 : Multiplication table:
"""n=int(input("Enter the number : "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")"""
    
    
# Question 12 : Print list items:
"""list = [1, 2, 3, 4, 5]
for i in list:
    print(i)"""
    
    
# Question 13 : Characters of string:
"""n=input("Enter an string : ")
for ch in n:
    print(ch)"""
 

# Question 14 : Factorial:
"""n=int(input("Enter an number : "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)"""


# Question 15 : Create a pattern:

"""*
   **
   ***"""
"""sum="*"
for i in range(1,4):
   
    print(sum*i)
    i+=1"""
    
    
# Question 16 : Print all elements of a list in reverse using a for loop.
"""list = [1, 2, 3, 4, 5]
for i in reversed(list):
    print(i)"""
    
    
# Question 17 : Count how many times a character appears in a string.
"""s=input("Enter an string : ")
ch=input("Enter an charcter : ")
count=0
for i in s:
    if i==ch:
        count+=1
print(count)"""


# Question 18 : Find all vowels in a string using a for loop.
"""str=input("Enter an string : ")
vowels="aeiouAEIOU"
for ch in str:
    if ch in vowels:
        print(ch)"""
    

# Question 19 : Check if a list contains a given item.
"""lst = [10, 20, 30]
x=int(input("Enter the number : "))
found=False
for item in lst:
    if item==x:
        found=True
        break
print("found" if found else "not found")"""


# Question 20 : Print 100 to 1:
"""for i in range(100,0,-1):
    print(i)"""
    
    
# Question 21 : Square of list items:
"""lst = [1, 2, 3, 4]
for item in lst:
    print(item**2)"""
    
    
# Question 22 : Loop through a dictionary and print keys and values.
"""d={"a":1,"b":2}
for key in d:
    print(f"{key}:{d[key]}")"""

