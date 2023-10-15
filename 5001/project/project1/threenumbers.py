'''
    Ask the user for three numbers and print the biggest and smallest and the average of these numbers.
'''

# Input the nums and convert them into int form in order to calculate
num1 = int(input("please enter the first number: "))
num2 = int(input("please enter the second number: "))
num3 = int(input("please enter the third number: "))

# Find the average of the numbers
average_num = (num1 + num2 + num3) / 3

# Find the max and min number by compare the numbers and output the results
if num1 < num2:
    min_num = num1
    max_num = num2
else:
    min_num = num2
    max_num = num1

if num3 < min_num:
    min_num = num3
else:
    if num3 > max_num:
        max_num = num3

# Output the result
print(
    f'The biggest number is {max_num}, the smallest number is {min_num}, the average number is {average_num}.')
