import math
#1. Inside the function
def func():
    print('I`m inside the function')
func()

#2. My name is...
def my_name_is(name):
    print(f"My name is {name}")

my_name_is('Sten')

#3. Sum six
def sum_six(num):
    print(num + 6)
sum_six(6)

#4. Sum numbers
def sum_numbers(a, b):
    return a +b
print(sum_numbers(5, 5))

#5. USD to EUR
def usd_to_eur(usd):
    return usd * 0.8
print(int(usd_to_eur(100)))

##############

def print_hello():
    print("Hello")

def get_hello():
    return "Hello"
print_hello()
greeting = get_hello()
print(greeting)

#Task
def ask_name_and_greet_user():
    name = input("Enter your name: ").lower().capitalize()
    if (name != "Thanos"):
        print(f"Hi, {name}. Would you like to have a hamburger")
    else:
        print("Get out of here, Thanos! Nobody wants to play with you!")

ask_name_and_greet_user()

def calculate_hypotenuse_length(a, b):
    print(math.sqrt(a**2 + b**2))
calculate_hypotenuse_length(3, 4)

def calculate_cathetus_length(c, b):
    print(math.sqrt(c**2 - b**2))
calculate_cathetus_length(5, 4)
