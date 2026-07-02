## Seperate chaining implementation of a hash table in Python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size, capacity):
        self.size = size
        self.capacity = capacity 
        self.table = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity 


    def insert(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value  # Update existing key
                    return
                current = current.next
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1


    def search(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError("Key not found")  # Key not found

    def remove(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        raise KeyError("Key not found for removal")  # Key not found

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False
        
if __name__ == "__main__":
    hash_table = HashTable(size=0, capacity=10)
    hash_table.insert("name", "Alice")
    hash_table.insert("age", 30)
    hash_table.insert("name", "Bob")  # Update existing key
    print(hash_table.search("name"))  # Output: Bob
    print(hash_table.search("age"))   # Output: 30
    hash_table.remove("name")
    print("name" in hash_table)      # Output: False
    print("age" in hash_table)       # Output: True
    print(len(hash_table))           # Output: 1
# time_complexity = {
#     "insert": "O(1) on average, O(n) in worst case",
#     "search": "O(1) on average, O(n) in worst case",
#     "remove": "O(1) on average, O(n) in worst case"
# }






# students = {
#     "Alice": {"age": 20, "grade": "A"},
#     "Bob": {"age": 22, "grade": "B"},
#     "Charlie": {"age": 21, "grade": "A"}
# }   

# for student, info in students.items():
#     print(f"{student}: Age={info['age']}, Grade={info['grade']}")