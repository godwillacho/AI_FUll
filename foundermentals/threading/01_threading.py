import threading 
import time

def take_orders():
    for i in range(1,4):
        print(f'taking order #{i} ')
        time.sleep(1)

def brew_chai():
    for i in range(1,4):
        print(f'Brewing chai for #{i}')
        time.sleep(2)

order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

#wait for thread to finish 
order_thread.join()
brew_thread.join()

print(f'all orders taken and chai brewed')