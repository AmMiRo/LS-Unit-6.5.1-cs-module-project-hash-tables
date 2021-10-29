class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.storage = [None] * capacity
        self.num_items = 0

    @property
    def capacity(self):
        return len(self.storage)

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.num_items / self.capacity


    def increase_size(self):
        self.num_items += 1
        if self.get_load_factor() > 0.7:
            return self.resize(self.capacity * 2)


    def decrease_size(self):    
        self.num_items -= 1
        if self.get_load_factor() < 0.2:
            half_size = self.capacity // 2
            if half_size <= MIN_CAPACITY:
                return self.resize(MIN_CAPACITY)
            elif half_size > MIN_CAPACITY:
                return self.resize(half_size)


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        
        if self.storage[i] == None:
            self.storage[i] = HashTableEntry(key, value)
            self.increase_size()
        else:
            current = self.storage[i]
            while True:
                if current.key == key:
                    current.value = value
                    return
                elif current.next is None:
                    current.next = HashTableEntry(key, value)
                    self.increase_size()
                    return
                else:
                    current = current.next
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        current = self.storage[i]
        prev = None
        if current.key == key:
            if current.next != None:
                self.storage[i] = current.next
                self.decrease_size()
                return
            else:
                self.storage[i] = None
                self.decrease_size()
                return
        else:
            while current != None:
                if current.key == key:
                    prev.next = current.next
                    current = None
                    self.decrease_size()
                    return
                else:
                    prev = current
                    current = current.next
            


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        current = self.storage[i]
        if current is None:
            return
        while current != None:
            if current.key == key:
                return current.value
            else:
                current = current.next


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_storage = self.storage[:]
        self.storage = [None] * new_capacity
        self.num_items = 0
        for x in old_storage:
            if x != None:
                current = x
                while current != None:
                    self.put(current.key, current.value)
                    current = current.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
