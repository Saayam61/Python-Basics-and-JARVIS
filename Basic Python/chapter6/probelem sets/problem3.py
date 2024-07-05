# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

cmt = input('Enter your comment: ')
if 'Make a lot of money' in cmt or 'buy now' in cmt or 'subscribe this' in cmt or 'click this' in cmt:
    print('This is a spam')
else:
    print('This is not a spam')
    