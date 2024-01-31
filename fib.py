from functools import lru_cache
import time 

def timer(func):
    def wrapper(*args, **kwargs):
        num = args
        begin_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - begin_time
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
    fib(100)
    