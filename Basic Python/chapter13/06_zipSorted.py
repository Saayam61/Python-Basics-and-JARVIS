# sorted(): Returns a new sorted list from the elements of any iterable.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
letter = ['c','saayam', 'b']
sorted_nums = sorted(numbers)
sorted_letter = sorted(letter)
print(sorted_nums)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]
print(sorted_letter)  # Output: ['b', 'c', 'saayam']

points = [(1, 2), (3, 1), (5, -1), (2, 3)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)  # Output: [(5, -1), (3, 1), (1, 2), (2, 3)]

# zip(): Takes iterables(more than one) (lists, tuples, etc.) as arguments and returns an iterator of 
# tuples where the i-th tuple contains the i-th element from each of the input iterables.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
