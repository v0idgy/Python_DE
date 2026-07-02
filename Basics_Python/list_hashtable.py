my_list = [[],[],[],[],[],[],[],[],[],[]]  # Initialize a list with 10 None values act as Hashtable buckets

### Empty hashtable with 10 buckets, each bucket is a list to handle collisions

def hash_function(value):  # a = 97, b = 98, c = 99, d = 100, e = 101, f = 102, g = 103, h = 104, i = 105, j = 106, k = 107, l = 108, m = 109, n = 110, o = 111, p = 112, q = 113, r = 114, s = 115, t = 116, u = 117, v = 118, w = 119, x = 120, y = 121, z = 122 
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)  # Get ASCII value of each character and sum them up
    return sum_of_char % 10  # Return the index by taking modulus with the length of the list


print("Hash function for Gourav is:", hash_function("Gourav"))  # Example usage of the hash function
def add(name):
    index = hash_function(name)  # Get the index for the given name using the hash function
    my_list[index] = [name]  # Store the name at the computed index in the list


add("Sourav")
add("Alice")
add("Bob")
add("Lisa")
add("Stuart")
print(my_list)  # Output the list to see the added names at their respective indices

def search(name):
    index = hash_function(name)  # Get the index for the given name using the hash function
    return name in my_list[index] # Return True if the name is in the list at the computed index

print(search("Sourav"))  # Output: True
print(search("Bob"))   # Output: True
print(search("Alice")) # Output: True


def add1(name):
    index = hash_function(name)  # Get the index for the given name using the hash function
    my_list[index].append(name) # If there is a collision, append the name to the list at that index

add1("Stuart")
add1("Lisa")  # This will cause a collision and both names will be stored in the same bucket
print(my_list)  # Output the list to see the added names and how collisions are handled