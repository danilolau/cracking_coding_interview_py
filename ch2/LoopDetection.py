from structs.linkedlist import Node, LinkedList
import random

def gen_loop(ll=LinkedList()):
    length = 0
    p = ll.head
    while p is not None:
        length += 1
        p = p.next
    rand = random.choice(range(length))
    p = ll.head
    for _ in range(rand):
        p = p.next
    
    ll.tail.next = p
    
def loop_detection(ll=LinkedList()):
    p = ll.head
    nodes = set()
    is_loop = False
    while p is not None:
        if(p in nodes):
            is_loop = True
            break
        nodes.add(p)
        p = p.next
    return is_loop

ll = LinkedList()
ll.append_list_to_tail([2,3,6,4,2,6,8,2,10])
print(loop_detection(ll))
gen_loop(ll)
print(loop_detection(ll))

        
        