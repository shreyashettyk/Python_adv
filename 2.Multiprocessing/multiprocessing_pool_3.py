from multiprocessing import Pool,cpu_count
from functools import partial
import time
import os

pid_list = []
number_cores = max(1,cpu_count()-1)
power = 3
additional_component = 2
comparision_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
range_list = [(0,25*10**6),(25*10**6,50*10**6),(50*10**6,75*10**6),(75*10**6,10**8)]
range_list = [(0,25*10**2),(25*10**2,50*10**2),(50*10**2,75*10**2),(75*10**2,10**4)]

def comparision_in_list(comp_list,lower,upper):
    number_hits = 0
    for i  in range(lower,upper):
        print(f"The pid value os {os.getpid()} and input processed is ",(lower,upper))
        if i in comp_list:
            number_hits +=1
        time.sleep(0.1)
    return number_hits



if __name__ == '__main__':
    print("*"*10)
    print(f'Operating on {number_cores} cores')
    print("PID of the main process is ",os.getpid())
    print("*"*10)
    input_list = []
    for i in range(len(range_list)):
        input_list.append((comparision_list,*range_list[i]))
    
    start_time = time.time()
    with Pool(number_cores) as mp_pool:
       result = mp_pool.starmap(comparision_in_list,input_list)
    end_time = time.time()

    print("total time ")
    print(end_time-start_time)
    print("Result is ",result)
    
