print("hello world")
print('kuewu pamela')
print('0----')
print(' ||||')
print('*' * 10 ) 
price = 50
price = 20
price = 80
#this code will print 80. and this is because python execute its code line by line.
print(price)
# lets write an example of a floating point digit
rating = 5.89
print(rating)
# lets write an example of a string
name = 'pamela'
print(name)

# first example
patient_name = input('enter your name: ')
patient_age = input('enter your age: ')
patient_type = input('enter your info: ')
print('hi ' + patient_name)
print('you are ' + patient_age)
print('you are a ' + patient_type)

# second example
#ask two questions: persons name and favourite color. then print a message like "mosh likes blue"
person_name = input('what is your name? ')
favourite_color = input('what is your favourite color? ')
print('his name is ' + person_name)
print(person_name + ' likes '+ favourite_color)

# lets study type conversion
# calculate the age of an individual
#birth_year = input('birth year: ')
#age = 2024 - birth_year
#print(age)
# this particular code prints an error message. this is because the year the individual inputs is assumed by the interpreter as a string and thereby will not be able to perform any arithmetic operation.
# therefore to correct this error you need to write the type of datatype against the value


#corection
birth_year = input('birth year: ')
#lets iclude the built in function type()
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)

#third example
#ask the user their weight (in pounds), convert it to kilogrms and print it on the terminal
weight = int(input('what is your weight in pounds? ')) 
converted = weight * 0.45
print('your weight now in kilograms is ', converted)


#lets learn about strings
course = "python's course for beginners"
print(course[0:-1]) 

# formatted strings
first = 'john'
second = 'smith'
# the formated string is used to get messages in this form
# e.g john [smith] is a coder
msg = f'{first} {second} is a coder'
print(msg)


# lets calculate the length of variables
# to do this you need to use the built in function len()
course_length = 'python program for beginners'
print(course_length.upper())
print(course_length.lower())
print(course_length.title())
print(course_length.find('a'))
print(course_length.replace('program','Program'))
print('for' in course_length)


# math functions
pam = -5.88
print(round(pam))
print(abs(pam))
 