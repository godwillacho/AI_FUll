from multiprocessing import Process
import time 

def cpu_hevy():
    print(f'Crunching some numbers...')
    total = 0
    for i in range(10**8):
        total += 1
    print('Done ')

if __name__ == '__main__':
    start = time.time()
    processes  = [Process(target=cpu_hevy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]

    print(f'Time taken: {time.time() - start:.2f}seconds')