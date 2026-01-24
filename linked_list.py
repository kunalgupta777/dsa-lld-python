from typing import Optional


class ListNode:
    def __init__(self, val = None) -> None:
        self.val = val
        self.next = None

def get_length(head: ListNode) -> int:
    cur_ptr = head
    length = 0
    while cur_ptr:
        length += 1
        cur_ptr = cur_ptr.next
    return length

def print_list(head_node: ListNode) -> None:
    curr_ptr = head_node
    while curr_ptr:
        if curr_ptr.next:
            print(str(curr_ptr.val) + "->", end="")
        else:
            print(str(curr_ptr.val))
        curr_ptr = curr_ptr.next

def find_element(head_node: ListNode, target: int) -> Optional[ListNode]:
    curr_node = head_node
    while curr_node:
        if curr_node.val == target:
            return curr_node
        curr_node = curr_node.next
    return None

def reverse_linked_list(head_node: ListNode) -> tuple[ListNode, ListNode]:
    prev, curr_node, next_node = None, head_node, head_node.next
    while next_node:
        curr_node.next = prev
        prev = curr_node
        curr_node = next_node
        next_node = next_node.next
    curr_node.next = prev
    return curr_node, head_node

if __name__ == "__main__":
    head_node = ListNode(val=1)
    curr_node = head_node
    for i in range(2, 11):
        new_node = ListNode(val=i)
        curr_node.next = new_node
        curr_node = new_node
    print_list(head_node=head_node)
    l = get_length(head=head_node)
    print("Length = " + str(l))

    node = find_element(head_node=head_node, target=11)
    if node:
        print("Element found", node.val)
    else:
        print("Element not found!")
    
    new_head, new_tail = reverse_linked_list(head_node=head_node)
    print("Reversed Linked List's Head and Tail are respectively: " + str(new_head.val) + ", " + str(new_tail.val))
    print_list(head_node=new_head)
    
