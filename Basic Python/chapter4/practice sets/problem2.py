# 2. Write a program to accept marks of 3 students and display them in a sorted
# manner.

marks = []
marks.append(float(input('Enter 1st mark: ')))
marks.append(float(input('Enter 2nd mark: ')))
marks.append(float(input('Enter 3rd mark: ')))
marks.sort()
print(marks)