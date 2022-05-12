## ================================Chapter1============================================== ##

## ================================Chapter2============================================== ##

# # Exercise 1
# '''
# Hello World!
# '''
# print("Hello World!")

# # Exercise 2  
# '''
# Calculates and displays the projected profit of a company.
# Assumes the annual profit is usually 23% of total sales.
# '''
# sales = float(input('Enter the amount of projected sales: '))
# profit = sales * .23
# print("The project profit is", format(profit, ',.2f'))

# # Exercise 3 
# '''
# Uses the total square feet in a tract of land and calculates the number of acres in the tract.
# One acre of land is equivalent to 43,560 square feet.
# '''
# SQ_FEET_PER_ACRE = 43560
# total_sqaure_feet = int(input("Enter total sqaure feet of your property: "))

# acres = total_sqaure_feet / SQ_FEET_PER_ACRE

# print('Total acres is: ', format(acres, '.2f'))
 
# # Exercise 4  
# '''
# Calculates the subtotal, sales tax, and overall total of five items.
# Assumes sales tax is 7%
# '''
# TAX_RATE = 0.07

# item1 = float(input("Enter the price of item #1: "))
# item2 = float(input("Enter the price of item #2: "))
# item3 = float(input("Enter the price of item #3: "))
# item4 = float(input("Enter the price of item #4: "))
# item5 = float(input("Enter the price of item #5: "))

# subtotal = item1 + item2 + item3 + item4 + item5
# tax = subtotal * TAX_RATE
# total = subtotal + tax

# print('Subtotal: ', format(subtotal, '10.2f'))
# print('Sales Tax: ', format(tax, '10.2f'))
# print('Total: ', format(total, '10.2f'))

# # Exercise 7  
# '''
# Calculate a car's miles-per-gallon (MPG).
# Use this formula: MPG = miles driven / gallons of gas used
# '''
# # input
# miles_driven = int(input("Enter the miles driven: "))
# gallons_of_gas_used = int(input("Enter the amount of gas used: "))

# # processing
# mpg = miles_driven / gallons_of_gas_used

# # output
# print("Your miles per gallon is:", format(mpg, '.2f'))

# # Exercise 9 
# '''
# Convert Celsius temperatures to Fahrenheit temperatures.
# Use this formula: F = (9/5)C + 32
# '''
# celsius_temp = int(input("Enter temperature in Celsius: "))

# fahrenheit_temp = 9/5 * celsius_temp + 32

# print('Temperature in Fahrenheit:', format(fahrenheit_temp, '.2f'))
 
# # Exercise 11
# '''
# Calculate and display the percentage of males and females in a class.
# '''
# males = int(input("Enter the number of male students: "))
# females = int(input("Enter the number of female students: "))

# class_total = males + females
# percent_of_males = males / class_total
# percent_of_females = females / class_total

# print('Male students:', format(percent_of_males, '.0%'))
# print('Female students:', format(percent_of_females, '.0%'))

## ================================Chapter3============================================== ##

# # Exercise 1
# '''
# Ask user for a number and display a day of the week.
# Monday = 1, Tuesday = 2...
# '''
# def main():
#     day = int(input('Enter the day of the week: '))
#     if day == 1:
#         print('Monday')
#     elif day == 2:
#         print('Tuesday')
#     elif day == 3:
#         print('Wednesday')
#     elif day == 4:
#         print('Thursday')
#     elif day == 5:
#         print('Friday')
#     elif day == 6:
#         print('Saturday')
#     elif day == 7:
#         print('Sunday')
#     else:
#         print('Please enter a value 1 through 7')

# if __name__ == '__main__':
#     main()

# # Exercise 3
# '''
# Determine whether a person is an infant, child, teenager, or an adult based on user input.
# '''
# def main():
#     age = int(input('Enter your age: '))
#     if age <= 1:
#         print('Infant')
#     elif age > 1 and age < 13:
#         print('Child')
#     elif age >= 13 and age < 20:
#         print('Teenager')
#     elif age >= 20:
#         print('Adult')

# if __name__ == '__main__':
#     main()

# # Exercise 12
# '''
# Calculate and display the amount of the discount (if any) 
# and the total amount of the purchase after the discount.
# Assumes the retail price is $99.
# | Quantity  | Discount |
# |  10-19    |   10%    |
# |  20-49    |   20%    |
# |  50-99    |   30%    |
# |  100-more |   40%    |
# '''
# retail = 99
# discount = 0
# quantity = float(input('Enter the number of packages purchased: '))

