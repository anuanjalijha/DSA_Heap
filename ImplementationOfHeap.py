class Heap :
    def __init__(self,max_size : int ) -> None :
        self.heap= [0 for _ in range (max_size)]
        self.size= 0 
    def compare(self,a,b)->bool:
        return b>a 
    def swap (self, idx1,idx2):
        self.heap[idx1] ,self.heap[idx2]= self.heap[idx2],self.heap[idx1]
    def insert(self ,val: int ) ->None :
        self.size +=1 
        self.heap [self.size]= val 
        idx =self.size 
        while idx>1: 
            parent =idx //2 
            if self.compare(self.heap[parent],self.heap[idx]):
                self.swap(parent,idx)
                idx=parent
            else :
                break 
    def print(self)->None :
        print ("Heap is: ")
        for i in range (1,self.size+1):
            print(self .heap[i],)
            #print ("/n==========")
if __name__=="__main__":
    heap = Heap(10)
    heap.insert(10)
    heap.insert(20)
    heap.insert(30)
    heap.insert(25)
    heap.insert(35)
    heap.print()