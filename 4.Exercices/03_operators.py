import sympy as sp

# 1. Declare your age as integer variable
age = 18

# 2. Declare your height as a float variable
height = 2

# 3. Declare a variable that store a complex number
complex_num = 1 + 1j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)
base_triangle = int(input("Enter base triangle: "))
height_triangle = int(input("Enter height triangle: "))
area_of_triangle = 0.5 * base_triangle * height_triangle

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)
a_of_triangle = int(input("Enter a number: "))
b_of_triangle = int(input("Enter b number: "))
c_of_triangle = int(input("Enter c number: "))
perimeter_of_triangle = a_of_triangle + b_of_triangle + c_of_triangle

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length_of_rectangle = int(input("Enter length of rectangle: "))
width_of_rectangle = int(input("Enter width of rectangle: "))
area_of_rectangle = length_of_rectangle * width_of_rectangle
perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14
radius_of_circle = int(input("Enter radius of circle: "))
area_of_circle = radius_of_circle ** 2 * 3.14
circumference_of_circle = 2 * 3.14 * radius_of_circle

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x - 2
print("Slope = 2")
print("x-intercept = 1")
print("y-intercept = -2")

# 9. Slope is (m = y2 - y1 / x2 - x1). Find the slope and Euclidean distance between point (2, 2) and point (6, 10)
x1, y1, x2, y2 = 2, 2, 6, 10
print("Slope =", int((y2 - y1) / (x2 - x1)))
print(f"Euclidean= {((x2-x1)**2 + (y2-y1)**2) ** 0.5:.2f}" )

# 10. Compare the slopes in tasks 8 and 9
print(2 == int((y2 - y1) / (x2 - x1)))

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0
for x in range(-10, 10):
    y = x**2 + 6*x + 9
    if y == 0:
        print(x)
    break

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement
print(len('python') > len('dragon'))

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python' and 'on' in 'dragon':
    print('on in python and dragon')

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence
if 'jargon' in 'I hope this course is not full of jargon':
    print('jargon exist')
# 15. There is no 'on' in both dragon and python
if "on" not in "python" and "on" not in "dragon":
    print('on not in python and dragon')

# 16. Find the length of the text python and convert the value to float and convert it to string
text_py = 'python'
len_int = int(len(text_py))
len_float = float(len(text_py))
print(len_int, len_float)
# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?


# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print(7 // 3 == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print(type('10') == type(10))
# 20. Check if int('9.8') is equal to 10
print(int(9.8) == int(10))

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person
hour = input("Enter hour: ")
per_hour = int(input("Enter per hour: "))
print('pay=', hour * per_hour)

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = float(input("Enter number of years: "))
seconds = years * 365 * 24 * 60 * 60
print("Seconds lived:", seconds)

# 23. Write a Python script that displays the following table
#
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
