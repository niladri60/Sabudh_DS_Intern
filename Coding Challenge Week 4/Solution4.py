# Reverse a Linked List 
# Given a pointer to the head node of a linked list, the task is to reverse the linked list. We need to reverse the list by changing the links between nodes. 

# Examples: 
# Input: Head of following linked list 
# 1->2->3->4->NULL

# Output: Linked list should be changed to, 
# 4->3->2->1->NULL 

# Input: Head of following linked list 
# 1->2->3->4->5->NULL 

# Output: Linked list should be changed to, 
# 5->4->3->2->1->NULL 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev to current
            current = next_node       # Move current to next node

        self.head = prev  # Update the head to the new front

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")


# Example 1: 1->2->3->4->NULL
llist1 = LinkedList()
llist1.append(1)
llist1.append(2)
llist1.append(3)
llist1.append(4)
print("Original Linked List:")
llist1.print_list()
llist1.reverse()
print("Reversed Linked List:")
llist1.print_list()  # Output: 4->3->2->1->NULL

# Example 2: 1->2->3->4->5->NULL
llist2 = LinkedList()
llist2.append(1)
llist2.append(2)
llist2.append(3)
llist2.append(4)
llist2.append(5)
print("Original Linked List:")
llist2.print_list()
llist2.reverse()
print("Reversed Linked List:")
llist2.print_list()  # Output: 5->4->3->2->1->NULL
