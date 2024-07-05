# 6. Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

class Demo:
    def demo(harry):
        print('Hello user')

a = Demo()
a.demo()
# Nothing changes whatever you write but it is convention to write self.