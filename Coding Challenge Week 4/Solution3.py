# Remove duplicate elements from sorted linked list 
# Write a function that takes a list sorted in non-decreasing order and deletes any duplicate nodes from the list. The list should only be traversed once. 

# For example if the linked list is 11->11->11->21->43->43->60->NULL then removeDuplicates() should convert the list to 11->21->43->60->NULL. 

# Test Cases: 

# TestCase1: 
# Linked list: 11->11->11->13->13->20->NULL 
# Output: 11->13->20->NULL 

# TestCase2: 
# Linked list: 10->15->15->15->20->20->20->23->25->25->NULL 
# Output: 10->15->20->23->25->NULL 

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

    def remove_duplicates(self):
        current = self.head

        # Traverse the list till the last node
        while current and current.next:
            # If the current node's data is the same as the next node's data
            if current.data == current.next.data:
                # Skip the next node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")


# TestCase1: 11->11->11->13->13->20->NULL
llist1 = LinkedList()
llist1.append(11)
llist1.append(11)
llist1.append(11)
llist1.append(13)
llist1.append(13)
llist1.append(20)
llist1.remove_duplicates()
llist1.print_list()  # Output: 11->13->20->NULL

# TestCase2: 10->15->15->15->20->20->20->23->25->25->NULL
llist2 = LinkedList()
llist2.append(10)
llist2.append(15)
llist2.append(15)
llist2.append(15)
llist2.append(20)
llist2.append(20)
llist2.append(20)
llist2.append(23)
llist2.append(25)
llist2.append(25)
llist2.remove_duplicates()
llist2.print_list()  # Output: 10->15->20->23->25->NULL
