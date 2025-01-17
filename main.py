# DO NOT MODIFY THE NODE CLASS
class Node:
    def __init__(self, value, next=None):
        self.value = value 
        # if next is None, this is the last element in the list
        self.next = next 

def is_palindrome(head):
    vals = []  # create an empty Python list to put the values into
    current = head  # current is the node we're currently looking at

    while current is not None:  # while we've not reached the end of the list
        # take the current value from the node and add it to our Python list
        vals.append(current.value)
        # move to the next node
        current = current.next

    # check whether the Python list is the same forwards and backwards
    return vals == list(reversed(vals))


# 5->4->2
list_1 = Node(5, Node(4, Node(2)))
assert not is_palindrome(list_1)

# 5->4->5
list_2 = Node(5, Node(4, Node(5)))
assert is_palindrome(list_2)

# a->b->c->c->b->a
list_3 = Node("a", Node("b", Node("c", Node("c", Node("b", Node("a"))))))
assert is_palindrome(list_3)

# a->b->c->E->b->a
list_4 = Node("a", Node("b", Node("c", Node("E", Node("b", Node("a"))))))
assert not is_palindrome(list_4)

# 3->3
list_5 = Node(3, Node(3))
assert is_palindrome(list_5)

# 5 (only one element in list)
list_6 = Node(5)
assert is_palindrome(list_6)

# (empty list)
list_7 = None
assert is_palindrome(list_7)

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
