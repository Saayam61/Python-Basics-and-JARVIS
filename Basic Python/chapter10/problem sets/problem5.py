# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

from random import randint

class Train:
    
    def __init__(self, trainNo) -> None:
        self.trainNo = trainNo
    
    def book(self, From, to):
        print(f'The ticket is booked in train number {self.trainNo} from {From} to {to}.')
    
    def getStatus(self):
        print(f'The number of seats available in train {self.trainNo} is {randint(1,50)}')

    def getFare(self, From, to):
        print(f'The ticket fare in train number {self.trainNo} from {From} to {to} is {randint(500, 10000)}.')

a = Train(734612)
a.getStatus()
a.getFare('Nepal','USA')
a.book('Nepal','USA')

