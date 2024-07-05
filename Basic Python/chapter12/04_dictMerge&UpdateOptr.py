# The | operator is used to merge two dictionaries into a new dictionary. 
# It creates a new dictionary that contains all key-value pairs from both dictionaries.

# In the merged dictionary, if there are keys that exist in both dict1 and dict2, 
# the value from dict2 overrides the value from dict1

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict1 | dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# The |= operator is used to update the dictionary on the left-hand side (LHS) with key-value pairs 
# from the dictionary on the right-hand side (RHS). It modifies the dictionary in-place.

# After the update operation (dict1 |= dict2), dict1 is modified to include all key-value pairs from 
# dict2. If there are common keys, the values from dict2 overwrite the values in dict1.

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1 |= dict2
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}
