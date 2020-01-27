from database import db

class Piezo:
    d = db.DB()

    name = None
    weight = 0
    length = 0
    width = 0
    height = 0
    min_output = 0
    max_output = 0

    def __init__(self, id):
        piezo = self.d.one('SELECT * FROM piezos WHERE id = {0}'.format(id))
        
        self.name = piezo[1]
        self.weight = piezo[2]
        self.length = piezo[3]
        self.width = piezo[4]
        self.height = piezo[5]
        self.min_output = piezo[6]
        self.max_output = piezo[7]