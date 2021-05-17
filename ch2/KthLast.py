from structs.linkedlist import Node, LinkedList

def kth_last(k,ll):
    pointer = ll.head
    kth = ll.head
    for _ in range(k):
        try:
            pointer = pointer.next
        except:
            break
        
    while pointer!=ll.tail:
        pointer = pointer.next
        kth = kth.next
        
    return kth

ll = LinkedList(Node(1))
items = [2,3,4,5,6,5,3,2,3,5,4,3,2,6,7,8,10,1]
ll.append_list_to_tail(items)

print(ll)
print(kth_last(0,ll))
