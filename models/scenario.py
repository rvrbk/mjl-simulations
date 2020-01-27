from database import db
from models import car
from models import setup

class Scenario:
    d = db.DB()

    car = None
    setup = None
    speed = 0
    distance = 0

    def __init__(self, id):
        scenario = self.d.one('SELECT * FROM scenarios WHERE id = {0};'.format(id))

        self.car = car.Car(scenario[1])
        self.setup = setup.Setup(scenario[2])
        self.speed = scenario[3]
        self.distance = scenario[4]

    def play(self):
        print(self.setup.piezo.name)