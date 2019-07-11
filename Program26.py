#Python Program for Reversing of linked list nodes...
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
    
    def ReverseNodes(self):
        prev = None
        curr=self.head
        nxt = curr.next_node
        while(curr):
            curr.next_node=prev
            prev=curr
            curr=nxt
            if nxt:
                nxt=nxt.next_node
        
        self.head=prev
            
ll1=LinkedList()
ll1.insert(8)
ll1.insert(7)
ll1.insert(6)
ll1.insert(5)
ll1.insert(9)
ll1.insert(10)
ll1.PrintList()
ll1.ReverseNodes()
print("\nAfter reversing nodes are: ")
ll1.PrintList()
