#Question 1 : print numbers from 1 to 100.
"""i=1
while i<=100:
    print(i)
    i+=1"""
    
# Question 2 : print number from 100 to 1.
"""i=100
while i>=1:
    print(i)
    i-=1"""
    
# Question 3 : print the multiplication table of a number n.
"""n=int(input("Enter number : "))
i=1
while i<=10:
    print(n*i)
    i+=1"""
    
# Question 4 : print the element of the following list using a loop [1,4,9,16,25,36,49,64,81,100]
"""list=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(list):
    print(list[idx])
    idx+=1"""
    
# Question 5 : search for a number x in this tuple using loops:
"""x=int (input("Enter searching number : "))
tup=(1,4,9,16,25,36,49,64,81,100)
idx=0
while idx<len(tup):
    if (tup[idx]==x):
        print("number is found at index : " , idx)
        idx+=1"""
        
# Question 6 : WAP to find the sum of first n natural number .
"""n=int (input("Enter the number : "))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print("the sum of number ",n, " is ", sum)"""

# Question 7 : print all even numbers b/w 1 and 50 .
"""n= int(input("Enter the value of n : "))
i=2
while i<=n:
    print(i)
    i+=2"""
    
# Question 8 : Find the factorial of a number.
"""n=int(input("Enter the value : "))
fact=1
total=1
while fact<=n:
    total*=fact
    
    fact+=1
print(total) """   

# Question 9 : count digit in a number.
"""n=int(input("Enter the value : "))
count=0
while n>0:
    n//=10
    count+=1
print("Digit count is ", count)"""


# Question 10 : Reverse a number (eg. 123-321)
"""n=int(input("Enter the value : "))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("Reversed number is ",rev)"""

# Question 11 : check if a number is palindrome .
"""n=int(input("Enter the value : "))
temp=n
rev=0
while n>0:
    digit= n%10
    rev=rev*10+digit
    n=n//10
if(rev==temp):
    print("It is palindrome")
else:
    print("It is not palindrome")"""

# Question 12 : Print Fibonacci series up to n terms.
"""n=int(input("Enter the value : "))
a,b=0,1
count=0
while count<n:
    print(a,end = ' , ')
    a,b=b,a+b
    count+=1"""

# Question 13 : Find whether a number is an Armstrong number.
"""n=int(input("Enter the value : "))
temp=n
sum=0
order=len(str(n))
while n>0:
    digit=n%10
    sum+=digit**order
    n//=10
if sum==temp:
    print("that number is armstrong")
else:
    print("that is not armstrong")"""

# Question 14 : Take user input repeatedly until they enter 0.
"""while True:
    n=int(input("Enter the value : "))
    if n==0:
       print("the code is end : ")
       break
    else:
        print("the enter number is ", n)"""
        
# Question 15 : Check if a number is prime
"""n=int(input("Enter the value : "))
i=2
is_prime= True
while i<n:
    if n%i==0:
        is_prime=False
        break
    i+=1
if is_prime and n>1:
    print("prime")
else:
    print("not prime")"""    
    
# Question 16 : Print numbers n to 1:
"""n=int(input("Enter the value : "))
while n>=1:
    print(n)
    n-=1"""
    

# Question 17 : Square from 1 to n:
"""n=int(input("Enter the value : "))
while n>=1:
    print(n**2)
    n-=1"""