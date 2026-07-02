import time 

def start_counter(seconds, delay=1):
    for i in range(1, seconds + 1): # Loop from 1 to the specified number of seconds
        print("Counter is at:", i)
        time.sleep(delay)
    print("Counter finished!")

start_counter(10)


## Stopwatch example