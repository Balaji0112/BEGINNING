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
    def Remove_dups(self):
        cur= self.head
        prev=None
        dup_values=dict()
        while(cur):
            if cur.data in dup_values:
                prev.next=cur.next
                cur=None
            else:
                dup_values[cur.data]=1
                prev=cur
            cur=prev.next
    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next
llist=LinkedList()
no_of_input=int(input())
for i in range(no_of_input):
    llist.insert(input())
llist.Remove_dups()
llist.print_list()
