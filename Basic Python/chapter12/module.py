# this file is imported as module in ifName==Main.py
def myFunction():
    print('Hello World!')

# if the function is called here, the ifName file will run this code without even 
# calling the function in ifName.py (just by importing the module). So dont do it.
# myFunction()

# if this whole code is directly run by the file it is present in it will display __main__
# if this file was imported as module and run from that file it will display the name of this file.
print(__name__)

# the code inside it will only run in the file it is written in.
# it wont run in the another file if this file was imported as module
if __name__ == '__main__':
    print('We are directly running this code')
    
    # this function is called here as this call is needed only in our original file not in another.
    myFunction()