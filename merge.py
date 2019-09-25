import time
import random
import itertools
import heapq

def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list

def merge2(lists):
    #return sorted(list(itertools.chain.from_iterable(lists)))
    return sorted([a for items in lists for a in items])

def timeit(name, func, arg):
    t_start = time.time()
    func(arg)
    elapsed_secs = time.time() - t_start
    print(f"{name} took {elapsed_secs:2.3f}secs")

for n in [10,100,1000,10000,100000]:
    for k in [2,5,10,50,100,1000]:
        lists = []
        for _ in range(k):
            lists.append(sorted([random.random() for _ in range(n)]))
        print(f"\n{k} lists of {n} each")
        timeit("just sort it", merge2, lists)
        timeit("heap merge", merge, lists)
