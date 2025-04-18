# Assisgment-3-
# This is a simple-level Python which basically functions of a calculator. It enables users to do four most common math operations:  addition, subtraction, multiplication and division.
# what the program does
This calculator: accepts two numbers as user input.
open asks the user which operation to do. - Does that operation.
displays the result.
It's completely text-based and runs in the terminal or command line.
# step by step explanation 
# 1. Function satup
The program defines four small chunks of code, known as functions, to perform each math operation:
one function for addition
one for subtraction
one for multiplication
one for division
Each function:
.Inputs two numbers.
. calculates the result - sends the result out.
# 2 . Getting user input
The program then:
. Prompts the user to enter the first number - Requests the second number.
. The inputs are cast into float so the calculator can manage both the whole 
    and decimals numbers.
# 3 . Showing the user options 
after it obtains the numbers, the program prints a little menu:
 . Addition
 . Subtraction
 . Division
 . Multiplication
Informs the user which number to put for each action.
# 4. Taking the user's choice
The user then is prompted to enter a number(1,2,3, or 4) to choose the operation they wish to apply.
# 5 performing the operation
The program checks to see what the user selected:
 . run the code matching function.
 . here it takes the two numbers as input.
 . displays the output of the calculation.
for example:
  . If the user selected 1, the calculator adds the numbers.
  . they dividing by 3 if they selected3.
# 6. Handling division errors
In the divisional section there is a minor protection:
  . It does not attempt to divide if the second number is zero.
  . Instead it prints something like: Error! Division by zero.
But there is a bug in the code in the cureent version. Unfortunately, the divison function multiplies.
# Fix needed
This is what the code does in the division function:
return a*b # this is wrong
It should be:
return a/b# Correct: this divides a by b
so if you're actually running the program, you want to fix that.
 
# How to Run the Program 
If you’d like to test the calculator: 
1. Save the code in a file calculator. py. 
2. Ensure that you have installed Python. 
3. But command line or terminal window must be open first. 
4. Run the program by typing: 
python calculator.py 
5. Instructions will appear in the terminal. 
# Example Run 
Here is how the calculator might work: 
Enter the first number: 10   
Enter the second number: 2   
1. Addition   
2. Subtraction   
3. Division   
4. Multiplication   
 Enter your choice (1/2/3/4): 3 
Result: 5.0 
#  Things to Know 
1. The program is text-based. No buttons or graphics. 
2. It uses float() for decimal numbers (like 3.5 or 12.75)
3. 3. It produces an error message if you try to divide by zero. 
4. Then, you can run it again to try various operations. 
#  Ideas to Improve 
1. If you want to grow this program, you could: 
2. Add more operations. 
3. Allow users to continuously perform calculations in a loop. And add in some packages.
4. Dump calculation history to a file. 
