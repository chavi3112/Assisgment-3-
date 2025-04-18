# Assisgment-3-
# This is a simple-level Python which basically functions of a calculator. It enables users to do four most common math operations:  addition, subtraction, multiplication and division.
# what the program does
This calculator: accepts two numbers as user input.
open asks the user which operation to do. - Does that operation.
displays the result.
It's completely text-based and runs in the terminal or command line.
# step by step explanation 
1. Function satup
The program defines four small chunks of code, known as functions, to perform each math operation:
one function for addition
one for subtraction
one for multiplication
one for division
# Each function:
 1.Inputs two numbers.
 2. calculates the result - sends the result out.
2. Getting user input
The program then:
 1. Prompts the user to enter the first number - Requests the second number.
 2. The inputs are cast into float so the calculator can manage both the whole and decimals numbers.
3. Showing the user options 
after it obtains the numbers, the program prints a little menu:
 1. Addition
 2. Subtraction
 3. Division
 4. Multiplication
Informs the user which number to put for each action.
4. Taking the user's choice
The user then is prompted to enter a number(1,2,3, or 4) to choose the operation they wish to apply.
5 performing the operation
The program checks to see what the user selected:
  1. run the code matching function.
  2. here it takes the two numbers as input.
  3. displays the output of the calculation.
for example:
  1. If the user selected 1, the calculator adds the numbers.
  2. they dividing by 3 if they selected3.
6. Handling division errors
In the divisional section there is a minor protection:
   1. It does not attempt to divide if the second number is zero.
   2. Instead it prints something like: Error! Division by zero.
But there is a bug in the code in the cureent version. Unfortunately, the divison function multiplies.
# Fix needed
This is what the code does in the division function:
return a*b # this is wrong
It should be:
return a/b# Correct: this divides a by b
so if you're actually running the program, you want to fix that.
