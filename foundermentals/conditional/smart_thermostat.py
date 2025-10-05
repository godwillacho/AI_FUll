Device_status = True
temperature = 8
if Device_status:
    if (temperature > 35): 
        print (f'high temperature alert!')
    else:
        print(f'Temperature normal ')
else:
    print(f'Device is offline')