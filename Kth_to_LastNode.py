class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def Kth_to_LastNode(self,k):
        p=self.head
        q=self.head
        count=0
        while (q and count<k):
            q=q.next
            count+=1
        if not (q) and k>count:
            print(str(k)+' is greater than the number of nodes in the list')
            return
        while (p and q):
            p=p.next
            q=q.next
        return p.data
llist=LinkedList()
No_of_Input=int(input())
for i in range(No_of_Input):
    llist.insert(input())
k=int(input())
print(llist.Kth_to_LastNode(k))
