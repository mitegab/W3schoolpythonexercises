"""
this one is all about phyton variables how to use them and how to declare them
"""
#exercise 1
#Create a variable named carname and assign the value Volvo to it.
carname = "Volvo"
print(carname)
#exercise 2
#Create a variable named x and assign the value 50 to it.
x = 50
print(x)
#exercise 3
#Display the sum of 5 + 10, using two variables: x and y.
x = 5
y=10
print(x+y)
#exercise 4
#Create a variable called z, assign x + y to it, and display the result.
z = x + y
print(z)
#exercise 5
#Insert the correct syntax to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#exercise 6
#Insert the correct syntax to assign the same value to all three variables in one code line.
x = y = z = "Orange"
print(x)
print(y)
print(z)
#exercise 7
#Insert the correct keyword to make the variable xx belong to the global scope.
xx = "awesome"
def myfunc():
  global xx
  xx = "fantastic"
myfunc()
print(xx)
