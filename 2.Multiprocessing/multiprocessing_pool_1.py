from multiprocessing import Pool,cpu_count
import time
import os

pid_list = []


def square(x):
    print()
    print("PID data is ",os.getpid(),"input value is ",x)
    time.sleep(3)
    # print(os.getpid())
    return x*x

number_cores = max(1,cpu_count()-1)


if __name__ == '__main__':
    print("*"*10)
    print(f'Operating on {number_cores} cores')
    print("PID of the main process is ",os.getpid())
    print("*"*10)
    comparision_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_time = time.time()
    with Pool(number_cores) as mp_pool:
        print("the mppool value is ",mp_pool)
        result = mp_pool.map(square,comparision_list)
    end_time = time.time()

    print("total time ")
    print(end_time-start_time)
    print("Result is ",result)
    
