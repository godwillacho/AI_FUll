import threading
import time

def boil_milk():
    print('boiling milk')
    time.sleep(2)
    print(f'milk is boiled')
def toast_bun():
    print(f'Taosting bun...') 
    time.sleep(3)
    print(f'bun taostd ')

start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()

t1.join()
t2.join()

end =time.time()

print(f'time :{end-start:.2f}')