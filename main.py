"""
1.	Write a program to print all the numbers from 1 to 100 except multiples of 3.
2.	Write a program to print all alphabets from a to z.
3.	Write a program to create function func1() to accept a variable length of arguments and print their value.
4.	Write a program to display only those numbers from a list that satisfy the following conditions
•	The number must be divisible by five
•	If the number is greater than 150, then skip it and move to the next number
•	If the number is greater than 500, then stop the loop given numbers = [12, 75, 150, 180, 145, 525, 50]
5.	Display numbers from -10 to -1 using while loop
Choose one of the Questions below from 6-7
6.	Create a program that asks the user a series of questions. Each question should have a multiple choice answer. The user should be able to type in the letter of the answer they think is correct. After all the questions have been asked, the program should tell the user how many they got correct and what the correct answers were.
7.	Create a program that generates a random password for the user. Ask the user how long they want their password to be, and how many letters and numbers they want in their password. Have a mix of upper and lowercase letters, as well as numbers and symbols. The password should be a minimum of 6 characters long.
"""

# 1. Write a program to print all the numbers from 1 to 100 except multiples of 3.
for i in range(1, 101):
    if i % 3 != 0:
        print(i)

# 2. Write a program to print all alphabets from a to z.
for i in range(97, 123):
    print(chr(i))

# 3. Write a program to create function func1() to accept a variable length of arguments and print their value.
def func1(*args):
    for i in args:
        print(i)
func1(1, 2, 3, 4, 5)

# 4. Write a program to display only those numbers from a list that satisfy the following conditions
# •	The number must be divisible by five
# •	If the number is greater than 150, then skip it and move to the next number
# •	If the number is greater than 500, then stop the loop given numbers = [12, 75, 150, 180, 145, 525, 50]
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)

# 5. Display numbers from -10 to -1 using while loop
i = -10
while i < 0:
    print(i)
    i += 1

# 6. Create a program that asks the user a series of questions. Each question should have a multiple choice answer. The user should be able to type in the letter of the answer they think is correct. After all the questions have been asked, the program should tell the user how many they got correct and what the correct answers were.
questions = [
    "What is the capital of India?\n(a) Delhi\n(b) Mumbai\n(c) Chennai\n(d) Kolkata\n",
    "What is the capital of Australia?\n(a) Sydney\n(b) Melbourne\n(c) Canberra\n(d) Perth\n",
    "What is the capital of Japan?\n(a) Tokyo\n(b) Osaka\n(c) Kyoto\n(d) Nagoya\n",
    "What is the capital of China?\n(a) Beijing\n(b) Shanghai\n(c) Guangzhou\n(d) Shenzhen\n",
    "What is the capital of Russia?\n(a) Moscow\n(b) St. Petersburg\n(c) Novosibirsk\n(d) Yekaterinburg\n",
    "What is the capital of Brazil?\n(a) Rio de Janeiro\n(b) Sao Paulo\n(c) Brasilia\n(d) Salvador\n",
    "What is the capital of Canada?\n(a) Toronto\n(b) Montreal\n(c) Ottawa\n(d) Vancouver\n",
    "What is the capital of France?\n(a) Paris\n(b) Marseille\n(c) Lyon\n(d) Toulouse\n",
    "What is the capital of Germany?\n(a) Berlin\n(b) Hamburg\n(c) Munich\n(d) Cologne\n",
]
answers = ["a", "c", "a", "a", "a", "c", "c", "a", "a"]
correct = 0
for i in range(len(questions)):
    answer = input(questions[i]).lower()
    if answer == answers[i]:
        correct += 1
print(f"You got {correct} out of {len(questions)} correct.")

# 7. Create a program that generates a random password for the user. Ask the user how long they want their password to be, and how many letters and numbers they want in their password. Have a mix of upper and lowercase letters, as well as numbers and symbols. The password should be a minimum of 6 characters long.
import random
import string
length = int(input("How long do you want your password to be? "))
letters = int(input("How many letters do you want in your password? "))
numbers = int(input("How many numbers do you want in your password? "))
symbols = int(input("How many symbols do you want in your password? "))
password = ""
for i in range(letters):
    password += random.choice(string.ascii_letters)
for i in range(numbers):
    password += random.choice(string.digits)
for i in range(symbols):
    password += random.choice(string.punctuation)
password = list(password)
random.shuffle(password)
password = "".join(password)
print(password)

