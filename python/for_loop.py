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
n=int(input("Enter the number : "))
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial of ",n, "is " , fact)    