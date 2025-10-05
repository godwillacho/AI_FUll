import threading
import requests
import time

def download(url):
    print(f"starting download  start ")
    resp = requests.get(url )
    print(f'Finished downloading from{url},size: {len(resp.content)}bytes')

urls = [
    'https://httpbin.org/image/jpeg',
    'https://httpbin.org/image/png',
    'https://httpbin.org/image/svg',
]
start = time.time()
thread_pool = []
count = 0
for url in urls:
    th = threading.Thread(target=download,args=(url,),name= f'thread {count+1}')
    thread_pool.append(th)
    th.start()
    print(f'Thread {th.name} has been started ')
for th in thread_pool:
    th.join()


end =time.time()
print(f'ALL downloads where done in {end-start:.2f}seconds')

