# Question 1 : WAF to print the length of a list. (list is the parameter)
"""cities=["delhi","mumbai","chennai","noida","gurgaon"]
heroes=["thor","shaktimaan","ironman","caption america"]
def print_len(list):
    print(len(list))
print_len(cities)
print_len(heroes)"""

# Question 2 : WAF to print the element of a list in a single line. (list is the parameter)
"""list=[1,2,3,4,5,6]
def print_ele(list):
    for item in list:
        print(item,end=" ")
print_ele(list)"""
    
# Question 3 : WAF to find the factorial of n.(n is the parameter)
"""def fact(n):
    factorial=1
    for i in range(1,n+1):            
        factorial*=i 
    print(factorial) 
fact(8)"""       
    
# Question 4 : WAF to convert USD to INR
"""def usd_to_inr(usd):
    inr=78*usd
    print(inr)
usd_to_inr(3)"""


# Question 5 : Print Hello Function
"""def print_hello():
    print("hello")
print_hello()"""


# Question 6 : Write a function add(a, b) that returns the sum of a and b.
"""def sum(a,b):
    return a+b
print(sum(2,3))"""


# Question 7 : Write a function find_max(a, b) that returns the larger of two numbers.
"""a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
def max(a,b):
    if(a>b):
        print("a is greater then b")
    else:
        print("b is greater than a")

max(a,b)   """     


# Question 8 : Write a function is_even(n) that returns True if the number is even, otherwise False.
"""def is_even(n):
    if(n%2==0):
        return True
    else:
        return False
n=int(input("Enter the value of n : "))
print(is_even(n)) """       


# Question 9 : Write a function square(n) that returns the square of a number.
"""def square(n):
    print(n**2)
n=int(input("Enter the value of n : "))
square(n)"""


# Question 10 : Write a function fibonacci(n) that prints the first n numbers of the Fibonacci series.
"""def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a , end=" ")
        a,b=b,a+b
n=int(input("Enter the value of n : "))
fibonacci(n)"""


# Question 11 : Write a function is_palindrome(s) that returns True if the string s is a palindrome.
"""def is_palindrome(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]
print(is_palindrome("madam"))"""


# Question 12 : Write a function list_sum(lst) that returns the sum of all elements in a list.
"""def list_sum(lst):
    return sum(lst) # Uses built-in sum() to return the total
print(list_sum([1,2,3,4,5,6]))"""


# Question 13 : Write a function count_vowels(s) that returns the number of vowels in a string.
"""def count_vowels(s):
    vowels='aeiouAEIOU'
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count
s=input('enter an string : ')
print(count_vowels(s))   """    
        
        
    
# Question 14 : Write a function is_prime(n) that returns True if n is a prime number.
"""def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%2==0:
            return False
    return True
n=int(input("Enter the value of n : "))
print(is_prime(n))"""
        


# Question 15 : Write a function is_armstrong(n) that returns True if n is an Armstrong number.
"""def is_armstrong(n):
    order=len(str(n))
    total=sum(int(digit)**order for digit in str(n))
    return total==n
print(is_armstrong(153))"""
