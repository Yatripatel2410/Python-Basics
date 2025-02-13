class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True #ye sab un-nessasary chije hide ho jayegi and sirf
        self.acc=True
        print("car started")  #nessasory chije dikhegi jinki jarurat hai

car1=car()
car1.start()        

#encapsulation:--->wrapping data and function into a single unit (object)