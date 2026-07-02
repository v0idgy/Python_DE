def keys_upper(test_dict):
    return {k.upper(): keys_upper(v) if isinstance(v, dict) else v for k, v in test_dict.items() }
test_dict = {'a': 1, 'b': {'b': 2}, 'c': 3}

result = keys_upper(test_dict)
print(result)