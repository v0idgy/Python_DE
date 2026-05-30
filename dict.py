# def sort_dict_by_value(d, reverse=False):
#     return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


# colors = {"Red": 1, "Green": 5, "Blue": 2, "Black": 4, "White": 3}
# print(colors)
# print("Sorted dict in ascending order:", sort_dict_by_value(colors))
# print("Sorted dict in descending order:", sort_dict_by_value(colors, reverse=True))



## Merge two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

def merge_dicts(*dicts):
    merged_dict = {}
    for d in dicts:
        merged_dict.update(d)
    return merged_dict
merged = merge_dicts(dict1, dict2)
print(merged)
