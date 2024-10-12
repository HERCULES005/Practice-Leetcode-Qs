class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertion_at_begin(self,newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode

if __name__ == '__main__':
    pass