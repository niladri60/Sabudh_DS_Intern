# Find the second last element from the linked list 
# Input : List = 2 -> 4 -> 6 -> 8 -> 33 -> 67 -> NULL
# Output : 33 
# Input : List = 1 -> 2 -> 3 -> 4 -> 5 -> NULL
# Output : 4

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

    def find_second_last(self):
        if not self.head or not self.head.next:
            print("List is too short to have a second last element.")
            return None
        
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        
        return second_last.data

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")


# Example 1
llist1 = LinkedList()
llist1.append(2)
llist1.append(4)
llist1.append(6)
llist1.append(8)
llist1.append(33)
llist1.append(67)
print("List 1:")
llist1.print_list()  # Output: 2->4->6->8->33->67->NULL
print("Second last element:", llist1.find_second_last())  # Output: 33

# Example 2
llist2 = LinkedList()
llist2.append(1)
llist2.append(2)
llist2.append(3)
llist2.append(4)
llist2.append(5)
print("List 2:")
llist2.print_list()  # Output: 1->2->3->4->5->NULL
print("Second last element:", llist2.find_second_last())  # Output: 4
