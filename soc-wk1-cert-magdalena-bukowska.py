import datetime
from datetime import date

# How many hours are in a year

print('####################################')
print('##### Summer of Code - Week 1 ######')
print('####################################')

# ------------------------ DAY 1 ------------------------- 

print('DAY 1')

print('---------------------------------------')
print('1. How many hours are in a year?')

hoursInYear = 365 * 24

print('There are ', hoursInYear ,' hours in a year')
print('-----------------------------------------')


# How many minutes are in a decade?

print('2. How many minutes are in a decade?')

minutesInDecade = 365 * 10 * 24 * 60

print('There are '+ str(minutesInDecade) + ' minutes in a decade')
print('-----------------------------------------')


# How many seconds old are you? 

print('3. How many seconds old are you?')

secondsInYear = hoursInYear * 60 * 60
ageInSeconds = 35 * secondsInYear

print('I am '+ str(ageInSeconds) + ' seconds old')
print('-----------------------------------------')


# Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age, there was a mistake in her calculation, need to multiply it by 24

print('4. Andrea is 1166832000 seconds old. What is her age?')

andreasAge = int(1166832000 / secondsInYear)

print('Andrea is ' + str(andreasAge) + ' years old')
print('-------------------------------------------')


# How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
# So there has been some discussion on the mentor channel about the 32-bit problem too (it is a bit confusing to the mentors too, so you're all doing good :smiley: ). Some suggested this is the full problem:
# if the integer is 32-bit, and you have a system that increases it by 1 every milisecond, how many days will it take to overflow? So you would need to know the maximum of a 32-bit integer.
# @Katalin M  you are definitely thinking in the right direction.
# @Paula - mentor  thanks Paula, but unfortunately, this was a tip by a mentor, not own :joy:  So first I have to figure the maximum value of 32 bit integer and then just divide the number to dates. Something like this?
# @Paula - mentor  how do we know that the system increases it by 1 in every milisecond?
# maybe it's something obvious, Im just too beginner.
# @Katalin M That's a missing information in this question. Systems keep track of time passed as variables by incrementing them in set intervals. Some increment it by 1 every 1 second (UNIX for example as you discovered.) Some every 100 nano seconds. (Notably some languages in windows system) And there was another related bug in computers on Airplane engines That would cause them to shutdown on midflight if they kept turned on without completely shutting down (Not just stopped) Fortunately no pilots kept their engines without turning off for that long. And the bug was discovered while reviewing the code.
# Yes as @Paula - mentor mentioned specify any of your assumptions when in doubt
# While the question is not totally clear, you are on the right track. I wrote you not to use a fixed date. I meant by that, do not read the date from somewhere, as you said you did, and just calculate the days until than. You need to understand where that date is coming from, and basically calculate it yourself.
# What is clear is the end date. What is not totally clear in the question  is where to start counting the days. That you can ask from Ilona.
# But if you manage to calculate the end date, you did the most important part of the puzzle :).

print('5. How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?')




print('-------------------------------------------')


# How about a 64-bit system?

print('6. How many days does it take for a 64-bit system to timeout, if it has a bug with integer overflow?')

print('-------------------------------------------')


# Calculate your age accurately based on your birthday

print('7. Calculate your age accurately based on your birthday')

dateNow = datetime.date.today()
myDateOfBirth = datetime.date(1983, 4, 12)

myAgeInDays = dateNow - myDateOfBirth


print(dateNow)
print(myDateOfBirth)
print(myAgeInDays)

# from datetime import date

# def calculate_age(born):
#     today = date.today()
#     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

print('-------------------------------------------')

# http://www.agapow.net/programming/python/convert-timedelta-to-float/


# hackaton @Silvia [Gold] Regarding the hackathon task, you've got the right idea about using an array of arrays, but don't forget that this task is for the whole week so you'll learn more about how to use python to do this as the week goes on. I'd recommend learning how to use loops in Python. For the logic of looping you can use the recommended learn to program book and then you can google python loops to see how python implements that logic.
# Regarding whether you should create a world with pre-defined continents, that is up to you. If you look at the details for the week1 hackathon again you'll see that you can get bonus points for making it randomly generated but you certainly don't need to start out that way. I'd recommend fulfilling the purpose of the task which is to count the size of continents before you expand upon the task with the bonus features

# ------------------------ DAY 3 ------------------------- 

print('DAY 3')
print('-------------------------------------------')

# Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.

print('1. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.\n')

firstName = input('Enter first name: ')
middleName = input('Enter second name: ')
lastName = input('Enter last name: ')

print('Hello', firstName, middleName, lastName, '! Nice to meet you!' )

# Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number.

print('-------------------------------------------')
print('2. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number.')

favNumber = int(input('What is your favourite number?'))

print('I think this number ' + str(favNumber + 1) + ' might be better :)')

# Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you.

print('-------------------------------------------')
print('3. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you.')

answer = input('What do you want??!! \n')

bossAnswer = 'whaddaya mean \"' + answer + '\" you\'re fired!!!'

print(bossAnswer.upper())

#  write a program that will display a table of contents

print('-------------------------------------------')
print('4. Write a program that will display a table of contents')

# print('Chapter 1 : Getting started', '{:>30}'.format('page 1'))
# print('Chapter 2 : Lets beggin!', '{:>30}'.format('page 9'))
# print('Chapter 3 : Love to learn Python - part 1', '{:>30}'.format('page 13'))
# chapter1 = 'Chapter 1: Getting started page 1'
# chapter2 = 'Chapter 2 : Lets beggin! page 9'
# chapter3 = 'Chapter 3 : Love to learn Python page 13'
# chapter4 = 'Chapter 4 : Make your dream come true page 19'


# chapter1Length = 70 - len(chapter1)
# chapter2Length = 70 - len(chapter2)
# chapter3Length = 70 - len(chapter3)
# chapter4Length = 70 - len(chapter4)

# print('-------------')

# print(chapter1Length)
# print(chapter2Length)
# print(chapter3Length)
# print(chapter4Length)

print('Chapter 1 : Getting started', 'page 1'.rjust(37, '-'))
print('Chapter 2 : Lets beggin!', 'page 9'.rjust(40, '-'))
print('Chapter 3 : Love to learn Python', 'page 13'.rjust(33, '-'))
print('Chapter 4 : Make your dream come true', 'page 19'.rjust(28, '-'))