# def main():
#     price = retail * discount
#     price = retail - price
#     print('Discount: ', format(discount, '.0%'))
#     print('Total: ', format(price, '.2f'))

# if quantity >= 10 and quantity <= 19:
#     discount = 0.1
#     main()
# elif quantity >= 20 and quantity <= 49:
#     discount = 0.2
#     main()
# elif quantity >= 50 and quantity <= 99:
#     discount = 0.3
#     main()
# elif quantity >= 100:
#     discount = 0.4
#     main()
# else:
#     discount = 0
#     main()

# # Exercise 14
# '''
# Calculate and display a person's body mass index (BMI).
# Also display whether the person is underweight, at optimal weight or overweight.
# Uses this formula: BMI = weight * 703/height^2
# '''
# weight = float(input('Enter your weight in pounds: '))
# height = float(input('Enter your height in inches: '))
# bmi = weight * 703/height**2

# def main():
#     if bmi >= 18.5 and bmi <= 25:
#         print("You're at optimal weight")
#     elif bmi < 18.5:
#         print('You are underweight')
#     elif bmi > 25:
#         print('You are overweight')

# if __name__ == '__main__':
#     main()

# # Exercise 17
# '''
# Walk the user through the troubleshooting process
# for fixing a bad Wi-Fi connection.
# '''
# print('Reboot the computer and try to connect.')

# def main():
#     user = input('Did that fix the problem?: ')
#     if user == 'no':
#         print('Reboot the router and try to connect.')
#         user = input('Did that fix the problem?: ')
#     if user == 'no':
#         print('Make sure the cables between the router and modem are plugged in firmly.')
#         user = input('Did that fix the problem?: ')
#     if user == 'no':
#         print('Move the router to a new location.')
#         user = input('Did that fix the problem?: ')
#     if user == 'no':
#         print('Get a new router.')
#     else:
#         print('Your solution has been solved.')

# if __name__ == '__main__':
#     main()

## ================================Chapter4============================================== ##

# # Exercise 4
# '''
# Display the distance a vehicle has traveled for a period of time (in hours).
# Uses this formula: distance = speed * time
# '''
# def main():
#     # prompt for speed
#     speed = float(input("What is the speed of the vehicle in mph? "))
#     # prompt for hours traveled
#     hours = int(input("How many hours has it traveled? "))

#     # loop for each hour traveled
#     #   calculate distance traveled = speed * hour
#     #   print the hour and distance traveled
#     print('Hour\tDistance Traveled')
#     for hour in range(1, hours + 1):
#         distance = speed * hour
#         print(hour, '\t', format(distance, '.0f'))

# if __name__ == '__main__':
#     main()

# # Exercise 8
# '''
# Ask user for a series of positive numbers and displays their sum. 
# '''
# def main():
#     number_sum = 0.0
#     number = 1
#     while number > 0:
#         number = float(input("Enter a positive number (negative to end): "))
#         if number > 0:
#             number_sum += number

#     print("The sum is", number_sum)

# if __name__ == '__main__':
#     main()

# # Exercise 10
# '''
# Calculate and display the tuition rate of a college for the next 5 years.
# Assumes the current tuition is $8,000 and the tuition will increase 3% each year for the next 5 years.
# '''
# TUITION = 8000.0
# RATE = .03
# NUMBER_OF_YEARS = 5

# def main():
#     new_tuition = TUITION
#     for year in range(1, NUMBER_OF_YEARS + 1):
#         increase_sum = new_tuition * RATE
#         new_tuition += increase_sum
#         print(year, '\t', format(new_tuition, '.2f'))

# if __name__ == '__main__':
#     main()

# # Exercise 12
# '''
# Calculates the factorial of a given number.
# '''
# def factorial(number):
#     result = 1
#     # use a loop to calculate the factorial of the number
#     for num in range(1, number + 1):
#         result *= num

#     # return the calculated factorial
#     return result

# def main():
#     # prompt the user for a positive integer
#     number = 0
#     # prompt until a positive integer is entered
#     while number < 1:
#         number = int(input("Enter a positive integer: "))

#     # call the factorial function with the number as an argument
#     answer = factorial(number)

#     # print the value returned from the factorial function
#     print("The factorial of", number, "is", answer)

# if __name__ == '__main__':
#     main()

# # Exercise 14
# '''
# Displays a pattern using nested loops.
# '''
# def main():
#     for r in range(7, 0, -1):
#         for c in range(r, 0, -1):
#             print('*', end='')
#         print()

# if __name__ == '__main__':
#     main()

