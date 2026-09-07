def find_duplicates(input_list):
    result = []
    for num in input_list:
        index = abs(num) - 1 
        if input_list[index] < 0:
            result.append(index + 1)
        else:
            input_list[index] = -input_list[index]
    return result

example_list = [4, 3, 2, 7, 8, 2, 3, 1]
duplicates = find_duplicates(example_list)
print("Duplicates in the list:", duplicates)