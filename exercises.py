# # Please answer the practice questions at the end of chapters 1-6 here under the cooresponding comment:
################################################################################




# # Chapter 1

# 1. Which of the following are operators, and which are values?
     *           operator
     'hello'     Value
     -88.8       Value
     -           operator
     /           operator
     +           operator
     5           Value

# 2. Which of the following is a variable, and which is a string?
     spam        variable
     'spam'      string

# 3. Name three data types.
     interger, floating-point, string

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
This causes an error because you cant concatenate integers with strings
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


# 8. Identify the three blocks in this code:

# spam = 0
# if spam == 10:
#     print('eggs')
#     if spam > 5:
#         print('bacon')
#     else:
#         print('ham')
#     print('spam')
# print('spam')

# 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# 10. What keys can you press if your program is stuck in an infinite loop?

# 11. What is the difference between break and continue?

# 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

# 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

# Extra credit: Look up the round() and abs() functions on the internet, and find out what they do. Experiment with them in the interactive shell.





# Chapter 3

# Chapter 4

# Chapter 5

# Chapter 6