## ================================Chapter5============================================== ##

# # Exercise 15
# '''
# Ask user to enter 5 test scores.
# Display the letter grade for each test and 
# the average test score.
# '''
# def calc_average(score1, score2, score3, score4, score5):
#     '''
#     Acceot 5 test scores as arguments.
#     Return average of scores.
#     '''
#     total = score1 + score2 + score3 + score4 + score5
#     average = total / 5
#     return average

# def determine_grade(score):
#     '''
#     Accept a test score as an argument.
#     Return a letter grade based on the following scale:
#     | Score  | Letter Grade |
#     | 90-100 |   A    |
#     | 80-89  |   B    |
#     | 70-79  |   C    |
#     | 60-69  |   D    |
#     | > 60   |   F    |
#     '''
#     grade = ''
#     if score >= 90 and score <= 100:
#         grade = 'A'
#     elif score >= 80 and score <= 89:
#         grade = 'B'
#     elif score >= 70 and score <= 79:
#         grade = 'C'
#     elif score >= 60 and score <= 69:
#         grade = 'D'
#     elif score < 60:
#         grade = 'F'
#     return grade

# def main():
#     s1 = float(input("Enter score 1: "))
#     s2 = float(input("Enter score 2: "))
#     s3 = float(input("Enter score 3: "))
#     s4 = float(input("Enter score 4: "))
#     s5 = float(input("Enter score 5: "))

#     average = calc_average(s1, s2, s3, s4, s5)

#     print("score       numeric grade    letter grade")
#     print("======================================================================")
#     print("score 1:\t", s1, '\t\t', determine_grade(s1))
#     print("score 2:\t", s2, '\t\t', determine_grade(s2))
#     print("score 3:\t", s3, '\t\t', determine_grade(s3))
#     print("score 4:\t", s4, '\t\t', determine_grade(s4))
#     print("score 5:\t", s5, '\t\t', determine_grade(s5))

#     print("======================================================================")
#     print("Average score:\t", average, '\t\t', determine_grade(average))

# if __name__ == '__main__':
#     main()

# # Exercise 17
# '''
# Prompt user for input and determine whether the number is prime.
# '''
# def is_prime(number):
#     num = 0
#     for prime_number in range(1, number + 1):
#         if number % prime_number == 0:
#             num = num + 1
#             if num > 2:
#                 return False
#     return True

# def main():
#     number = int(input('Enter a number: '))
#     if is_prime(number):
#         print(number, "is a prime number.")
#     else:
#         print(number, "is not a prime number.")

# if __name__ == '__main__':
#     main()

# # Exercise 18
# '''
# Displays all prime numbers from 1 to 100.
# '''
# from main import is_prime

# def main():
#     for prime_number in range(1, 101):
#         if is_prime(prime_number):
#             print(prime_number)

# if __name__ == '__main__':
#     main()

## ================================Chapter6============================================== ##

# # Exercise 1
# '''
# Displays contents of numbers.txt
# '''
# def main():
#     # Open file for reading
#     infile = open('numbers.txt', 'r')
    
#     numbers = infile.read()

#     # Close file
#     infile.close()

#     # Print contents of file
#     print(numbers)

# # Call the main function
# main()

# # Exercise 2
# '''
# Displays the first 5 lines of a specified file.
# '''
# def main():
#     # Declare variables
#     counter = 0
#     line = ''

#     # Prompt for file name
#     file_name = input('Enter the name of the file: ')

#     # Open the specified file for reading
#     infile = open(file_name, 'r')

#     # Print reading
#     line = infile.readline()
#     counter = 1

#     # Read and display first five lines
#     while line != '' and counter <= 5:
#         # Strip '\n'
#         line = line.rstrip('\n')
#         print(line)
#         line = infile.readline()
#         # Update counter when line is read
#         counter += 1

#     # Close file
#     infile.close()

# # Call the main function
# main()

# # Exercise 3
# '''
# Displays contents of a specified file in a number list format.
# '''
# def main():
#     # Declare variables
#     line = ''
#     counter = 0

#     # Prompt for file name
#     file_name = input('Enter the name of the file: ')

#     # Open specified file for reading
#     infile = open(file_name, 'r')

#     # Read and display file contents in numberical order
#     for line in infile:
#         counter += 1
#         print(counter, end='')
#         print(':', end=' ')
#         # Strip '\n'
#         line = line.rstrip('\n')
#         print(line)

#     # Close file
#     infile.close

# # Call the main function
# main()

# # Exercise 4
# '''
# Displays the number of names from names.txt
# '''
# def main():
#     # Define variables
#     counter = 0

