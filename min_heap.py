class min_heap:
    def __init__(self) -> None:
        self.heap = []  #initialize an empty array as a heap


    def insert(self, value):  #insert values to heap at the end of array then check the heap propertiy by calling heapify up 
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)


    def heapify_up(self,value): 
        parent = (value-1)//2 
        if value >0 and self.heap[value] < self.heap[parent]:
            self.heap[value], self.heap[parent]= self.heap[parent] , self.heap[value]
            self.heapify_up(parent)    


    def extract_min(self):  #remove the minimum value from list then chek the heap propertiy by calling heapify down
        if len(self.heap)==0:
            return
        if len(self.heap)==1 :
            return self.heap.pop()
        minElement = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return minElement


    def heapify_down(self, index):
        smallest = index
        left_child = 2*index + 1
        right_child = 2*index + 2
        if left_child < len(self.heap)  and self.heap[left_child] < self.heap[smallest] :
            smallest = left_child
        
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index :
            self.heap[index] , self.heap[smallest] = self.heap[smallest] , self.heap[index]
            self.heapify_down(smallest)

    def get_min(self):  #git the minimum value without removing it 
        if len(self.heap) == 0:
            return
        return self.heap[0]


    def display(self): #return the list 
        return self.heap


    def display_tree(self, index=0, indent=""):
        if index < len(self.heap):
            print(indent + str(self.heap[index]))
            if 2 * index + 1 < len(self.heap):
                print(indent + "├── ", end="")
                self.display_tree(2 * index + 1, indent + "│   ")
            if 2 * index + 2 < len(self.heap):
                print(indent + "└── ", end="")
                self.display_tree(2 * index + 2, indent + "    ")


MinHeap = min_heap()
MinHeap.insert(10)
print(MinHeap.display()) # Output: [10]
MinHeap.insert(5)
print(MinHeap.display())# Output: [5,10]
MinHeap.insert(3)
print(MinHeap.display())# Output: [3,10,5]
MinHeap.insert(2)
print(MinHeap.display())# Output: [2,3,5,10]
MinHeap.insert(7)
print(MinHeap.display())# Output: [2, 3, 5, 10, 7]
MinHeap.display_tree()
print(MinHeap.get_min())  # Output: 2
print(MinHeap.extract_min())  # Output: 2
print(MinHeap.display()) # Output: [3, 7, 5, 10]
MinHeap.insert(100)
MinHeap.insert(11)
print(MinHeap.display())#Output: [3, 7, 5, 10,100,11]
MinHeap.insert(22)
print(MinHeap.display())#[3,7,5,10,100,11,22]
MinHeap.insert(3)
print(MinHeap.display())#[3,3,5,7,100,11,22,10]
MinHeap.insert(6)
print(MinHeap.display())#3,3,5,6,100,11,22,10,7
MinHeap.insert(70)
print(MinHeap.display())#3,3,5,6,70,11,22,10,7,100
MinHeap.insert(1)
print(MinHeap.display())#[1, 3, 5, 6, 3, 11, 22, 10, 7, 100, 70]
MinHeap.insert(8)
print(MinHeap.display())#[1, 3, 5, 6, 3, 8, 22, 10, 7, 100, 70, 11]
MinHeap.insert(9)
print(MinHeap.display())#[1, 3, 5, 6, 3, 8, 22, 10, 7, 100, 70, 11, 9]
MinHeap.insert(10)
print(MinHeap.display())#[1, 3, 5, 6, 3, 8, 10, 10, 7, 100, 70, 11, 9, 22]
MinHeap.insert(11)
print(MinHeap.display())#[1, 3, 5, 6, 3, 8, 10, 10, 7, 100, 70, 11, 9, 22, 11]
MinHeap.display_tree()