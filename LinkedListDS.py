
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        curr = self.head

        while curr.next:
            curr = curr.next
        curr.next = new_node


datas = [1,2,3,4,5,6,7]

node_instance = Node(data=datas)
obj = LinkedList()

obj.append(data=datas)