class vehicles:
    def __init__(self, make, model, year, weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = needsMaintenance
        self.tripsSinceMaintenance = tripsSinceMaintenance

    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def setYear(self, year):
        self.year = year

    def setWeight(self, weight):
        self.weight = weight

    def getInfo(self):
        print("make: ", self.make,"\n","Model: ", self.model,"\n", "Year: ", make.year,"\n", "Weight: ", self.make, "\n", "Needs Maintenance: ", self.needsMaintenance,"\n", "Trips Since Maintenance: ", self.tripsSinceMaintenance, "\n")

class Cars(vehicles):
    def __init__(self, make, model, year, weight, needsMaintenance = False, tripsSinceMaintenance = 0, isDriving=False):
        vehicles.__init__(self, make, model, year, weight, needsMaintenance, tripsSinceMaintenance)
        self.isDriving = isDriving

    def drive(self):
        self.isDriving = True

    def stop(self):
        self.isDriving = False
        self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True

    def repair(self):
        self.needsMaintenance = False


rs6 = Cars("audi", "rs6 avant", "2020", 4600, False, 0, False)
m5 = Cars("BMW", "e39 M5", "2001", 3957, True, 37, True)
p_911 = Cars("Porsche", "911-997.2 GT3", "2011", 3075, False, 97, False)

for i in range(10):
    rs6.drive()
    rs6.stop()

for i in range(50):
    m5.drive()
    m5.stop()

for i in range(100):
    p_911.drive()
    p_911.stop()

myCars = [rs6, m5, p_911]

for i in myCars:
    print("Make:", i.make)
    print("Model:", i.model)
    print("Year:", i.year)
    print("Weight:", i.weight)
    print("Needs Maintenance:", i.needsMaintenance)
    print("Trips Since Maintenacne:", i.tripsSinceMaintenance, "\n")
