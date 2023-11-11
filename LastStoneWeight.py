from sys import stdin
import sys
sys.setrecursionlimit(10**7) 
from queue import PriorityQueue

def weightOfLastStone(stones, n) :
    pq= PriorityQueue()

    for i in range(n) :
        # By default it is min heap so inserting negative values to get the max value at top
        pq.put(-stones[i])

    while (pq.qsize()>1) :
        
        # Weight of Heaviest stone
        x = -pq.get()   

        # Weight of second heaviest stone
        y = -pq.get() 

        # If not equal
        if (x - y > 0) : 
            pq.put(-(x - y))   

    # If all the stones are destroyed.
    if (pq.qsize() == 0):
        return 0   
    
    # If elment left return's its value (negative sign is because we have inserted the negative of the actual value)
    return -pq.get()   
    
    
