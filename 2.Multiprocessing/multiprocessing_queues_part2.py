from multiprocessing import Process,Queue,current_process
import time

def check_value_in_list(x,i,num_process,queue_data):
        max_number_to_check = 10 ** 8
        lower = int(i * max_number_to_check / num_process)
        upper = int((i+1) * max_number_to_check / num_process)
        numberof_hits = 0
        for i in range(lower,upper):
            if(i in x):
                numberof_hits += 1
        queue_data.put((lower,upper,numberof_hits,current_process().name))
        



if __name__ == '__main__':

    comparision_list = [1,3,8,5389689]
    num_process = 4
    processes = []
    process_queue = Queue()
    
    start_time = time.time()
    # check_value_in_list(comparision_list)
    for i in range(num_process):
        t = Process(target = check_value_in_list,args=(comparision_list,i,num_process,process_queue),name = "process"+str(i))
        processes.append(t)
        print("process list is ",processes)
        t.start()

    # for t in processes:
    #     t.start()

    for i in range(num_process):
        processes[i].join() 

    
  
    process_queue.put('DONE')
    
    

    while True:
         v = process_queue.get()
         if v == 'DONE':
              break
         
         print("queue data : ",v)

    print("total time taken ",time.time()-start_time)



