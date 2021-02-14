# threading - to speed up of programs, running tasks concurrently

import time, threading

start = time.perf_counter()

def somefunction(second):
    print(f'Task done for {second} second(s).')
    time.sleep(second)
    print('Done Task')

#1
# somefunction()
# somefunction()

#2
# thread1 = threading.Thread(target=somefunction)
# thread2 = threading.Thread(target=somefunction)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

#3
# listOfThreads = []

# for _ in range(10):
#     t = threading.Thread(target=somefunction, args=[1.5])
#     t.start()
#     listOfThreads.append(t)

# for thread in listOfThreads:
#     thread.join()

#4 thread pool executer, using concurrent future module

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)')