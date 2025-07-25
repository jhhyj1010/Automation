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

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.length += 1
        return True

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        #   +===================================================+
        #   |               WRITE YOUR CODE HERE                |
        #   | Description:                                      |
        #   | - Reverses a segment of a doubly linked list      |
        #   |   between the given start_index and end_index.    |
        #   | - This operation modifies only the segment in     |
        #   |   place, preserving the rest of the list.         |
        #   |                                                   |
        #   | Behavior:                                         |
        #   | - A dummy node is used to simplify edge cases     |
        #   |   like reversing from the head.                   |
        #   | - The `prev` pointer moves to the node before     |
        #   |   the reversal section.                           |
        #   | - The segment is reversed by removing nodes one   |
        #   |   at a time and reinserting them at the front of  |
        #   |   the sublist.                                    |
        #   | - All `next` and `prev` pointers are updated      |
        #   |   carefully to maintain list integrity.           |
        #   | - At the end, the new head is set properly and    |
        #   |   its prev pointer is cleared.                    |
        #   +===================================================+
        '''if start_index >= end_index or self.length:
            return
        
        if start_index < 0 or start_index >= self.length:
            return
        if end_index < 0 or end_index >= self.length:
            return
        
        start = self.head
        for _ in range(start_index):
            start = start.next
            
        before = start.prev
        
        for _ in range(end_index - start_index + 1):
            start.prev, start.next = start.next, start.prev
            start = start.prev
            
        after = start
        end = after.prev
        before.next = end
        end.prev = before
        start.next = after
        after.prev = start'''
        
        if start_index >= end_index or self.length == 0:
            return
        
        # Use dummy node to handle edge cases
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        
        prev = dummy
        for _ in range(start_index):
            if not prev.next:
                return self.head
            prev = prev.next
        
        # start node is the first node to be reversed    
        start_node = prev.next
        curr = start_node
        for _ in range(end_index - start_index):
            if not curr.next:
                break
            next_node = curr.next
            
            # Remove next_node from its current position
            curr.next = next_node.next
            if next_node.next:
                next_node.next.prev = curr
            
            # Insert next_node at the front of the sublist
            next_node.prev = prev
            next_node.next = prev.next
            prev.next.prev = next_node
            prev.next = next_node
            
        # Restore head and prev pointer
        self.head = dummy.next
        self.head.prev = None
        dummy.next = None
        return







# Test Cases
print("\nTest 1: Middle segment reversal")
dll1 = DoublyLinkedList(3)
for v in [8, 5, 10, 2, 1]:
    dll1.append(v)
print("BEFORE: ", end="")
dll1.print_list()
dll1.reverse_between(1, 4)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest 2: Full list reversal")
dll2 = DoublyLinkedList(1)
for v in [2, 3, 4, 5]:
    dll2.append(v)
print("BEFORE: ", end="")
dll2.print_list()
dll2.reverse_between(0, 4)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest 3: No-op on single node")
dll3 = DoublyLinkedList(9)
print("BEFORE: ", end="")
dll3.print_list()
dll3.reverse_between(0, 0)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest 4: Reversal with head involved")
dll4 = DoublyLinkedList(7)
for v in [8, 9]:
    dll4.append(v)
print("BEFORE: ", end="")
dll4.print_list()
dll4.reverse_between(0, 2)
print("AFTER:  ", end="")
dll4.print_list()

