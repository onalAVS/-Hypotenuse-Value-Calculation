import math

def calculate_circle(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return perimeter, area

# Example usage
radius = float(input("Enter the radius of the circle: "))
circle_perimeter, circle_area = calculate_circle(radius)

print("Perimeter of the circle:", circle_perimeter)
print("Area of the circle:", circle_area)

def calculate_square(side_length):
    perimeter = 4 * side_length
    area = side_length ** 2
    return perimeter, area

# Example usage for Square
side_length = float(input("Enter the side length of the square: "))
square_perimeter, square_area = calculate_square(side_length)

print("Perimeter of the square:", square_perimeter)
print("Area of the square:", square_area)


