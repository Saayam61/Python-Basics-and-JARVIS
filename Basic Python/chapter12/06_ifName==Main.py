# it will call myFunction() just by importing if it's calling was not inside if __name__ == 'main'
from module import myFunction
# import module
# module.myFunction()

# if inside if __name__ == 'main', we need to call it like this
myFunction()
