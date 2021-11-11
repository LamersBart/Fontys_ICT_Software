# THREADING https://www.youtube.com/watch?v=IEEhzQoKtQU
import concurrent.futures # voor de andere methode onderaan.
import threading
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Slapen voor {seconds} seconde...')
    time.sleep(seconds)
    print('Klaar met slapen...')

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[2])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

#thread1 = threading.Thread(target=do_something)
#thread2 = threading.Thread(target=do_something)
#thread3 = threading.Thread(target=do_something)

#thread1.start()
#thread2.start()
#thread3.start()

#thread1.join()
#thread2.join()
#thread3.join()

finish = time.perf_counter()

print(f'Klaar in {round(finish-start, 2)} seconde(n)')



# andere methode:
start2 = time.perf_counter()

def do_something2(seconds2):
    print(f'Slapen voor {seconds2} seconde...')
    time.sleep(seconds2)
    return 'Klaar met slapen...'

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something2, 1)
    f2 = executor.submit(do_something2, 1)
    
    print(f1.result())
    print(f2.result())

finish2 = time.perf_counter()

print(f'Klaar in {round(finish2-start2, 2)} seconde(n)')