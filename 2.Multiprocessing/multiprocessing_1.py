from multiprocessing import Process
import time

def check_value_in_list(x):
        for i in range(10**8):
            if(i in x):
                print("TRUE")


if __name__ == '__main__':

    comparision_list = [1,3,8]
    num_process = 4
    processes = []

    
    start_time = time.time()
    # check_value_in_list(comparision_list)
    for i in range(num_process):
        t = Process(target = check_value_in_list,args=(comparision_list,))
        processes.append(t)
        
    for t in processes:
        t.start()

    for i in range(num_process):
        processes[i].join() 


    print("total time taken ",time.time()-start_time)



