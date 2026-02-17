""". Check whether the quadratic equation has real roots or imaginary roots. Display the roots.
"""
import math  # needed for square root

# take coefficients of quadratic equation
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# calculate discriminant
D = b**2 - 4*a*c

# check nature of roots
if D > 0:
    # two real and distinct roots
    r1 = (-b + math.sqrt(D)) / (2*a)
    r2 = (-b - math.sqrt(D)) / (2*a)
    print("Roots are real and distinct")
    print("Root1 =", r1)
    print("Root2 =", r2)

elif D == 0:
    # real and equal roots
    r = -b / (2*a)
    print("Roots are real and equal")
    print("Root =", r)

else:
    # imaginary (complex) roots
    real = -b / (2*a)
    imag = math.sqrt(-D) / (2*a)
    print("Roots are imaginary")
    print("Root1 =", real, "+", imag, "i")
    print("Root2 =", real, "-", imag, "i")
