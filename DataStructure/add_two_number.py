class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __repr__(self):
        return str(self.val)

class LinkedList:
    def __init__(self, val):
        self.head = ListNode(val)

    def addToHead(self, val):
        new_head = ListNode(val)
        new_head.next = self.head
        self.head = new_head

def print_linkedList(head):
    ptr = head
    while True:
        if ptr.next is not None:
            print(ptr,end='-')
        else: 
            print(ptr)
            break
        ptr = ptr.next

def addTwoNumbers(l1, l2):
        ptr1 = l1
        ptr2 = l2
        big_ll = ptr1
        small_ll = ptr2
        while True:
            if ptr1 == None and ptr2 == None:
                break
            if ptr2 == None:
                break
            if ptr1 == None:
                small_ll = l1
                big_ll = l2
                break
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        counter = 0
        sum_ll = None
        sum_ptr = ListNode(-1)
        while small_ll is not None:
            sum_digit = small_ll.val + big_ll.val + counter
            if  sum_digit < 10:
                sum_ptr.next = ListNode(sum_digit)
                counter = 0
            else:
                sum_ptr.next = ListNode(sum_digit - 10)
                counter = 1
            if sum_ll is None:
                sum_ll = sum_ptr.next
            sum_ptr = sum_ptr.next
            small_ll = small_ll.next
            big_ll = big_ll.next
        while big_ll is not None:
            sum_digit = big_ll.val + counter
            if sum_digit < 10:
                sum_ptr.next = ListNode(sum_digit)
                counter = 0
            else:
                sum_ptr.next = ListNode(sum_digit - 10)
                counter = 1
            sum_ptr = sum_ptr.next
            big_ll = big_ll.next
        if counter != 0:
            sum_ptr.next = ListNode(counter)
        print_linkedList(sum_ll) 

l1 = LinkedList(3)
l1.addToHead(4)
l1.addToHead(2)

l2 = LinkedList(4)
l2.addToHead(6)
l2.addToHead(5)

addTwoNumbers(l1.head, l2.head)

