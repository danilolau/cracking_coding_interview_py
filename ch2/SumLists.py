from linkedlist import Node, LinkedList

def sum_lists(fll,sll):
    result = LinkedList()
    first = fll.head
    second = sll.head
    rest = 0
    while first is not None and second is not None:
        value, rest = sum_place(first.value,second.value,rest)
        result.append_to_tail(Node(value))
        first = first.next
        second = second.next
        
    while first is not None:
        value, rest = sum_place(first.value,0,rest)
        result.append_to_tail(Node(value))
        first = first.next
        
    while second is not None:
        value, rest = sum_place(0,second.value,rest)
        result.append_to_tail(Node(value))
        second = second.next
        
    if rest > 0:
        result.append_to_tail(rest)
        
    return result
        
def sum_place(val1,val2,rest):
    sump = val1 + val2 + rest
    rest = int(sump/10)
    value = sump%10
    return value, rest

first = LinkedList()
second = LinkedList()
first.append_list_to_tail([7,1,6])
second.append_list_to_tail([5,9,2])
result = sum_lists(first,second)
print(result)
print(617 + 295)
    