# Add 1 to a number which is represented as a linked list 
# A number is represented as a linked list such that each digit corresponds to a node in the linked list. Add 1 to the number and form a new linked list. For example 1999 is represented as (1-> 9-> 9 -> 9->NULL) and adding 1 to it should change it to (2->0->0->0->NULL) 

# TestCase 1: 
# Input: 1999 
# Output: 2000 

# TestCase 2: 
# Input: 3453 
# Output: 3454 


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
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def add_one(self):
        # Step 1: Reverse the linked list
        self.reverse()

        # Step 2: Add one to the reversed list
        current = self.head
        carry = 1

        while current:
            current.data += carry
            carry = current.data // 10
            current.data = current.data % 10
            prev = current
            current = current.next

        # Step 3: If there is still a carry after the last node, add a new node
        if carry:
            prev.next = Node(carry)

        # Step 4: Reverse the list again to restore original order
        self.reverse()

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")


# TestCase 1: Input: 1999 (1->9->9->9->NULL)
llist1 = LinkedList()
llist1.append(1)
llist1.append(9)
llist1.append(9)
llist1.append(9)
print("Original List:")
llist1.print_list()  # Output: 1->9->9->9->NULL
llist1.add_one()
print("List after adding 1:")
llist1.print_list()  # Output: 2->0->0->0->NULL

# TestCase 2: Input: 3453 (3->4->5->3->NULL)
llist2 = LinkedList()
llist2.append(3)
llist2.append(4)
llist2.append(5)
llist2.append(3)
print("Original List:")
llist2.print_list()  # Output: 3->4->5->3->NULL
llist2.add_one()
print("List after adding 1:")
llist2.print_list()  # Output: 3->4->5->4->NULL