#     # Open names.txt file for reading
#     infile = open('names.txt', 'r')

#     # Read in until no more data
#     for line in infile:
#         counter += 1

#     # Close file
#     infile.close()

#     # Display the number of names in the file
#     print(counter, 'names were read.')

# # Call the main function
# main()

# # Exercise 6
# '''
# Calculate and display the average of all numbers stored in numbers.txt
# '''
# def main():
#     # Define variables
#     counter = 0
#     sum = 0.0

#     # Open numbers.txt file for reading
#     infile = open('numbers.txt', 'r')
#     for line in infile:
#         counter = counter + 1
#         number = float(line)
#         sum += number

#     # Close file
#     infile.close()

#     # Calculate average
#     average = sum / counter

#     # Display average of numbers in file
#     print('Average:', sum)

# # Call the main function
# main()

# # Exercise 9
# '''
# Practice with exception handling. Raises an IOError and ValueError exceptions.
# '''
# def main():
#     # Define variables
#     counter = 0
#     sum = 0.0
#     try:

#         # Open numbers.txt file for reading
#         infile = open('numbers_errors.txt', 'r')
#         for line in infile:
#             counter = counter + 1
#             number = float(line)
#             sum += number

#         # Close file
#         infile.close()

#         # Calculate average
#         average = sum / counter

#         # Display average of numbers in file
#         print('Average:', sum)

#     except IOError:
#         print('An error occurred trying to read the file.')
#     except ValueError:
#         print('Non-numeric data found in the file.')

# # Call the main function
# main()

# Reverse Strings
# s1 = '123456789'
# s2 = ''
# for i in range(len(s1)-1, -1, -1):
#     s2 += s1[i]
# print(s2)

## ================================Chapter7============================================== ##

# # Exercise 1
# '''
# Stores sales data into a list. Uses a loop to calculate total sales for the week and displays result. 
# '''
# def main():
#     # Create a list with 7 containers
#     amounts = [0] * 7

#     # Prompt user to enter sales
#     # # DRY principle: Don't Repeat Yourself
#     index = 0
#     while index < len(amounts):
#         amounts[index] = float(
#             input('Enter day ' + str(index + 1) + ' sales: '))
#         index += 1

#     # Calculate sales of the week 
#     total = 0.0
#     for day_sales in amounts:
#         total += day_sales

#     # Print the total 
#     print('Total sales for the week are:', total)

# main()

# # Exercise 4
# '''
# Prompt user for a series of 20 numbers. Store numbers in a list and display the lowest and highest numbers, total numbers, and average of the numbers.
# '''
# import random

# def display_stats(number_list):
#     total = 0
#     for value in number_list:
#         total += value
#     print('min=', min(number_list), 'max=', max(number_list), 
#         'total=', total, 'avg=', total/len(number_list), sep='')

# def main():
#     # define a list to hold the numbers
#     number = [] 
#     # generate the list of 20 random numbers
#     for i in range(20):
#         number.append(random.randrange(1, 100))

#     # call a function to display the data
#     display_stats(number)
    
# main()

# # Exercise 5
# '''
# Ask user for charge account number and determine whether the number is in the charge_accounts.txt file or not.
# '''
# def main():
#     # Read the contents of the file into a list
#     infile = open('charge_accounts.txt', 'r')

#     charge = infile.readlines()

#     infile.close()

#     index = 0
#     while index < len(charge):
#         charge[index] = charge[index].rstrip('\n')
#         index += 1

#     # Ask user to enter a account number
#     search = input('Enter a charge account number: ')

#     # Determine whether the number is valid by searching list
#     if search in charge:
#         print(search, 'was found in our system.')
#     else:
#         print(search, 'was not found in our system.')

# main()

# # Exercise 6
# '''
# Accepts two arguments: a list, and a number n. Display all the numbers in the list that are greater than the number n.
# '''
# def larger_than_n(list1, n):
#     numbers = []
#     for value in list1:
#         if value > n and value not in numbers:
#             numbers.append(value)
#     return numbers

# # Lists
# num = [2,3,4]
# print()
# print(all(x > 1 for x in num))
# print(all(x > 4 for x in num))
# print()

# numbers = [5, 10, 15, 20]
# print(numbers)
# print('\n')

# print('A list of numbers generated with range(5)')
# numbers = list(range(5))
# print(numbers)
# print('\n')

# print('A list of numbers generated with range(2, 52, 2)')
# numbers = list(range(2, 52, 2))
# print(numbers)
# print('\n')

