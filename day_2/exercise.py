# ITP Week 1 Day 4 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.
import math
# Easy:
#     - A function that subtracts one integer from another
#     - A function that multiplies three integers
#     - A function that adds four integers

def subtract(number1, number2):
  return number1 - number2

def multiply(number1, number2, number3):
  return number1 * number2 * number3

def add(number1, number2, number3, number4):
  return number1 + number2 + number3 + number4

function = input("please choose function by selecting a number \n"
"1. Subtract 2 numbers \n"
"2. multiply 3 numbers \n"
"3. add 4 numbers \n"
"Function Choice: ")


if function == '1':
  number1 = input("Please choose number 1: ")
  number2 = input("Please choose number 2: ")
  def subtract(number1, number2):
    return number1 - number2
  print(subtract(number1, number2))
elif function == 2:
  number1 = input("Please choose number 1: ")
  number2 = input("Please choose number 2: ")
  number3 = input("Please choose number 3: ")
  def multiply(number1, number2, number3):
    return number1 * number2 * number3
  print(multiply(number1, number2, number3))
elif function == 3:
  number1 = input("Please choose number 1: ")
  number2 = input("Please choose number 2: ")
  number3 = input("Please choose number 3: ")
  number4 = input("Please choose number 4: ")
  def add(number1, number2, number3, number4):
    return number1 + number2 + number3 + number4
  print(add(number1 + number2 + number3 + number4))



# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.

# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global variable, or through a specific amount input by the user.  You may use the math module from the Python standard library.

#Remember to first write in comments an outline of what you want to code (using regular words, no computer-speak) BEFORE you begin to code.  Break each part down to the smallest problem you can, and then address them individually.  CONSULT THE RESOURCES if you get stuck, and don't be afraid to Google.