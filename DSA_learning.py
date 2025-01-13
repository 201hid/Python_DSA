class Node:
    def __init__(self, value):
        self.value= value
        self.next= None



class LinkedList:
    def __init__(self, value):
        new_node= Node(value)
        self.head= new_node
        self.tail= new_node
        self.length=1


    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next   


    def append(self, value):
        new_node= Node(value)
        if self.head is None:
            new_node=self.head 
            new_node=self.tail   
            self.length = 1
        else:    
            self.tail.next=new_node
            self.tail=new_node
        self.length = self.length + 1   
        return True

        
    def pop(self):
        if self.head is None:
            return None
        else: 
            pre = self.head
            temp = self.head
            while temp.next is not  None:
                pre= temp
                temp = temp.next 
            # print(pre.value)
            pre.next=None
            self.tail= pre
            self.length= -1     
            # print(temp.value)
            if self.length==0:
                self.head=None
                self.tail=None

    def prepend(self, value):
        new_node= Node(value)
        # when no element
        if self.length==0:
            self.head= new_node
            self.tail= new_node
        else:
            temp =self.head
            self.head= new_node
            self.head.next= temp    
        self.length= self.length +1
        return True


    def pop_first(self):
        if self.length==0:
            return None

        temp = self.head
        self.head=self.head.next
        temp.next=None
        self.length= self.length - 1
        if self.length==0:
            self.tail=None
        return temp


    def get(self, index):
        if self.length==0 or index>=self.length or index<0:
            return None
        else:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        return temp.value
                



    def get(self, index):
        if self.length==0 or index>=self.length or index<0:
            return None
        else:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        return temp
                
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value= value
            return True
        
    def insert(self, index, value):

        if index<0 or index>self.length:
            return False

        if index==0:
            self.prepend(value)
        if index==self.length:
            self.append(value)
        else:
            new_node=Node(value)
            for _ in range(index-1):
                temp=temp.next
            after=temp.next
            # print(after.value)
            temp.next=new_node
            new_node.next=after
            return True

    def remove(self, index):

        if index<0 or index>=self.length:
            return False

        if index==0:
            return self.pop_first()
        if index==self.length:
            return self.pop()
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            current=temp.next
            temp.next=temp.next.next
            self.length= self.length-1
            return current.value


    def reverse(self):
        temp= self.head
        self.head=self.tail
        self.tail=temp
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after



class DoublyLinkedList:

    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1


    def printlist(self):
        temp= self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self, value):
        new_Node=Node(value)
        if self.head is None:
            self.head=new_Node
            self.tail=new_Node
        else:
            new_Node.prev=self.tail
            self.tail.next=new_Node
            self.tail=new_Node
        self.length=self.length+1
        return True


    def Pop(self):
        if self.length==0:
            return None
        temp= self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:

            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
        self.length=self.length-1            
        return temp




    def Prepend(self, value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
        self.length=self.length+1            
        return True


    def PopFirst(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            temp.next=None
            self.head.prev=None
            temp.next

        self.length=self.length-1            
        return temp

    def Get(self, index):
        if index>=self.length or index<0:
            return None

        temp=self.head
        if index<self.length/2:
            for i in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for i in range(self.length-index-1):
                temp=temp.prev
        return temp


    def Set(self, index, value):
        
        temp=self.Get(index)
        if temp:
            temp.value=value
        return True


    def Insert(self, index, value):
        if index>self.length or index<0:
            return None

        if self.length==0:
            self.head=new_node
            self.tail=new_node
            return True
        
        if index==0:
            self.Prepend(value)
            return True

        if index==self.length:
            self.append(value)
            return True

        new_node=Node(value)
        current=self.Get(index)
        prev_node=current.prev
        prev_node.next=new_node
        new_node.prev=prev_node
        new_node.next=current
        current.prev=new_node
        self.length=self.length+1
        return True


    def Remove(self, index):
        if index>=self.length or index<0:
            return None

        if index==0:
            return self.PopFirst()
            
        if index==self.length-1:
            return self.Pop()
        current=self.Get(index)
        prev_node=current.prev
        next_node=current.next

        prev_node.next=next_node
        next_node.prev=prev_node
        current.next=None
        current.prev=None
        self.length=self.length-1

        return True

class Stack:
    def __init__(self, value):
        new_node=Node(value)
        self.top=new_node
        self.height=1


    def print_list(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def push(self, value):
        new_node=Node(value)
        if self.height==0:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height= self.height+1

    def pop(self):
        if self.height==0:
            return None
        temp=self.top
        self.top=self.top.next
        temp.next=None
        self.height=self.height-1
        return temp

class Queue:
    def __init__(self, value):
        new_node=Node(value)
        self.first=new_node
        self.end=new_node
        self.length=1
    
    def print_list(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
        
    def enqueue(self, value):
        new_node=Node(value)
        if self.length==0:
            self.first= new_node
            self.last= new_node
        else:
            self.end.next=new_node
            self.end=new_node
        self.length=self.length+1

    def dequeue(self):
        if self.length==0:
            return None
        temp=self.first
        if self.length==1:
            self.first=None
            self.end=None
        else:
            self.first=self.first.next
            temp.next=None
        return temp

            

        




        


# my_linked_list= DoublyLinkedList(5)      

# my_linked_list.append(32)
# my_linked_list.append(12)
# my_linked_list.append(4)
# my_linked_list.append(2)
# my_linked_list.Prepend(2)

#stack
# my_stack=Stack(3)
# print("printing stack")
# my_stack.print_list()
# print("printing stack after push ")
# my_stack.push(4)
# my_stack.push(2)
# my_stack.push(4)


# my_stack.print_list()
# print("printing stack after pop ")

# my_stack.pop()
# my_stack.print_list()

my_queue=Queue(5)
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.enqueue(8)

my_queue.print_list()

print("printing after 1st deque")
my_queue.dequeue()
my_queue.print_list()

print("printing after 2nd deque")

my_queue.dequeue()
my_queue.print_list()

print("printing after 3rd deque")

my_queue.dequeue()
my_queue.print_list()

print("printing after 4th deque")

my_queue.dequeue()
my_queue.print_list()
