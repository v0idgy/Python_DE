# def add(a,b):   ### Recursive function to add two numbers without using the + operator
#     if b == 0:
#         return a
#     else:
#         return add(a+1, b-1)

# 0 1 1 2 3 5 8 13 21 34

## Problem 1: Write a recursive function to calculate the fibonacci sequence up to n terms.

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# n_terms = 10
# print("Fibonacci sequence up to", n_terms, "terms:")
# for i in range(n_terms):
#     print(fibonacci(i), end=' ')

## Problem 2: Print all increasing sequences of length k from a set of n natural numbers. 
#### Description: Given two integers n and k, write a recursive function to print all 
# increasing sequences of length k that can be formed from the first n natural numbers.

### Exmp:
### Input: n = 3, k = 2
### Output:
### 1 2
### 1 3
### 2 3

### Input: n = 5, k = 5
### Output:
### 1 2 3 4 5

### Input: n = 5, k = 3
### Output:
### 1 2 3
### 1 2 4
### 1 2 5
### 1 3 4
### 1 3 5
### 1 4 5
### 2 3 4
### 2 3 5
### 2 4 5
### 3 4 5   


### Method 1 : Using a helper function to generate the sequences recursively

# def printArr(arr, k):
#     for i in range(k):
#         print(arr[i], end=' ')
#     print()
# def printSeq(n, k, len, arr):
#     if len == k:
#         printArr(arr, k)
#         return
#     i = 1 if len == 0 else arr[len-1] + 1
#     len += 1
#     while i <= n:
#         arr[len-1] = i
#         printSeq(n, k, len, arr)
#         i += 1
#     len -= 1
# def printSequences(n, k):
#     arr = [0] * k
#     len = 0
#     printSeq(n, k, len, arr)


# k = 3
# n = 5
# printSequences(n, k)

### Method 2 

# def print_increasing_sequences(n, k):
#     def build_sequence(start, sequence):
#         if len(sequence) == k:
#             print(sequence)
#             return
#         elements = k - len(sequence)  # Number of elements still needed to complete the sequence
#         element_available = n - start + 1  # Number of elements available to choose from
#         if elements > element_available:  # If we need more elements than available, return early
#             return
#         for i in range(start, n + 1):
#             build_sequence(i + 1, sequence + [i])  # Recur with the next number and the current sequence
#     build_sequence(1, [])  # Start building sequences from the first number


# print_increasing_sequences(5, 3)


## Problem 3 : Implement factorial using recursion.

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# num = 5 
# print("Factorial of", num, "is", factorial(num)). ## 5 * 4 * 3 * 2 * 1 = 120


# Steps to implement recursion in Python:
# 1.Define the base case: Identify the simplest instance of the problem that 
# can be solved directly without recursion. This will prevent infinite recursion and provide 
# a stopping point for the recursive calls.

# 2. Define the recursive case: Break down the problem into smaller subproblems that can be 
# solved using the same function. The recursive case should move towards the base case with each call.

# 3. Ensure that the recursion terminates: Make sure that the recursive calls eventually 
# reach the base case. This can be achieved by modifying the input parameters in a way that 
# they approach the base case.

# 4. Test the function: After implementing the recursive function, test it with various 
# inputs to ensure that it works correctly and handles edge cases appropriately.




## Write a recursive function to calculate the sum of n natural numbers.



# def sum_of_natural_numbers(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_of_natural_numbers(n - 1)
    
# print("Sum of first 5 natural numbers is:", sum_of_natural_numbers(5))  # Output: 15 (1 + 2 + 3 + 4 + 5 = 15)   









