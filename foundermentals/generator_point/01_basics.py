# def infinite_chai():
#     count =1 
#     while True:
#         yield f'refil #{ count}'
#         count += 1

# refill = infinite_chai()

def taking_order():
    print("enter the name of the meal your interested in having ")
    meal = yield 
    while True:
        print(f'preparing {meal}')
        meal = yield 

kitchen = taking_order()
next(kitchen)

kitchen.send('koki')
kitchen.send('kwacoco')
