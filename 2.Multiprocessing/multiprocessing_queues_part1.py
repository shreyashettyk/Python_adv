from multiprocessing import Process
import time

def check_value_in_list(x,i,num_process):
        max_number_to_check = 10 ** 8
        lower = int(i * max_number_to_check / num_process)
        upper = int((i+1) * max_number_to_check / num_process)
        for i in range(lower,upper):
            if(i in x):
                print("TRUE")


if __name__ == '__main__':

    comparision_list = [1,3,8,10589]
    num_process = 4
    processes = []

    
    start_time = time.time()
    # check_value_in_list(comparision_list)
    for i in range(num_process):
        t = Process(target = check_value_in_list,args=(comparision_list,i,num_process),name = "process"+str(i))
        processes.append(t)
        t.start()

    # for t in processes:
    #     t.start()

    for i in range(num_process):
        processes[i].join() 


    print("total time taken ",time.time()-start_time)



