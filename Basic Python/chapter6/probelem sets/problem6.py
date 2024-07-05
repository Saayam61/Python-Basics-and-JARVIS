# 6. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks = int(input('Enter  a number: '))

if marks>100 or marks<0:
    print('Invalid marks')
elif marks>=90:
    print('The grade is Ex')
elif marks>=80:
    print('The grade is A')
elif marks>=70:
    print('The grade is B')
elif marks>=60:
    print('The grade is C')
elif marks>=50:
    print('The grade is D')
else:
    print('The grade is F')