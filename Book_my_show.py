def singleTon(cls):
    L = []
    def inner():
        if len(L) == 0:
            L.append(cls())
        return L[0]
    return inner

@singleTon
class Hanuman:
    def __init__(self):
        self.tickets = 400
        
    def Booking(self, tickets):
        if self.tickets >= tickets:
            self.tickets -= tickets
            print(f'{tickets} booked successfully')
        else:
            print('tickets not found')

@singleTon
class Salar:
    def __init__(self):
        self.tickets = 400
        
    def Booking(self, tickets):
        if self.tickets >= tickets:
            self.tickets -= tickets
            print(f'{tickets} booked successfully')
        else:
            print('tickets not found')

@singleTon
class Animal:
    def __init__(self):
        self.tickets = 400
        
    def Booking(self, tickets):
        if self.tickets >= tickets:
            self.tickets -= tickets
            print(f'{tickets} booked successfully')
        else:
            print('tickets not found')

def Book_my_Show():
    print('1->Hanuman \n 2->Salar \n 3->Animal')
    option = int(input('choose an option:'))
    if option == 1:
        H1 = Hanuman()
        tickets = int(input('enter number of tickets:'))
        H1.Booking(tickets)
    elif option == 2:
        S1 = Salar()
        tickets = int(input('enter number of tickets:'))
        S1.Booking(tickets)
    elif option == 3:
        A1 = Animal()
        tickets = int(input('enter number of tickets:'))
        A1.Booking(tickets)
    else:
        print('movie not found')
while True:
    Book_my_Show()
    print('-'*30)
    

