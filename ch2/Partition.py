from structs.linkedlist import Node, LinkedList

def partition(k,ll):
    rll = LinkedList()
    lll = LinkedList()
    pll = LinkedList()
    pointer = ll.head
    while pointer is not None:
        if pointer.value < k:
            lll.append_to_tail(pointer)
        else:
            rll.append_to_tail(pointer)
        pointer = pointer.next
        
    lll.tail.next = rll.head
    pll.head = lll.head
    pll.tail = rll.tail
    pll.tail.next = None
    
    return pll

input = [3,5,8,5,10,2,1,3,4,0,12,10,9,8,7,6,18,20]
ll = LinkedList()
ll.append_list_to_tail(input)
print(ll)
p = partition(10,ll)
print(p)
