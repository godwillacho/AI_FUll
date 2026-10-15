prices = {"small":10 , "meduim":15 , 'large':20}
size = input('What cup size would you want to order(small/large/meduim)? : ').lower()

if size in prices:
    print(f'The price of your order will be {prices[size]} rupees')
else:
    print(f'Unknown cup size')