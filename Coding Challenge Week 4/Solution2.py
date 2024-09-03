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

    def delete_middle(self):
        # If linked list is empty or has only one node
        if self.head is None or self.head.next is None:
            self.head = None
            return

        # Initialize slow and fast pointers
        slow = self.head
        fast = self.head
        prev = None

        # Move fast by two and slow by one step
        # When fast reaches the end, slow will be at the middle
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # Delete the middle node
        if prev:
            prev.next = slow.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Example 1: 1->2->3->4->5->NULL
llist1 = LinkedList()
llist1.append(1)
llist1.append(2)
llist1.append(3)
llist1.append(4)
llist1.append(5)
llist1.delete_middle()
llist1.print_list()  # Output: 1 2 4 5

# Example 2: 2->4->6->7->5->1->NULL
llist2 = LinkedList()
llist2.append(2)
llist2.append(4)
llist2.append(6)
llist2.append(7)
llist2.append(5)
llist2.append(1)
llist2.delete_middle()
llist2.print_list()  # Output: 2 4 6 5 1
