import threading
import time

def brew_chai():
    print(f'{threading.current_thread().name} started the brewing process....')
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f'{threading.current_thread().name} finish brewing ....')


thread1 = threading.Thread(target=brew_chai,name='Waiter 1')
thread2 = threading.Thread(target=brew_chai,name='Waiter 2')
thread3 = threading.Thread(target=brew_chai,name='Waiter 3')

start = time.time()
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
end = time.time()

print(f'Just comeback: {end - start :.2f} seconds')
