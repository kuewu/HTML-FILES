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
