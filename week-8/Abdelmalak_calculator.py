# /*
# ;============================================
# ; Title: Exercise 8.3
# ; Author: Professor Krasso
# ; Date: 16 July 2021
# ; Modified By: Soliman Abdelmalak
# ; Description: Python in Action
# ;===========================================
# */

first_name = 'Soliman'
last_name = 'Abdelmalak'
first_Python = 'Calculator app'
print(first_name + ' ' + last_name + ' ' + first_Python)

# Create an “add” function with two parameters 
# the function return the total of the parameterized values
def add(addA, addB):
    return addA + addB

# Create a “subtract” function with two parameters 
# the function return the subtracted total of the parameterized values
def subtract(subA, subB):
    return subA - subB

# Create a “divide” function with two parameters 
#  the function return the divided total of the parameterized values
def divide(divA, divB):
        return divA / divB

# Call each function with a separate print statement output
print(add(1, 2))
print(subtract(4, 1))
print(divide(8, 2))