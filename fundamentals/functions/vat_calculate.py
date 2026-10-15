def add_vat(price, vat_rate):
    total = price * vat_rate  + price
    return total 


print(f'the total price including va is : {add_vat(20,0.1)}')
