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
x=int (input("Enter searching number : "))
tup=(1,4,9,16,25,36,49,64,81,100)
idx=0
while idx<len(tup):
    if (tup[idx]==x):
        print("number is found at index : " , idx)
        idx+=1

    
    