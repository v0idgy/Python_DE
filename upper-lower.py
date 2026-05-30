sentence  = 'The quick Brown Fox jumps over the Lazy Dog'
counts = {'upper': 0, 'lower': 0}

for char in sentence:
    if char.isupper():
        counts['upper'] += 1
    elif char.islower():
        counts['lower'] += 1


print("Number of uppercase characters:", counts['upper'])
print("Number of lowercase characters:", counts['lower'])