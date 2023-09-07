
from time import time
from multiprocessing.dummy import Pool as ThreadPool

def create_threads(list, function):
    
    num_threads_str = input("\nNumber of threads (5): ") or "5"
    num_threads = int( num_threads_str )

    threads_list = []

    for ip in list:
        threads_list.append((ip))

    starting_time = time()

    th = ThreadPool( num_threads )
    results = th.map( function, threads_list )

    th.close()
    th.join()
    
    print('\n---- End get config threadpool, elapsed time=', time()-starting_time)
        