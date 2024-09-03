# Add two numbers represented by Linked List 
# Given two numbers represented by two lists, write a function that returns the sum in the form of a linked list. 

# Example: 
# Input: 
# List1: 5->6->3->NULL // represents number 563 
# List2: 8->4->2->NULL // represents number 842 

# Output: 
# Resultant list: 1->4->0->5->NULL // represents number 1405 

# Explanation: 563 + 842 = 1405 

# Input: 
# List1: 7->5->9->4->6->NULL // represents number 75946 
# List2: 8->4->NULL // represents number 84 

# Output: 
# Resultant list: 7->6->0->3->0->NULL // represents number 76030 

# Explanation: 75946+84=76030

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

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")


def add_two_lists(first: LinkedList, second: LinkedList) -> LinkedList:
    # Reverse both linked lists to start addition from the least significant digit
    first.reverse()
    second.reverse()

    # Create a new linked list for the result
    result = LinkedList()
    
    carry = 0
    f = first.head
    s = second.head

    # Traverse both lists
    while f is not None or s is not None:
        # Calculate the sum of corresponding nodes and carry
        sum_value = carry
        if f is not None:
            sum_value += f.data
            f = f.next
        if s is not None:
            sum_value += s.data
            s = s.next

        # Update carry for next calculation
        carry = sum_value // 10

        # Create a new node with the digit part of sum_value and append to result
        result.append(sum_value % 10)

    # If there is a carry left at the end, add a new node
    if carry > 0:
        result.append(carry)

    # Reverse the result list to get the correct order
    result.reverse()

    return result


# Example 1
list1 = LinkedList()
list1.append(5)
list1.append(6)
list1.append(3)

list2 = LinkedList()
list2.append(8)
list2.append(4)
list2.append(2)

print("List 1:")
list1.print_list()  # Output: 5->6->3->NULL

print("List 2:")
list2.print_list()  # Output: 8->4->2->NULL

result = add_two_lists(list1, list2)
print("Resultant List:")
result.print_list()  # Output: 1->4->0->5->NULL

# Example 2
list3 = LinkedList()
list3.append(7)
list3.append(5)
list3.append(9)
list3.append(4)
list3.append(6)

list4 = LinkedList()
list4.append(8)
list4.append(4)

print("List 3:")
list3.print_list()  # Output: 7->5->9->4->6->NULL

print("List 4:")
list4.print_list()  # Output: 8->4->NULL

result2 = add_two_lists(list3, list4)
print("Resultant List:")
result2.print_list()  # Output: 7->6->0->3->0->NULL
