name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Using f-strings
print("My name is {} and I am {} years old.".format(name, age))  # Using .format()


x = 10          # Integer
y = 3.14        # Float
z = "Python"    # String
is_active = True  # Boolean

print(type(x), type(y), type(z), type(is_active))  # Output types


a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False


# For loop
for i in range(5):
    print(i)  # Outputs: 0 1 2 3 4

# While loop
n = 3
while n > 0:
    print(n)
    n -= 1  # Outputs: 3 2 1


