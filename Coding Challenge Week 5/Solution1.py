# Inserting at the Beginning
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def insert_at_beginning(self, new_data):
        # Allocate the Node and put in the data
        new_node = Node(new_data)
        # Make next of new Node as head
        new_node.next = self.head
        # Move the head to point to new Node
        self.head = new_node

    # Function to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="->" if current.next else "\n")
            current = current.next

# Test case 1
llist1 = LinkedList()
llist1.insert_at_beginning(5)
llist1.insert_at_beginning(4)
llist1.insert_at_beginning(3)
llist1.insert_at_beginning(2)
print("Test Case 1: Before insertion")
llist1.print_list()

llist1.insert_at_beginning(1)
print("Test Case 1: After insertion")
llist1.print_list()

# Test case 2
llist2 = LinkedList()
llist2.insert_at_beginning(2)
llist2.insert_at_beginning(1)
llist2.insert_at_beginning(7)
llist2.insert_at_beginning(5)
llist2.insert_at_beginning(2)
llist2.insert_at_beginning(3)
print("Test Case 2: Before insertion")
llist2.print_list()

llist2.insert_at_beginning(9)
print("Test Case 2: After insertion")
llist2.print_list()


# Output
# Test Case 1: Before insertion
# 2->3->4->5
# Test Case 1: After insertion
# 1->2->3->4->5
# Test Case 2: Before insertion
# 3->2->5->7->1->2
# Test Case 2: After insertion
# 9->3->2->5->7->1->2