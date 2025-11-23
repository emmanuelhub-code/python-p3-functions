# lib/functions.py

# 1. greet_programmer: no arguments, prints a fixed string
def greet_programmer():
    print("Hello, programmer!")


# 2. greet: takes one argument 'name', prints a personalized greeting
def greet(name):
    print(f"Hello, {name}!")


# 3. greet_with_default: same as greet, but has a default argument
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


# 4. add: takes two numbers and returns their sum
def add(num1, num2):
    return num1 + num2


# 5. halve: takes one number and returns it divided by two
def halve(number):
    return number / 2
