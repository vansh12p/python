# Questinon 2 : WAP to input user's first name & print its length
"""name=input("Enter first name : ")
print(len("name"))"""

# Questinon 2 : WAP to find the occurrence of '$' in a string
"""str="Hi, $I am the $ symbol $99.99"
print(str.count("$"))"""

# Questinon 3 : remove 1 in list
"""list=[2,1,3]
list.remove(1)
print(list)"""

# question 3 : Reverse a string
"""str="hello"
rev=str[::-1]
print(rev)"""

# Question 4 : Count vowels in a string
"""str=input("Enter an string : ")
count=0
for chr in str:
    if chr in "aeiouAEIOU":
        count+=1
print(count)"""

# Question 5 : Check if string is palindrome
"""str=input("Enter an string : ")
rev=str[::-1]
if str==rev:
    print("palindrome")
else:
    print("not palindrome")"""
    
# Question 6 : Count words in a sentence
sentence = input("Enter an string : ")
word=sentence.split()
count=len(word)
print(count)
    