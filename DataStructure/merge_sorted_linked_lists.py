def main():
    list1 = Node(1)
    list1.insert_last(Node(2))
    list1.insert_last(Node(4))

    list2 = Node(1)
    list2.insert_last(Node(3))
    list2.insert_last(Node(4))

    print(merge_sorted_lists(list1, list2))

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
    
    def insert_last(self, node):
        if self.next is None:
            self.next = node
        else:
            ptr = self
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = node

    def __repr__(self):
        ptr = self
        list_str = ''
        
        while ptr is not None:
            list_str += str(ptr.value) + ' '
            ptr = ptr.next

        return list_str

def merge_sorted_lists(head1, head2):
    ptr1 = head1
    ptr2 = head2

    merged_list = None

    while ptr1 is not None or ptr2 is not None:
        if ptr1 is None:
            new_ptr.next = ptr2
            break
        elif ptr2 is None:
            new_ptr.next = ptr1
            break
        
        min_value = min(ptr1.value, ptr2.value)

        if merged_list is None:
            merged_list = Node(min_value)
            new_ptr = merged_list
        else:
            new_ptr.next = Node(min_value)
            new_ptr = new_ptr.next

        if (min_value == ptr1.value and min_value == ptr2.value) or min_value == ptr1.value:
            ptr1 = ptr1.next
        else:
            ptr2 = ptr2.next
    
    return merged_list

if __name__ == '__main__':
    main()
