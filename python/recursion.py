# Question 1 : Write a recursive function to calculate the factorial of a number n.
"""def fact(n):
    if n==1 or n==0:
        return n
    return n*fact(n-1)
print(fact(6))"""


# Question 2 : Use recursion to find the sum of first n natural numbers.
"""def sum(n):
    if n==0:
        return 0
    return n + sum(n-1)
print(sum(5))"""


# Question 3 : Write a recursive function to print numbers from 1 to n.
"""def num(n):
    if n==0:
        return 0
    num(n-1)
    print(n, end=" ")
num(5)"""


# Question 4 : Recursive function to print numbers in reverse from n to 1.
"""def print_n_to_1(n):
    if n == 0:
        return 
    print(n, end=" ")
    print_n_to_1(n - 1)

print_n_to_1(5)"""


# Question 5 :Use recursion to check whether a string is a palindrome.
"""def is_palindrome(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("madam"))"""


# Question 6 : Find the nth number in the Fibonacci sequence recursively.
"""def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))"""


# Question 7 : Use recursion to calculate a^b. prowe(2, 3) → 8
"""def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
print(power(2,3))"""


# Question 8 : Count how many digits are in a given number n.
"""def count_digits(n):
    if n==0:
        return 0
    return 1 + count_digits(n//10)
print(count_digits(12345))"""


# Question 9 :  Use recursion to add all digits of n.
"""def sum_digits(n):
    if n==0:
        return 0
    return n%10 +sum_digits(n//10)
print(sum_digits(1234))"""
