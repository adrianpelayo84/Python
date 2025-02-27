# 1. Declare your age as integer variable
age = 40

# 2. Declare your height as a float variable
height = 5.94

# 3. Declare a complex number variable
complex_number = 1 + 1j

# 4. Write a script that prompts the user to enter base and height of a triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input('Enter the base of the triangle: '))
height = float(input('Enter the height of the triangle: '))
area = 0.5 * base * height
print('The area of the triangle is:', area)

# 5. Write a script that prompts the user to enter side a, side b, and side c of a triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input('Enter the side a of the triangle: '))
side_b = float(input('Enter the side b of the triangle: '))
side_c = float(input('Enter the side c of the triangle: '))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is:', perimeter)

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))
area = length * width
perimeter = 2 * (length + width)
print('The area of the rectangle is:', area)
print('The perimeter of the rectangle is:', perimeter)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input('Enter the radius of the circle: '))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print('The area of the circle is:', area)
print('The circumference of the circle is:', circumference)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# slope = 2
# x-intercept = 1
# y-intercept = -2

# 9. Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
print('The slope between point (2, 2) and point (6, 10) is:', slope)

# 10. Compare the slopes in tasks 8 and 9.
# The slope in task 8 is 2 and the slope in task 9 is 2.0. They are the same.

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
x1 = -4
x2 = -3
x3 = -2
x4 = -1
x5 = 0
x6 = 1
y1 = x1**2 + 6*x1 + 9
y2 = x2**2 + 6*x2 + 9
y3 = x3**2 + 6*x3 + 9
y4 = x4**2 + 6*x4 + 9
y5 = x5**2 + 6*x5 + 9
y6 = x6**2 + 6*x6 + 9
print(f"x = {x1}, y = {y1}")
print(f"x = {x2}, y = {y2}")
print(f"x = {x3}, y = {y3}")
print(f"x = {x4}, y = {y4}")
print(f"x = {x5}, y = {y5}")
print(f"x = {x6}, y = {y6}")

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
length_python = len('python')
length_jargon = len('dragon')
print(length_python > length_jargon)

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 14. I hope this course is not full of jargon. Use in operator to check if 'jargon' is in the sentence.
sentence = 'I hope this course is not full of jargon'
print('jargon' in sentence)

# 15. There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

# 16. Find the length of the text python and convert the value to float and convert it to string
length_python = len('python')
length_python = float(length_python)
print(type(length_python))
length_python = str(length_python)
print(type(length_python))

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 4
print(number % 2 == 0)

# 18. The floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))

# 19. Check if type of '10' is equal to 10
print(type('10') == type(10))

# 20. Check if int('9.8') is equal to 10
num = int(float('9.8'))
print(num == 10)

# 21. Wrie a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input('Enter hours: '))
rate = float(input('Enter rate per hour: '))
pay = hours * rate
print('Your pay is:', pay)
print('weekly pay:', pay * 7)

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input('Enter number of years: '))
seconds_per_year = 60 * 60 * 24 * 365
seconds_per_hundred_years = seconds_per_year * 100
seconds_lived = years * seconds_per_year
print('You have lived for:', seconds_lived, 'seconds')
print('You can live for:', seconds_per_hundred_years - seconds_lived, 'seconds')

# 23. Write a Python code that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')
