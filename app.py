"""
PYTHON BASIC REVISION GUIDING ASSIGNMENT ONE
1.	Write a python program that  asks a user for his/her name, age, and phone number and store it in three different variables.
2.	Given two lists, l1 and l2, write a python program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
3.	Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list. Given list1 = [54, 44, 27, 79, 91, 41]
4.	Write a Python program to test if a given page is found or not on the server.
5.	Write a function that returns the maximum of two numbers.
6.	Write a function called fizz_buzz that takes a number.
a.	If the number is divisible by 3, it should return “Fizz”.
b.	If it is divisible by 5, it should return “Buzz”.
c.	If it is divisible by both 3 and 5, it should return “FizzBuzz”.
d.	Otherwise, it should return the same number.
7.	Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
a.	0 EVEN
b.	1 ODD
c.	2 EVEN
d.	3 ODD

"""

# 1. Write a python program that  asks a user for his/her name, age, and phone number and store it in three different variables.
name = input("Enter your name: ")
age = input("Enter your age: ")
phone_number = input("Enter your phone number: ")
print("Your name is: ", name)
print("Your age is: ", age)
print("Your phone number is: ", phone_number)

# 2. Given two lists, l1 and l2, write a python program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []
for i in range(len(l1)):
    if i % 2 != 0:
        l3.append(l1[i])
for i in range(len(l2)):
    if i % 2 == 0:
        l3.append(l2[i])
print(l3)

# 3. Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list. Given list1 = [54, 44, 27, 79, 91, 41]
list1 = [54, 44, 27, 79, 91, 41]
list1.pop(4)
list1.insert(2, 91)
list1.append(91)
print(list1)

# 4. Write a Python program to test if a given page is found or not on the server.
import requests
url = "https://www.google.com"
response = requests.get(url)
if response.status_code == 200:
    print("Page found")
else:
    print("Page not found")

# 5. Write a function that returns the maximum of two numbers.
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
print(max_of_two(5, 10))

# 6. Write a function called fizz_buzz that takes a number.
# a. If the number is divisible by 3, it should return “Fizz”.
# b. If it is divisible by 5, it should return “Buzz”.
# c. If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# d. Otherwise, it should return the same number.
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
print(fizz_buzz(15))

# 7. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
# a. 0 EVEN
# b. 1 ODD
# c. 2 EVEN
# d. 3 ODD
def showNumbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")
showNumbers(3)



