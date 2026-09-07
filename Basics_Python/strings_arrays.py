from functools import cmp_to_key

def largestNumber(nums):
    str_nums = [str(num) for num in nums]
    str_nums.sort(key=cmp_to_key(lambda x, y: -1 if x + y > y + x else 1))
    
    # Join into a single string
    result = "".join(str_nums)
    return '0' if result[0] == '0' else result
print(largestNumber([3, 5, 4, 2, 8]))  
print(largestNumber([2, 4, 3, 4]))     