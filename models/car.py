from database import db

class Car:
    d = db.DB()

    name = None
    weight = 0

    def __init__(self, id):
        car = self.d.one('SELECT * FROM cars WHERE id = {0}'.format(id))
        
        self.name = car[1]
        self.weight = car[2]

    def drive(self, tire, piezo, setup):
        print('{} weighs {} drives'.format(self.type, self.weight))