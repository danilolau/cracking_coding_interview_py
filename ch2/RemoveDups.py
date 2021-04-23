from linkedlist import LinkedList, DoublyLinkedList, Node

def remove_dubs(ll):
    
    pointer = ll.head
    uniques = set()
    
    while(pointer is not None):
        if pointer.value in uniques:
            removed = pointer
            pointer = pointer.next
            ll.remove_by_ref(removed)
        else:
            uniques.add(pointer.value)
            pointer = pointer.next
            
ll = DoublyLinkedList(Node(5))

items = [2,3,4,5,6,5,3,2,3,5,4,3,2,6,7,8,10,1,1,1]

ll.append_list_to_tail(items)
    
print(ll)

remove_dubs(ll)

print(ll)