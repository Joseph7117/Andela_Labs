class Car(object):
    
    def __init__(self, cartype=None, model='GM', name='General', speed=0):
        self.cartype = cartype
        self.model = model
        self.name = name
        self.speed = speed

        if self.name in ['Porsche', 'Koeingsegg']:
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.cartype == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def getCarName(self):
        return self.name

    def getCarModel(self):
        return self.model

    def getCarType(self):
        return self.cartype

    def is_saloon(self):
        if self.cartype is not 'trailer':
            self.cartype == 'saloon'
            return True
        else:
            return False

    def drive(self, drvspeed):
        if drvspeed == 7:
            self.speed = 77
        elif drvspeed == 3:
            self.speed = 1000
        return self
