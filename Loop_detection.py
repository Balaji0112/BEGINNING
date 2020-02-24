class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def detect_loop(self):
        s=set()
        temp=self.head
        while(temp):
            if(temp in s):
                print(temp.data)
                return True
            s.add(temp)
            temp=temp.next
        return False
llist=LinkedList()
for i in [int(i) for i in input().split()]:
    llist.append(i)
llist.head.next.next.next.next=llist.head
if(llist.detect_loop()):
    print("Loop found")
else:
    print("No Loop")

            
        