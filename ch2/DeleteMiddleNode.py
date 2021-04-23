from linkedlist import LinkedList, Node

def delete_middle_node(ll):
    middle = ll.head
    pointer = ll.head
    
    while pointer != ll.tail:
        pointer = pointer.next.next
        if pointer is None:
            break
        if pointer != ll.tail:
            middle = middle.next

        
    middle.next = middle.next.next

ll = LinkedList(Node(1))
items = [2,3,4,5]
ll.append_list_to_tail(items)
print(ll)
delete_middle_node(ll)
print(ll)