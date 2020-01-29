from database import db
from models import piezo
from models import tire

class Setup:
    d = db.DB()

    id = 0
    name = None
    description = None
    piezo = None
    tire = None
    amount_sidewall = 0
    amount_base = 0

    def __init__(self, id):
        setup = self.d.one('SELECT * FROM setups WHERE id = {0}'.format(id))
        
        self.id = setup[0]
        self.name = setup[1]
        self.description = setup[2]
        self.piezo = piezo.Piezo(setup[3])
        self.tire = tire.Tire(setup[4])
        self.amount_sidewall = setup[5]
        self.amount_base = setup[6]