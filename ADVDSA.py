# ASSIGNMENT 1
# 1. Delete the elements in an linked list whose sum is equal to zero
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def delete_zero_sum(head):
    # Calculate cumulative sum and store in a hash table
    cumulative_sum = 0
    sum_map = {}
    curr = head

    while curr:
        cumulative_sum += curr.data

        if cumulative_sum == 0:
            # If cumulative sum is zero, set head to the next node
            head = curr.next
        elif cumulative_sum in sum_map:
            # If cumulative sum already exists in the hash table,
            # skip the nodes in between and update "next" pointers
            sum_node = sum_map[cumulative_sum]
            sum_node.next = curr.next
        else:
            sum_map[cumulative_sum] = curr

        curr = curr.next

    return head

def display_linked_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

# Create a linked list manually for testing
head = Node(3)
node1 = Node(4)
node2 = Node(-7)
node3 = Node(2)
node4 = Node(-5)
node5 = Node(1)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original Linked List:")
display_linked_list(head)

head = delete_zero_sum(head)
print("Linked List after deleting elements with zero sum:")
display_linked_list(head)






# 2.Reverse a linked list in groups of given size
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseLinkedList(head, k):
    if not head:
        return None

    prev = None
    curr = head
    next = None
    count = 0

    # Reverse the group of k nodes
    while curr is not None and count < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1

    # Recursively call for the remaining nodes
    if next is not None:
        head.next = reverseLinkedList(next, k)

    return prev


def printLinkedList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> None
head = Node(1)
current = head
for i in range(2, 9):
    newNode = Node(i)
    current.next = newNode
    current = current.next

print("Original Linked List:")
printLinkedList(head)

k = 3
head = reverseLinkedList(head, k)

print("Reversed Linked List in groups of", k)
printLinkedList(head)


# 3.Merge a linked list into another linked list at alternate positions
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def mergeLinkedLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    curr1 = list1
    next1 = curr1.next
    curr2 = list2

    while curr1 is not None and curr2 is not None:
        next1 = curr1.next
        curr1.next = curr2
        curr2 = curr2.next
        curr1.next.next = next1
        curr1 = next1

    if curr2 is not None:
        curr1.next = curr2

    return list1


def printLinkedList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


# Example usage
# Create the first linked list: 1 -> 2 -> 3 -> None
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)

# Create the second linked list: 4 -> 5 -> 6 -> 7 -> 8 -> None
list2 = Node(4)
list2.next = Node(5)
list2.next.next = Node(6)
list2.next.next.next = Node(7)
list2.next.next.next.next = Node(8)

print("List 1:")
printLinkedList(list1)

print("List 2:")
printLinkedList(list2)

merged_list = mergeLinkedLists(list1, list2)

print("Merged Linked List:")
printLinkedList(merged_list)


# 4.In an array, Count Pairs with given sum
def countPairsWithSum(arr, target):
    counter = {}
    pairCount = 0

    for num in arr:
        diff = target - num
        if diff in counter:
            pairCount += counter[diff]
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    return pairCount


# Example usage
arr = [1, 5, 7, -1, 5]
target = 6

pairCount = countPairsWithSum(arr, target)

print("Number of pairs with sum", target, "in the array:", pairCount)


# 5. Find duplicates in an array
def findDuplicates(arr):
    seen = set()
    duplicates = []

    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates


# Example usage
arr = [1, 2, 3, 4, 2, 5, 6, 3, 4]
duplicates = findDuplicates(arr)

print("Duplicate elements in the array:", duplicates)






# 6.Find the Kth largest and Kth smallest number in an array

def findKthLargestAndSmallest(arr, K):
    arr.sort()
    kth_smallest = arr[K - 1]
    kth_largest = arr[len(arr) - K]
    return kth_smallest, kth_largest


# Example usage
arr = [9, 4, 7, 1, 5, 2, 8, 3, 6]
K = 3
kth_smallest, kth_largest = findKthLargestAndSmallest(arr, K)

print("Kth Smallest Number:", kth_smallest)
print("Kth Largest Number:", kth_largest)


# 7.Move all the negative elements to one side of the array
import heapq


def findKthLargestAndSmallest(arr, K):
    min_heap = []

    for num in arr:
        if len(min_heap) < K:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

    kth_smallest = min_heap[0]
    kth_largest = heapq.nlargest(K, arr)[-1]

    return kth_smallest, kth_largest


# Example usage
arr = [9, 4, 7, 1, 5, 2, 8, 3, 6]
K = 3
kth_smallest, kth_largest = findKthLargestAndSmallest(arr, K)

print("Kth Smallest Number:", kth_smallest)
print("Kth Largest Number:", kth_largest)


# 8.Reverse a string using a stack data structure
def reverseString(input_str):
    stack = []
    reversed_str = ""

    # Push characters onto the stack
    for char in input_str:
        stack.append(char)

    # Pop characters from the stack to reverse the string
    while len(stack) > 0:
        reversed_str += stack.pop()

    return reversed_str


# Example usage
input_str = "Hello, World!"
reversed_str = reverseString(input_str)

print("Input String:", input_str)
print("Reversed String:", reversed_str)




# 9. Evaluate a postfix expression using stack
def evaluatePostfix(expression):
    stack = []

    # Iterate through each character in the expression
    for char in expression:
        if char.isdigit():
            # If the character is a digit, convert it to an integer and push it onto the stack
            stack.append(int(char))
        else:
            # If the character is an operator, pop the top two operands from the stack and apply the operator
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == "+":
                result = operand1 + operand2
            elif char == "-":
                result = operand1 - operand2
            elif char == "*":
                result = operand1 * operand2
            elif char == "/":
                result = operand1 / operand2

            # Push the result back onto the stack
            stack.append(result)

    # The final result will be left on the stack
    return stack.pop()


# Example usage
expression = "6523+8*+3+*"
result = evaluatePostfix(expression)

print("Postfix Expression:", expression)
print("Result:", result)



# 10.Implement a queue using the stack data structure
class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        # Push the item onto the enqueue stack
        self.enqueue_stack.append(item)

    def dequeue(self):
        # If the dequeue stack is empty, transfer elements from enqueue stack to dequeue stack
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        # Pop the element from the dequeue stack
        if self.dequeue_stack:
            return self.dequeue_stack.pop()
        else:
            # If both stacks are empty, the queue is empty
            return None

    def is_empty(self):
        # The queue is empty if both stacks are empty
        return len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0

    def size(self):
        # The size of the queue is the sum of the sizes of both stacks
        return len(self.enqueue_stack) + len(self.dequeue_stack)
# Create a new queue
queue = Queue()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue elements
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

# Check if the queue is empty
print(queue.is_empty())  # Output: False

# Get the size of the queue
print(queue.size())  # Output: 1


