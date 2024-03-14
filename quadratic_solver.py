# Linear Algebra: Quadratic Equation Solver

# Calculates the roots using the quadratic formula
import math
import cmath

# Display the quadratic formula template to guide the user
print("Welcome to the Quadratic Equation Solver!")
print("\nFind the two roots of a quadratic polynominal using the Quadratic Formula:")
print("ax^2 + bx + c = 0")

# Function to get the coefficient input
def get_coefficient(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nSorry brosif. You need to enter a numeric value :))")

# Take user input for coefficients a, b, and c with error handling
a = get_coefficient("\nEnter your a coefficient a: ")
# Ensure a is not zero for a quadratic equation
while a == 0:
    print("Nah kompis, it can't be quadratic function if 'a' is 0. You can try again thou..")
    a = get_coefficient("\nEnter coefficient 'a' : ")

b = get_coefficient("Enter coefficient 'b': ")
c = get_coefficient("Enter coefficient 'c': ")

# Calculate the discriminant
discriminant = b**2 - 4*a*c
print("\nThe discriminant is: ", discriminant)

# Calculate the two roots using the quadratic formula
if discriminant >= 0:
    # Real roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("\nThe roots are: x1= {} and x2= {}".format(round(root1, 3), round(root2, 3)))
else:
    # Complex roots
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    print("\nThe roots are complex and include an imaginary part: x1= {:.3f} + {:.3f}i and x2= {:.3f} - {:.3f}i".format(
        root1.real, root1.imag, root2.real, root2.imag))