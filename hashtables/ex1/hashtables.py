

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0


    # Hash int
    def hash(self, x):
        x = ((x >> 16) ^ x) * 0x45d9f3b
        x = ((x >> 16) ^ x) * 0x45d9f3b
        x = ((x >> 16) ^ x)

        return x % self.capacity


    # '''
    # Fill this in.

    # Hint: Used the LL handle collisions
    # '''
    def hash_table_insert(self, key, value):
        self.count += 1

        if self.count / self.capacity >= 0.7:
            self.count = 0
            self.hash_table_resize()

        index = hash(key)
        current_pair = self.storage[index]
        last_pair = None

        while current_pair is not None and current_pair.key != key:
            last_pair = current_pair
            current_pair = last_pair.next

        if current_pair is not None:
            current_pair.value = value
        else:
            new_pair = LinkedPair(key, value)
            new_pair.next = self.storage[index]
            self.storage[index] = new_pair



    # '''
    # Fill this in.

    # If you try to remove a value that isn't there, print a warning.
    # '''
    def hash_table_remove(self, key):
        index = hash(key)

        current_pair = self.storage[index]
        last_pair = None

        while current_pair is not None and current_pair.key != key:
            last_pair = current_pair
            current_pair = last_pair.next

        if current_pair is None:
            print("ERROR: Unable to remove entry with key " + key)
        else:
            if last_pair is None:  # Removing the first element in the LL
                self.storage[index] = current_pair.next
            else:
                last_pair.next = current_pair.next


    # '''
    # Fill this in.

    # Should return None if the key is not found.
    # '''
    def hash_table_retrieve(self, key):
        index = hash(key)

        current_pair = self.storage[index]

        while current_pair is not None:
            if(current_pair.key == key):
                return current_pair.value
            current_pair = current_pair.next
        return None


    # '''
    # Fill this in
    # '''
    def hash_table_resize(self):
        new_hash_table = HashTable(2 * len(self.storage))

        current_pair = None

        for i in range(len(self.storage)):
            current_pair = self.storage[i]
            while current_pair is not None:
                self.hash_table_insert(
                                current_pair.key,
                                current_pair.value)
                current_pair = current_pair.next

        return new_hash_table
