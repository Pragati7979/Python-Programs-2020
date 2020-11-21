class Train:
    seatList = []
    def __init__(self,name,seat,fare):
        global seatList
        self.name = name
        self.seat = seat
        self.fare = fare
        for i in range(1,self.seat+1):
            self.seatList.append(i)
        print("Available Seats:")
        print(self.seatList)

    def printSeats(self):
        print("Now available seats are:")
        self.seatList.sort()
        print(self.seatList)
        
    def getStatus(self):
        print("*"*10)
        print(f"Name of train is {self.name}")
        print(f"Number of seat available is {self.seat}")
        print("*"*10)

    def getFare(self):
        print(f"The cost of ticket is Rs.{self.fare}")

    def bookTicket(self):
        if(self.seat > 0):
            print("Your ticket has been booked")
            print(f"Your seat no. is {self.seat}")
            self.seatList.remove(self.seat)
            self.seat = self.seat - 1
            
        else:
            print("Sorry the train is booked!!")

    def cancelTicket(self,seatNo):
        print("Ticket number {self.seatNo} has been cancelled")
        self.seatList.append(seatNo)
        self.printSeats()

        
intercity = Train("Intercity",10,50)
intercity.getStatus()
intercity.bookTicket()
intercity.printSeats()
intercity.bookTicket()
intercity.printSeats()
intercity.bookTicket()
intercity.printSeats()
intercity.bookTicket()
intercity.printSeats()

intercity.cancelTicket(9)
intercity.cancelTicket(7)

