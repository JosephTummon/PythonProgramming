# Program to illustrate scoping in Python
def f(x):
    """Function that adds 1 to its argument and prints it out"""
    print("In function f:")
    x += 1
    y = 1
    a = 7
    c = 4
    print("a is", a)
    # No value for b will pull from outside function
    print("b is", b)
    print("c is", c)
    print("x is", x)
    print("y is", y)
    print("z is", z)
    return x

a, b, c, x, y, z = -2, 0, 99, 5, 10, 15

print("Before function f:")
print("a is", a)
print("b is", b)
print("c is", c)
print("x is", x)
print("y is", y)
print("z is", z)

z = f(x)

#will only change z as we let z =f(x)
# a, b, c should go back to where they were
print("After function f:")
print("a is", a)
print("b is", b)
print("c is", c)
print("x is", x)
print("y is", y)
print("z is", z)
