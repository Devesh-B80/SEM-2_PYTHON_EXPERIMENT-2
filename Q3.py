"""Find the greatest among the two numbers. If numbers are equal than print “numbers are equal”."""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Numbers are equal")
