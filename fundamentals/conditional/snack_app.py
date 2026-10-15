available_snacks = ("cookies","Samosa")

snack = input ("enter your prefered snack").lower()
if snack in available_snacks:
    print(f'your {snack} is being prpared  ')
else:
    print(f'{snack} is not availeble')