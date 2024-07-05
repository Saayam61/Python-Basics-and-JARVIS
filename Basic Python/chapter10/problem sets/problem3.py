# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Problem3:
    a = 2
    
o = Problem3()
print(o.a) # 2
o.a = 0
print(o.a) # 0
print(Problem3.a) # 2
# Ans: No id does not change the class attribute, 
# it only changes the instance of that attribute (prints instance attribute)