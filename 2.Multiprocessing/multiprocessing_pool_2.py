from multiprocessing import Pool,cpu_count
from functools import partial
import time
import os

pid_list = []
number_cores = max(1,cpu_count()-1)
power = 3
additional_component = 2

def square(exponent,add_comp,x):
    print(exponent)
    print("PID data is ",os.getpid(),"input value is ",x)
    time.sleep(3)
    # print(os.getpid())
    return x**exponent + add_comp




if __name__ == '__main__':
    print("*"*10)
    print(f'Operating on {number_cores} cores')
    print("PID of the main process is ",os.getpid())
    print("*"*10)
    comparision_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    partial_function = partial(square,power,additional_component)
    start_time = time.time()
    with Pool(number_cores) as mp_pool:
       result = mp_pool.map(partial_function,comparision_list)
    end_time = time.time()

    print("total time ")
    print(end_time-start_time)
    print("Result is ",result)
    
