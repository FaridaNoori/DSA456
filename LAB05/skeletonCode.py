from typing import Any, Optional, List

class Node:
    def __init__(self, data: Any, next_node=None):
        self.data = data
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        # Optional: keep track of size for O(1) size() method
        self._size = 0

    def is_empty(self) -> bool:
        return self.head is None

    def prepend(self, data: Any) -> None:
        """Insert at the beginning – O(1)"""
        new_node = Node(data, self.head)
        self.head = new_node
        self._size += 1

    def append(self, data: Any) -> None:
        """Insert at the end – O(n) without tail pointer"""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        
        self._size += 1

    def insert_after(self, target: Node, data: Any) -> None:
        """Insert after the given target node – O(1) if target is known"""
        if target is None:
            raise ValueError("Target node cannot be None")
        
        # We don't check if target actually belongs to this list 
        # (would require O(n) traversal) – assuming correct usage
        new_node = Node(data, target.next)
        target.next = new_node
        self._size += 1

    def delete(self, target: Node) -> bool:
        """Delete the given target node – O(n) because we need to find predecessor"""
        if self.is_empty() or target is None:
            return False

        # Special case: deleting head
        if target == self.head:
            self.head = self.head.next
            self._size -= 1
            return True

        # Find predecessor
        current = self.head
        while current is not None and current.next != target:
            current = current.next

        if current is None:
            # target not found in list
            return False

        # current.next == target → unlink it
        current.next = target.next
        self._size -= 1
        return True

    def search(self, data: Any) -> Optional[Node]:
        """Find first node with given data – O(n)"""
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def size(self) -> int:
        """O(1) using cached count"""
        return self._size

    def to_list(self) -> List[Any]:
        """Convert to Python list – O(n)"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def print(self) -> None:
        """Print all elements nicely"""
        if self.is_empty():
            print("List is empty")
            return
        
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        
        print(" → ".join(elements))


"""
Big-O Analysis (PART B):

Method,     Time Complexity,    Explanation,                                                    Space Complexity
__init__,       O(1),           Just setting head to None and size to 0,                            O(1)
is_empty,       O(1),           Check if head is None,                                              O(1)
prepend,        O(1),           "New node points to current head, update head",                     O(1)
append,         O(n),           Must traverse to the end (no tail pointer),                         O(1)
insert_after,   O(1),           Given the target node → just update pointers,                       O(1)
delete,         O(n),           Must find predecessor of target (worst case traverse whole list),   O(1)
search,         O(n),           Linear scan in worst case (and average case),                       O(1)
size,           O(1),           Using cached counter (most efficient approach),                     O(1)
to_list,        O(n),           Must visit every node once,                                         O(n)
print,          O(n),           Must visit every node to build string or print,                     O(n)
"""