from multiprocessing import Process, Queue

queue =Queue()

def prepare_chai(queue):
    queue.put('masala chai is ready ')
if __name__ == '__main__':
    p = Process(target=prepare_chai, args=(queue,))
    p.start()
    p.join()
    print(queue.get())


