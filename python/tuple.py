# Question 1 : WAP to ask user to enter names of their 3 favorite movies & store them in a list
"""movies=[]
mov1=input('Enter 1st movie : ')
mov2=input('Enter 2nd movie : ')
mov3=input('Enter 3rd movie : ')
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)"""

# Question 2 : WAP to check if a list contains a palindrome of elements .(Hint:use copy() method)
#  [1,2,3,2,1]        [1,"abc","abc",1]
"""val1=[1,2,3,2,1]
copy_val1 = val1.copy()
val1.reverse()
if (copy_val1==val1):
    print("it is palindrome")
else:
    print("it is not an palindrome")"""

# Question 3 : WAP to count the number of students with the "A" grade in the following tuple.
# ["C","D","A","A","B","B","A"]
tup = ("C","D","A","A","B","B","A")
print(tup.count("A"))
print(tup.index("C"))
      
# Question 3 : store the above values in a list & sort them "A" to "D".
"""list1 = ["C","D","A","A","B","B","A"]
list1.sort()
print(list1)"""
      