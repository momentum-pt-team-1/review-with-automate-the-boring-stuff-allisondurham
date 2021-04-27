# # Please answer the practice questions at the end of chapters 1-6 here under the cooresponding comment:
################################################################################








# # Chapter 1

# 1. Which of the following are operators, and which are values?
*           operator
'hello'     value
-88.8       value
-           operator
/           operator
+           operator
5           value

# 2. Which of the following is a variable, and which is a string?
spam        variable
'spam'      string

# 3. Name three data types.
integer, floating-point, string

# 4. What is an expression made up of? What do all expressions do?
an expression consists of values and operators, they can be evaluated down to, or reduced to, a single value

# 5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?
expressions use operators ( + - * / ), while assignment statements use an = to name a variable and assign its value

# 6. What does the variable bacon contain after the following code runs?
# bacon = 20
# bacon + 1
    21

# 7. What should the following two expressions evaluate to?
# 'spam' + 'spamspam'
# 'spam' * 3
"spamspamspam"

# 8. Why is eggs a valid variable name while 100 is invalid?
100 is not a valid variable name because variable names cant begin with a number.
Meanwhile, the variable name "eggs" doesnt violate any variable naming rules.

# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
int()
float()
str()

# 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'
This causes an error because integers cant be concatenated with strings
correction :  "I have eaten " + str(99) + "burritos."

# Extra credit: Search online for the Python documentation for the len() function. It will be on a web page titled “Built-in Functions.” Skim the list of other functions Python has, look up what the round() function does, and experiment with it in the interactive shell.
#######################################################################################










# # Chapter 2

# 1. What are the two values of the Boolean data type? How do you write them?
True and False, written with capital first letters. 

# 2. What are the three Boolean operators?
and, or, not

# 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
True and True       True
True and False      False
False and True      False
False and False     False

True or True        True
True or False       True
False or True       True
False or False      False

not True            False
not False           True

# 4. What do the following expressions evaluate to?
(5 > 4) and (3 == 5)                      False
not (5 > 4)                               False
(5 > 4) or (3 == 5)                       True
not ((5 > 4) or (3 == 5))                 False
(True and True) and (True == False)       False
(not False) or (not True)                 True

# 5. What are the six comparison operators?
==      equal
!-      not equal
<       less than
>       greater than
<=      less than or equal
>=      greater than or equal

# 6. What is the difference between the equal to operator and the assignment operator?
== equal operator compares two things, and the return of that comparison is a Boolean value (True/False)
=  assignment operator basically says "is".  its used to set the value of a variable

# 7. Explain what a condition is and where you would use one.
condition statements decide whether or not to run the code. 
if it is raining, run the code that instructss robot butler to fetch the umbrella

# 8. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')                           b
    if spam > 5:                            l
        print('bacon')      block2          o
    else:                                   c
        print('ham')        block3          k
    print('spam')                           1    
print('spam')

# 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")

# 10. What keys can you press if your program is stuck in an infinite loop?
CTRL-C

# 11. What is the difference between break and continue?
break exits the loop, while continue jumps back to the start of the loop

# 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
range(10)      would be to iterate through the for loop 10 times
range(0,10)     would be to iterate through the for loop for numbers 0,1,2,3,4,5,6,7,8,9   stopping just before 10
range(0,10,1)    would iterate through the for loop for numbers 0-9, by an increment of 1

# 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
for i in range (1,11):
    print(i)

number = 0
while number < 10 :
    number = number + 1
    print(number)

# 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
import spam

spam.bacon()

# Extra credit: Look up the round() and abs() functions on the internet, and find out what they do. Experiment with them in the interactive shell.
###################################################################################################################









# Chapter 3


# 1. Why are functions advantageous to have in your programs?
to reduce repetition, and make your programs shorter and easier to read

# 2. When does the code in a function execute: when the function is defined or when the function is called?
when the function is called

# 3. What statement creates a function?
def

# 4. What is the difference between a function and a function call?
a function on its own just exists and does nothing until called
calling a function runs it

# 5. How many global scopes are there in a Python program? How many local scopes?
one global, and perhaps infinite local scopes

# 6. What happens to variables in a local scope when the function call returns?
it is destroyed

# 7. What is a return value? Can a return value be part of an expression?
the value that a function call evaluates.  yes, because expressions are composed of values and operators. and a return value is a value

# 8. If a function does not have a return statement, what is the return value of a call to that function?
it returns nothing, with value of None

# 9. How can you force a variable in a function to refer to the global variable?
by not using it locally in an assignment statement

# 10. What is the data type of None?
NoneType

# 11. What does the import areallyourpetsnamederic statement do?
it would import a module called areallyourpetsnamederic, if it existed

# 12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?
import spam

spam.bacon()

# 13. How can you prevent a program from crashing when it gets an error?
with try and except statements, by putting the code that may have an error in a try clause

# 14. What goes in the try clause? What goes in the except clause?
the code that may have an error goes in the try clause
what to do if that error happens goes in the except clause

################################################################################################




# Chapter 4

# Chapter 5

# Chapter 6
