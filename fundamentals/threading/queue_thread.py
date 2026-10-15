import time 
import threading

def cpu_hevy():
    print(f'Crunching some numbers...')
    total = 0
    for i in range(10**8):
        total += 1
    print('Done ')
start =time.time()
th =[threading.Thread(target=cpu_hevy) for _ in range(2)]
[t.start() for t in th]
[t.join() for t in th]

print(f'Time taken: {time.time() - start:.2f} seconds')