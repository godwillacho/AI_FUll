import threading
import asyncio
import time 

def logger():
    while True:
        print(f"[]files are being logged ")
        time.sleep(2)

count = 0

t = threading.Thread(target=logger,daemon=True)
t.start()
while count < 10:
    print(f'{count + 1} Doing my own stuff')
    count += 1
    time.sleep(2)
