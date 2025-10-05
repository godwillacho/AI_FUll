clients = [
    {"ID":1,"TOTAL":100,"COUPON":"P20"},
    {"ID":2,"TOTAL":200,"COUPON":"D15"},
    {"ID":3,"TOTAL":80,"COUPON":"P45"},
    {"ID":4,"TOTAL":70,"COUPON":"C10"},
    {"ID":5,"TOTAL":130,"COUPON":"M20"},
    
]
discounts = {
    "P20" : (0.2, 0),
    "D15" : (0.6, 0),
    "P45" : (0.1, 15),
    "C10" : (0.5, 0),
    "M20" : (0, 40),
    
}

for client in clients:
    percentage,fixed = discounts.get(client["COUPON"], (0,0))
    discount = client['TOTAL'] * percentage  + fixed 
    print(f"{client["ID"]} paid {client["TOTAL"]} and got a discount of {discount}") 

   