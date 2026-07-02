# ## Pure Function Definition
# def pure_func(List):
#     New_List = []
#     for i in List:
#         New_List.append(i*2)
#     return New_List
# my_list = [1, 2, 3, 4, 5]
# modified_list = pure_func(my_list)
# print(modified_list)


# ## Recursion in Functional Programming
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))  # Output: 120


## Functions are First-Class Citizens in Python

# def shout(text):
#     return text.upper() + "!!!"
# def whisper(text):
#     return text.lower() + "..."
# def greet(func): ## func, value is used as a parameter to pass the function as an argument
#     greeting = func("Hello, World") ## func is called with the argument "Hello, World"
#     print(greeting)



# greet(shout)   # Output: HELLO, WORLD!!!
# greet(whisper) # Output: hello, world...


# ## A function is an instance of the Object type
# ## You can store the function in a variable
# ## You can pass the function as an argument to another function
# ## You can return a function from another function
# ## You can store functions in data structures such as lists, dictionaries, etc.




## Built-in Higher-Order Functions in Python

#map function

# def addition(n):
#     return n+n

# numbers = [1, 2, 3, 4, 5]
# result = map(addition, numbers) 

# print(type(result)) # Output: <map object at 0x7f8b8c8c8c8c>
# for x in result:
#     print(x) # Output: 2, 4, 6, 8, 10



# filter function

## The filter function is used to filter the elements of a sequence based on a given condition. 
# It takes two arguments: a function that defines the condition and an iterable (like a list) to be filtered. 
# The function should return True for elements that should be included in the result and False for those that should be excluded.


def fun(n):
    letters = ['a', 'e', 'i', 'o', 'u']
    if n in letters:
        return True
    else:
        return False
sequence = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
filtered_sequence = filter(fun, sequence)

print(type(filtered_sequence)) # Output: <filter object at 0x7f8b8c8c8c8c>
for x in filtered_sequence:
    print(x) 



## lambda function
lambda_func = lambda x: x * 2 ## lambda arguments: expression
print(lambda_func(5)) # Output: 10


