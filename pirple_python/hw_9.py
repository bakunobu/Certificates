class Vehicle:
    def __init__(self, make:str, model:str,
                 year:int, weight:float,
                 NeedsMaintenance:bool=False,
                 TripsSinceMaintenance:int=0) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance


class Car(Vehicle):
    def __init__(self, make:str, model:str,
                 year:int, weight:float,
                 NeedsMaintenance:bool=False,
                 TripsSinceMaintenance:int=0,
                 isDriving:bool=False) -> None:
        Vehicle.__init__(self, make, model, year, weight, 
                             NeedsMaintenance, TripsSinceMaintenance)
        self.isDriving = isDriving
            
            
    def drive(self):
        self.isDriving = True
            
            
    def stop(self):
        self.isDriving = False
        self.TripsSinceMaintenance += 1
        if self.TripsSinceMaintenance < 100:
            self.NeedsMaintenance = True
            
        
    def repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False
            
            
car1 = Car('Skoda', 'Superb', 2012, 1726.0)
car2 = Car('Renault', 'Megane', 2013, 1460.5, True, 25)
car3 = Car('Lada', 'Kalina', 2014, 1280.0, True, 78)


class Plane(Vehicle):
    def __init__(self, make:str, model:str,
                 year:int, weight:float,
                 NeedsMaintenance:bool=False,
                 TripsSinceMaintenance:int=0,
                 isFlying:bool=False) -> None:
        Vehicle.__init__(self, make, model, year, weight, 
                             NeedsMaintenance, TripsSinceMaintenance)
        self.isFlying = isFlying
    
    
    def flying(self):
        if not self.NeedsMaintenance:
            self.isFlying = True
        else:
            self.isFlying = False
            print('The plane can\'t fly until it\'s repaired') 
            
            
    def landing(self):
        self.isFriving = False
        self.TripsSinceMaintenance += 1
        if self.TripsSinceMaintenance < 100:
            self.NeedsMaintenance = True
            
        
    def repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False
        

plane1 = Plane('Il', '2', 1942, 4360.0)

