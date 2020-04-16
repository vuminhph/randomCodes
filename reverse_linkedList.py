
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def add_node(self, value):
        ptr = self.head

        while ptr.next != None:
            ptr = ptr.next
        ptr.next = Node(value)

    def print_list(self):
        ptr = self.head
        
        while ptr != None:
            print(ptr.value)
            ptr = ptr.next

def ll_reversed(linked_list):
    ptr = linked_list.head
    next_ptr = ptr.next
    linked_list.head.next = None

    while next_ptr != None:
        ptr1 = ptr
        ptr2 = next_ptr
        next_ptr = next_ptr.next
        
        ptr2.next = ptr1
        ptr = ptr2

    linked_list.head = ptr

linked_list = LinkedList(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(4)
linked_list.add_node(5)
linked_list.add_node(6)

linked_list.print_list()

ll_reversed(linked_list)