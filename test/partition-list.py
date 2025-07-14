class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

        
    def partition_list(self, x):
        #   +===================================================+
        #   |               WRITE YOUR CODE HERE                |
        #   | Description:                                      |
        #   | - Partitions a doubly linked list around a value  |
        #   |   `x`.                                            |
        #   | - All nodes with values less than `x` come before |
        #   |   nodes with values greater than or equal to `x`. |
        #   |                                                   |
        #   | Behavior:                                         |
        #   | - Uses two dummy nodes to create two sublists:    |
        #   |   one for nodes < x, and one for nodes >= x.      |
        #   | - Each node is added to the appropriate sublist   |
        #   |   while maintaining both next and prev pointers.  |
        #   | - The sublists are then joined together.          |
        #   | - The head of the list is updated to the start of |
        #   |   the merged result.                              |
        #   +===================================================+
        if self.length == 0 or self.length == 1:
            return

        small_dummy = Node(0)
        large_dummy = Node(0)
        small_tail = small_dummy
        large_tail = large_dummy
        current = self.head
        while current:
            next_node = current.next  # Store next node
            current.prev = current.next = None  # Detach current node
            if current.value < x:
                small_tail.next = current
                current.prev = small_tail
                small_tail = current
            else:
                large_tail.next = current
                current.prev = large_tail
                large_tail = current
            current = next_node
        # Merge the two lists
        if small_dummy.next:
            self.head = small_dummy.next
            small_tail.next = large_dummy.next
            if large_dummy.next:
                large_dummy.next.prev = small_tail
        else:
            self.head = large_dummy.next
        # Clean up dummy nodes
        small_dummy.next = large_dummy.next = None
        large_dummy.prev = small_tail = None
        # Ensure the new head's prev is None
        if self.head:
            self.head.prev = None
        return  

        '''dummy = DoublyLinkedList(0)
        cur = self.head
        large_counter = 0

        while cur:
            if cur.value >= x:
                if not cur.prev:
                    if self.length == 1:
                        return
                    cur.next.prev = None
                    self.head = cur.next
                    cur = cur.next
                    dummy.append(cur)
                    large_counter += 1
                    self.length -= 1
                    continue
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                dummy.append(cur)
                large_counter += 1
                self.length -= 1
            if cur.next is None:
                tail = cur
            cur = cur.next
            


        if dummy.length <= 1:
            return
        else:
            if large_counter == self.length:
                self.head = dummy.head.next
                self.head.prev = None
                dummy.head.next = None
                return
            tail.next = dummy.head.next
            dummy.head.next.prev = tail
            dummy.tail = None'''


# -------------------------------
# Test Cases:
# -------------------------------

print("\nTest Case 1: Partition around 5")
dll1 = DoublyLinkedList(3)
dll1.append(8)
dll1.append(5)
dll1.append(10)
dll1.append(2)
dll1.append(1)
print("BEFORE: ", end="")
dll1.print_list()
dll1.partition_list(5)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest Case 2: All nodes less than x")
dll2 = DoublyLinkedList(1)
dll2.append(2)
dll2.append(3)
print("BEFORE: ", end="")
dll2.print_list()
dll2.partition_list(5)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest Case 3: All nodes greater than x")
dll3 = DoublyLinkedList(6)
dll3.append(7)
dll3.append(8)
print("BEFORE: ", end="")
dll3.print_list()
dll3.partition_list(5)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest Case 4: Empty list")
dll4 = DoublyLinkedList(1)
dll4.make_empty()
print("BEFORE: ", end="")
dll4.print_list()
dll4.partition_list(5)
print("AFTER:  ", end="")
dll4.print_list()

print("\nTest Case 5: Single node")
dll5 = DoublyLinkedList(1)
print("BEFORE: ", end="")
dll5.print_list()
dll5.partition_list(5)
print("AFTER:  ", end="")
dll5.print_list()

