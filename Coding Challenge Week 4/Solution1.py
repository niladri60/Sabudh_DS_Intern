# Print the Middle of a given linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_middle(self):
        slow = self.head
        fast = self.head

        # Move fast by two and slow by one
        # When fast reaches end, slow will reach middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print("The middle element is:", slow.data)


# TestCase 1: 2->3->4->5->NULL
llist1 = LinkedList()
llist1.append(2)
llist1.append(3)
llist1.append(4)
llist1.append(5)
llist1.print_middle()  # Output: The middle element is: 4

# TestCase 2: 1->2->3->4->5->NULL
llist2 = LinkedList()
llist2.append(1)
llist2.append(2)
llist2.append(3)
llist2.append(4)
llist2.append(5)
llist2.print_middle()  # Output: The middle element is: 3
