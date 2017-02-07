class Car(object):
    def __init__(self, cartype, model, name):
        self.cartype = cartype
        self.model = model
        self.name = name

        if self.name in ['Porsche', 'Koeingsegg']:
            self.doors = 2
        else:
            self.doors = 4

        if self.cartype == 'trailer':
            self.wheels = 8
        else:
            self.wheels = 4

    def getCarName(self):
        return self.name

    def getCarModel(self):
        return self.model

    def getCarType(self):
        return self.cartype

    def is_salon(self):
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