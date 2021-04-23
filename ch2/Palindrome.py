from linkedlist import Node, DoublyLinkedList

def palindrome(ll=DoublyLinkedList()):

    p1 = ll.head
    p2 = ll.tail
    is_palindrome = True

    while p1 !=p2 and p1.prev != p2 and is_palindrome:
        if p1.value != p2.value:
            is_palindrome = False
        p1 = p1.next
        p2 = p2.prev

    return is_palindrome

ll = DoublyLinkedList()
ll.append_list_to_tail(['a','b','c','b','a'])
print(palindrome(ll))