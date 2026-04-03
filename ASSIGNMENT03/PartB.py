class ChainingTable:
    class Record:
        # Simple class to hold key-value pairs
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, capacity=32):
        self.capacity = capacity
        # The table is a list of lists (chains for collision resolution)
        # Each slot in the_table will hold a list of Records
        self.the_table = [[] for _ in range(capacity)]
        self.size = 0  # Number of actual records stored

    def _hash_index(self, key):
        # Use Python's built-in hash function and modulo for index
        return hash(key) % self.capacity

    def _resize(self):
        old_table = self.the_table
        old_capacity = self.capacity

        self.capacity *= 2
        self.the_table = [[] for _ in range(self.capacity)]
        self.size = 0  # Reset size, as records will be re-inserted

        # Rehash all existing records into the new, larger table
        for bucket in old_table:
            for record in bucket:
                self.insert(record.key, record.value)

    def insert(self, key, value):
        # Check if key already exists
        if self.search(key) is not None:
            return False

        # Check load factor and resize if necessary
        # Load factor = size / capacity. If it exceeds 1.0, resize.
        if (self.size + 1) / self.capacity > 1.0:
            self._resize()

        idx = self._hash_index(key)
        self.the_table[idx].append(self.Record(key, value))
        self.size += 1
        return True

    def modify(self, key, value):
        idx = self._hash_index(key)
        for record in self.the_table[idx]:
            if record.key == key:
                record.value = value
                return True
        return False

    def remove(self, key):
        idx = self._hash_index(key)
        # Iterate through the chain to find and remove the record
        # Create a new list for the bucket, excluding the removed record (if found)
        # This prevents issues with modifying a list while iterating over it
        new_chain = []
        found = False
        for record in self.the_table[idx]:
            if record.key == key:
                found = True
            else:
                new_chain.append(record)

        if found:
            self.the_table[idx] = new_chain
            self.size -= 1
            return True
        return False

    def search(self, key):
        idx = self._hash_index(key)
        for record in self.the_table[idx]:
            if record.key == key:
                return record.value
        return None  # Key not found

    def capacity(self):
        return self.capacity

    def __len__(self):
        return self.size

