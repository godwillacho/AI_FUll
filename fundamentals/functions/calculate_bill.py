def calculate_bill(cups, price_per_cup):
    totalbill = cups * price_per_cup 
    print(f'your total bill is {totalbill}')
    return totalbill

calculate_bill(3,20)