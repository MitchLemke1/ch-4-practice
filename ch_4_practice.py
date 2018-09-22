"""
	Complete all of the TODO directions
	The number next to the TODO represents the chapter
    and section that explain the required code
	Your file should compile error free
	Submit your completed file
"""
# TODO 4.2 A condition controlled loop
# write a loop that will change the variable in num by subtracting 1
# then print the variable. Keep looping until the num = 0 (While num > 0)
var1 = 5
while var1 > 0:
    print(var1)
    var1 -= 1

num = 10
# write your code here, the variable needs to exist before
# you test it

# TODO 4.3 the For Loop
# Use a for loop with a list of the days of the week, print each day
# of the week
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
for x in days:
    print(x)

# TODO 4.3 the for loop - range function
# use the range function to print the numbers from 1 to 10
for num in range (1, 11):
    print(num)


# TODO 4.4 a running total
# Have the user enter 5 numbers, provide a total at the end
# You can assume integers

MAX = 5
total = 0.0
print('this program calculates the sum of')
print(MAX, 'numbers you will enter')
for counter in range (MAX):
    number = int(input('enter number: '))
    total = total + number
print('the total is', total)
enter number: 1
enter number: 2
enter number: 3
enter number: 4
enter number: 5
the total is: 15.0


# TODO 4.5 Sentinel Value
# Create a variable to store a total amount
# Create a variable to store a count of the numbers entered
# Have the user enter test scores until a sentinel value of -1 is
# entered.
# Display the total, the count and the average (total / count)


# TODO 4.6 validating data
# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# prompt until the user enters a valid number. Test with
# both valid and invalid data


