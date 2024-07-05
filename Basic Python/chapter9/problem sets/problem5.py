# 5. Repeat program 4 for a list of such words to be censored.

l = ['Donkey','Monkey','Pig']

with open('censor.txt') as f:
    data = f.read()
    
for word in l:
    if word in data:
        data = data.replace(word, '#'*len(word))
        
with open('censor.txt','w') as f:
    f.write(data)