# # repetition operator
# numbers = [0] * 5
# print(numbers)

# numbers = [1, 2, 3] * 3
# print(numbers)

# # Similar to arrays in other languages
# # Arrays are more limited than lists
# # Python does not have an array type

# # A list is an iterable type - same as a string
# for i in numbers:
#     print(i, end=' ')
# print('\n')

# # indexing to access individual element of a list
# numbers = list(range(2, 21, 2))
# print(numbers[0], numbers[-1], numbers[-2])

# for i in range(len(numbers)):
#     print(numbers[i], end=' ')
# print('\n')

# # This is better code than using an index as above
# for n in numbers:
#     print(n, end=' ')
# print('\n')

# print('Printing each character in a string with a space between each character.')
# for ch in 'abc123efg456':
#     print(ch, end=' ')
# print('\n')

# print('This list of numbers', numbers, 'is a length of', len(numbers))
# try:
#     numbers[len(numbers)]
# except IndexError as e:
#     print('An index of', len(numbers), "results in a '", end='')
#     print(e, end='')
#     print("' exception.")

# numbers = list(range(10, 50, 10))
# print(numbers)
# index = 0
# while index < 5:
#     print(index, ': ', numbers[index], sep='')
#     index += 1
# print('\n')

# numbers = list(range(4))
# index = 0
# try:
#     while index < 5:
#         x = numbers[index]
#         index += 1
# except IndexError as e:
#     print('An index of', len(numbers), "results in a '", end='')
#     print(e, end='')
#     print("' exception.")
# print('I can keep going, because the program did not crash.')

# my_list = [10, 20, 30, 40]
# print(my_list[-1], my_list[-2], my_list[-3], my_list[-4])

# # Lists are mutable - they can be changed unlike strings
# numbers = list(range(2, 21, 2))
# print(numbers)
# numbers[0] = 11
# numbers[-1] = 99
# print(numbers)

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# list3 = list1 + list2
# print(list3)
# list1 += list2
# print(list1)
# print(list2)

# dinner_choices = ['Pizza', 'Tacos', 'Chicken']
# drink_choices = ['Cola', 'Ice Tea', 'Lemonade']
# menu_items = dinner_choices + drink_choices
# print(menu_items)

# # Slicing
# days = ['Sunday', 'Monday', 'Tuesday',
#         'Wednesday', 'Thursday', 'Friday', 'Saturday']
# mid_days = days[2:5]
# print(mid_days)

# print(days[0:3])
# print(days[:3])

# print(days[5:])

# print(days[5:])

# print(days[:])

# numbers = list(range(10, 110, 10))
# print(numbers)

# print(numbers[1:6:2])

# print(numbers[1::2])

# print(numbers[-5:])

# print(numbers[-5:7])

# # If the end index specifies a position beyond the end of the list,
# # Python will use the length of the list instead.
# print(numbers[3:27])

# # If the start index specifies a position before the beginning of the list,
# # Python will use 0 instead.
# print(numbers[-27:3])

# # If the start index is greater than the end index,
# # the slicing expression will return an empty list
# print(numbers[27:3])

# numbers.reverse()
# print(numbers)

# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

## ================================Chapter8============================================== ##

## ================================Chapter9============================================== ##

# Exercise 1
'''
Dictionary containing course numbers, room numbers, 
instructors, and meeting times. 
Displays information about a specified course.
'''
def course_directory():
    CourseNumber = ('CS101', 'CS102', 'CS103', 'NT110', 'CM241')
    RoomNumber = (3004, 4501, 6755, 1244, 1411)
    Instructor = ('Haynes', 'Alvarado', 'Rich', 'Burke', 'Lee')
    MeetingTime = ('8:00 a.m.', '9:00 a.m.',
                   '10:00 a.m.', '11:00 a.m.', '1:00 p.m')
    Room = dict()
    Prof = dict()
    Time = dict()
    for index in range(len(CourseNumber)):
        Room[CourseNumber[index]] = RoomNumber[index]
        Prof[CourseNumber[index]] = Instructor[index]
        Time[CourseNumber[index]] = MeetingTime[index]
    return CourseNumber, Room, Prof, Time

def main():
    CourseNumber, RoomNumber, Instructor, MeetingTime = course_directory()
    select = input("Enter a course number: ")
    print()
    if select in CourseNumber:
        print('Room Number: ', RoomNumber[select])
        print('Instructor: ', Instructor[select])
        print('Meeting Time: ', MeetingTime[select])
    else:
        print('This course could not be found.')

main()
