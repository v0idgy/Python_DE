import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

list = [2,3,5,7,9,11,13,15,17,19,20]
prime_numbers = [num for num in list if is_prime(num)]


print("Prime numbers in the list:", prime_numbers)
