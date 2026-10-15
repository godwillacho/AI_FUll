# menu =[
#     'ndop rice',
#     'ndole',
#     'kati kati',
#     'nangtari',
# ]

# ndole = [ meal for meal in menu if '' in meal]
# fufu = list(filter(lambda x: x !="kati kati",menu ))
# print(ndole)
# print(fufu)

chef = {
    'kati kati': ['chicken','palm oil','njanga'],
    'nangtari': ['cocoyam','palm oil ','njanga'],
    'ndole': ['bitterleaf','njanga','groundnut'],
}
menu_pricing = {
    'kati kati': 45,
    'nangtari': 35,
    'ndole': 40,
}
    
unique_spice = { ingrideint for spice in chef.values() for ingrideint in spice}
print(unique_spice)
 
menu_pricing_dollar = {meal:price * 100 /559 for meal, price in menu_pricing.items()}
print (menu_pricing_dollar)