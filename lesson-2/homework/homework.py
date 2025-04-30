1. Age Calculator
from datetime import datetime

name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
current_year = datetime.now().year
age = current_year - birth_year

print(f"Hello {name}! You are {age} years old.")

2. Extract Car Names (from 'LMaasleitbtui')
txt = 'LMaasleitbtui'
maserati = txt[1::2]
lamborghini = txt[0] + txt[2::2]

print("Maserati:", maserati)
print("Lamborghini:", lamborghini)

3. Extract Car Names (from 'MsaatmiazD')
txt = 'MsaatmiazD'
mazda = txt[0] + txt[3] + txt[5] + txt[7] + txt[9]
saturn = txt[1] + txt[2] + txt[4] + txt[6] + txt[8]

print("Mazda:", mazda)
print("Saturn:", saturn)

4. Extract Residence Area
txt = "I'am John. I am from London"
words = txt.split()
residence = words[-1]

print("Residence area:", residence)

5. Reverse String
user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)

6. Count Vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string: ")
print("Number of vowels:", count_vowels(user_input))

7. Find Maximum Value
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]
max_value = max(numbers)
print("The maximum value is:", max_value)

8. Check Palindrome
def is_palindrome(word):
    return word == word[::-1]

user_input = input("Enter a word: ")
if is_palindrome(user_input.lower()):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
  
9. Extract Email Domain
email = input("Enter your email address: ")
domain = email.split('@')[-1]
print("Email domain:", domain)

10. Generate Random Password
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Generated password:", generate_password())
