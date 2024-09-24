# Maximum Twin Sum of A Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add elements to the list
    def append(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Function to calculate the maximum twin sum
    def max_twin_sum(self):
        values = []
        current = self.head
        # Store all values of the linked list in a list
        while current:
            values.append(current.data)
            current = current.next
        
        # Initialize the maximum sum
        max_sum = 0
        n = len(values)
        
        # Calculate twin sum for each pair of equidistant nodes
        for i in range(n // 2):
            twin_sum = values[i] + values[n - 1 - i]
            max_sum = max(max_sum, twin_sum)
        
        return max_sum

# Helper function to print the list (for testing purposes)
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next

# Test case 1
llist1 = LinkedList()
llist1.append(5)
llist1.append(4)
llist1.append(2)
llist1.append(1)
print("Test Case 1: Linked List")
print_list(llist1.head)
print("Maximum Twin Sum:", llist1.max_twin_sum())  # Output: 6

# Test case 2
llist2 = LinkedList()
llist2.append(4)
llist2.append(2)
llist2.append(2)
llist2.append(3)
print("Test Case 2: Linked List")
print_list(llist2.head)
print("Maximum Twin Sum:", llist2.max_twin_sum())  # Output: 7


# Output
# Test Case 1: Linked List
# 5 -> 4 -> 2 -> 1
# Maximum Twin Sum: 6
# Test Case 2: Linked List
# 4 -> 2 -> 2 -> 3
# Maximum Twin Sum: 7