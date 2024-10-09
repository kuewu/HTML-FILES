import math
print(math.ceil(2.9))
print(math.floor(2.9))


# let finally begin with our if statements
is_hot = False   
is_cold = False     

if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
    
elif is_cold:
    print("it's a cold")
    print("wear warm clothes")
    
else:
    print("it's a lovely day")
print("enjoy your day")


#examples of if statements
price = 1000000
good_credit = False

if good_credit:
    down_payments = f'${price*0.1}'
    
else:
    down_payments = f'${price*0.2}'
print(f'They need to put down {down_payments}')



# the logical operators
has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print('eligible for loan')
if has_high_income and not has_criminal_record:
    print('eligible for loan')
    
# the comparison operator
temperature = int(input('what is the temperatrure of your area? ')) 
print(temperature)

if temperature > 30:
    print("its a hot day")
elif temperature < 10:
    print("it's a cold day")
else:
    print("its neither hot nor cold")
    
    
#example of comparison operators
name = input("what is your fucken name? ")
print(name)

if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name can be a maximum of 50")
else:
    print("name looks !")
    

#weight converter
weight_of_patient = int(input("what is your weight? "))
print(f'weight: {weight_of_patient}')

type_of_weight = str(input('(L)bs or (K)g: '))
print(type_of_weight.upper())

if type_of_weight == "l":
    print(f'You are {weight_of_patient*0.45} pounds')
elif type_of_weight == "k":
    print(f'you are {weight_of_patient//0.45} kilogram')
else:
    print('you are stupid')
    
    
# the while loop
i = 1

while i <= 5:
    print('*' * i)
    i =i + 1
print("leave me")

# Guessing Game
secret_number = 15
guess_count = 0 
guess_limit = 5


while guess_count < guess_limit :
    guess = int(input('Guess: '))
    guess_count +=1
    if guess == secret_number:
        print('you win')
        if guess == guess:
            print('you repeated the same number')
            break
else:
        print('sorry you failed')
    
    
    
#car game

user_ask_count = ""
started = False
while True :
    user_ask_count =  input('> ').lower()
    if user_ask_count == 'help':
        print('''
start - to start the car
stop -  to stop the car
 quit- to exit''')
    elif user_ask_count == 'start':
        if started:
            print('car already started....')
        else:
            started = True
            print('car started ...... ready to go!')
    elif user_ask_count == 'stop':
        if not started:
            print('car alredy stopped.....')
        else:
            started = False
            print('car stopped..........')
    elif user_ask_count == 'quit':
        break
    else: 
        print("i don't understand that............" )

    
    
#lts time for the for loop
for item in 'python':
    print(item)
for med in range(7,10):
    print(med)
for egg in range(2,10,2):
    print(egg)
prices = [10,20,30,40,50]

total = 0
for price in prices:
    total += price
print(f'total: {total}')