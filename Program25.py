#Python Program for Find middle element in Linked list...


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList(object):
    
    def __init__(self):
        self.head = None
    
    def insert(self,new_data):  #insert at the start of linked list
        new_node = Node(new_data)
        new_node.next_node=self.head
        self.head=new_node
    
    def PrintList(self):
        tempnode = self.head
        while(tempnode):
            print("{}".format(tempnode.data),end = '-->')
            tempnode = tempnode.next_node
    
    def FindMiddleElement(self):
        count = 0
        temp = self.head
        while(temp):
            count+=1
            temp=temp.next_node
        temp = self.head
        for i in range(0,count//2):
            temp=temp.next_node
        return temp
            
ll1=LinkedList()
ll1.insert(8)
ll1.insert(7)
ll1.insert(6)
ll1.insert(5)
ll1.insert(9)
ll1.insert(10)
ll1.PrintList()
temp = ll1.FindMiddleElement()
print("middle element is ",temp.data)
