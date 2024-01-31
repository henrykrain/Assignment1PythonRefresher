from functools import lru_cache
import time 
#import matplotlib.pyplot as plt
# def arrs(fib_load_time):
#     arr1 = []
#     for n in range(101):
#         arr1.append(n)

#     arr2=[]
#     for n in range(101):
#         arr2.append(fib_load_time)
#     return (plt.plot[arr1][arr2])

def timer(func):
    def wrapper(*args, **kwargs):
        num = args
        begin_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - begin_time
        #arrs(total_time)
        print(f"Finished in {total_time}: f{num} -> {result}")
        return result
    return wrapper

@lru_cache
@timer
def fib(n:int) -> int:
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    #arrs(fib)
    fib(100)
    #plt.show()
    