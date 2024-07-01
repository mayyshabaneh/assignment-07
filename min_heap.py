class  MinHeap:
    def __init__(self) -> None:
        self.heap = []  #initialize an empty array as a heap


    def insert(self, value):  #insert values to heap at the end of array then check the heap propertiy by calling heapify up 
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)


    def heapify_up(self,value): 
        parent = (value-1)//2 
        if value > 0 and self.heap[value] < self.heap[parent]:
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

#git this code to check correctness
    def display_tree(self, index=0, indent=""):
        if index < len(self.heap):
            print(indent + str(self.heap[index]))
            if 2 * index + 1 < len(self.heap):
                print(indent + "├── ", end="")
                self.display_tree(2 * index + 1, indent + "│   ")
            if 2 * index + 2 < len(self.heap):
                print(indent + "└── ", end="")
                self.display_tree(2 * index + 2, indent + "    ")


min_heap = MinHeap()
print("test the insertion : ")
min_heap.insert(11)
min_heap.insert(200)
min_heap.insert(22)
min_heap.insert(44)
min_heap.insert(15)
min_heap.insert(54)
min_heap.insert(3)
min_heap.insert(2)
min_heap.insert(1)
min_heap.insert(7)
min_heap.insert(6)
min_heap.insert(555)
min_heap.insert(89)
print(min_heap.display())


min_heap.extract_min()
print("after extarction :" , min_heap.display())
min_heap.display_tree()


min_heap.get_min()
print("get min :" , min_heap.display())
