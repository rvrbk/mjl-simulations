from database import db

class Tire:
    d = db.DB()

    name = None
    section_width = 0
    aspect_ratio = 0
    wheel_diameter = 0
    weight = 0
    diameter = 0

    def __init__(self, id):
        tire = self.d.one('SELECT * FROM tires WHERE id = {0}'.format(id))
        
        self.name = tire[1]
        self.section_width = tire[2]
        self.aspect_ratio = tire[3]
        self.wheel_diameter = tire[4]
        self.weight = tire[5]

        self.diameter = ((self.section_width * self.aspect_ratio) * 2) + (self.wheel_diameter * 25.4)