class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data


class LinkedList:
    def __init__(self, front=None, back=None) -> None:
        # Sentinel nodes (dummies) — standard for doubly-linked list
        self.front = Node() if front is None else front
        self.back = Node() if back is None else back
        self.front.next = self.back
        self.back.prev = self.front
        self._size = 0  # added for O(1) len()

    def show(self):
        """Helper to print the list (for testing)."""
        elements = []
        current = self.front.next
        while current != self.back:
            elements.append(str(current.get_data()))
            current = current.next
        print(" <-> ".join(elements) if elements else "Empty")

    def get_front(self):
        return self.front.next.get_data() if self.front.next != self.back else None

    def get_back(self):
        return self.back.prev.get_data() if self.back.prev != self.front else None

    def insert_front(self, data):
        """(Provided for completeness — not required for sorted behaviour)."""
        new_node = Node(data)
        new_node.next = self.front.next
        new_node.prev = self.front
        self.front.next.prev = new_node
        self.front.next = new_node
        self._size += 1

    def insert_back(self, data):
        """(Provided for completeness — not required for sorted behaviour)."""
        new_node = Node(data)
        new_node.prev = self.back.prev
        new_node.next = self.back
        self.back.prev.next = new_node
        self.back.prev = new_node
        self._size += 1

    def insert(self, data):
        """Inserts data so the list stays sorted (smallest → largest). Allows duplicates."""
        new_node = Node(data)
        current = self.front.next
        # Find first node >= data (or end)
        while current != self.back and current.data is not None and current.data < data:
            current = current.next
        # Splice in before current
        prev_node = current.prev
        new_node.prev = prev_node
        new_node.next = current
        prev_node.next = new_node
        current.prev = new_node
        self._size += 1

    def remove(self, data):
        """Removes ALL nodes containing data (spec says "nodes" plural). Returns True if any removed."""
        current = self.front.next
        found = False
        while current != self.back:
            if current.data == data:
                prev_node = current.prev
                next_node = current.next
                prev_node.next = next_node
                next_node.prev = prev_node
                found = True
                self._size -= 1
                current = next_node  # continue (removes duplicates too)
            else:
                current = current.next
        return found

    def is_present(self, data):
        """Returns True if data exists in the list."""
        current = self.front.next
        while current != self.back:
            if current.data == data:
                return True
            current = current.next
        return False

    def __len__(self):
        """Returns number of values stored."""
        return self._size


# Testing main (not marked — run to verify)
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10)
    ll.insert(5)
    ll.insert(7)
    ll.insert(5)          # duplicate allowed
    ll.show()             # 5 <-> 5 <-> 7 <-> 10
    print("Length:", len(ll))          # 4
    print("Is 7 present?", ll.is_present(7))  # True
    print("Remove 5?", ll.remove(5))   # True (removes both)
    ll.show()             # 7 <-> 10
    print("Length:", len(ll))          # 2
    print("Is 5 present?", ll.is_present(5))  # False

    """

    """