'''Practicing with different mathematical expressions and calculations.'''

#declare num_a and num_b

num_a = 3
num_b = 5

a = 3
b = 4
c = 5

# 1. Sum and difference

sum = num_a + num_b
print(f"{num_a} + {num_b} = {sum}")

difference = num_a - num_b
print(f"{num_a} - {num_b} = {difference}")

print('------------------------------------')

# 2. Float division

division = num_a / num_b;
print(f"{num_a} / {num_b} = {division}")

# 3. Integer division

division = num_a // num_b;
print(f"{num_a} // {num_b} = {division}")

# 4. Powerful operations
multiply_numbers = num_a * num_b
power = num_a ** num_b
remainder = num_a % num_b;

# 5. find average

average = (num_a + num_b) / 2

# 6. Area of a cirlce
import math

radius = 6
circle_area = math.pi * radius ** 2
print(round(circle_area, 2))

# 7. Area of an equilateral triangle
side_length = 3
triangle_area = a**2 * (math.sqrt(3) / 4)

# 8. Calculate discriminant

discriminant = b**2 - 4 * a * c

# 9. Calculate hypotenuse length
c = math.sqrt(a**2 + b**2)

# 10. calculate cathetus length

b = math.sqrt(c**2 - a**2)

# 11. Time converter
seconds = 98739430943
hours = seconds // 3600
minutes = seconds // 60

# 12. Student helper

angle = 67
sine = math.sin(angle)
cosine = math.cos(angle)

# 13. Greetings
n = 4
lots_of_heys = ""
i = 0

while i < n:
    i += 1
    lots_of_heys += 'Hey'
print(lots_of_heys)

# 14. Adding numbers

string_numbers = str(num_a) + str(num_b)
print(string_numbers)

