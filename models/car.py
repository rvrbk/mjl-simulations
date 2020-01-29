from database import db
import datetime

class Car:
    d = db.DB()

    name = None
    weight = 0

    def __init__(self, id):
        car = self.d.one('SELECT * FROM cars WHERE id = {0}'.format(id))
        
        self.name = car[1]
        self.weight = car[2]

    def drive(self, scenario):
        units_under_pressure_per_spin = int((scenario.setup.amount_sidewall + scenario.setup.amount_base) * 4)
        
        min_units_output_per_spin = units_under_pressure_per_spin * scenario.setup.piezo.min_output
        max_units_output_per_spin = units_under_pressure_per_spin * scenario.setup.piezo.max_output
        
        meters_per_spin =  3.14 * (scenario.setup.tire.diameter * 100)
        spins_per_km = 4 * (1000 / (meters_per_spin / 1))

        min_output = (spins_per_km * int(scenario.distance) * min_units_output_per_spin)
        max_output = (spins_per_km * int(scenario.distance) * max_units_output_per_spin)

        self.d.query('INSERT INTO results(setup_id, scenario_id, min_output, max_output, created) VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\')'.format(scenario.setup.id, scenario.id, min_output, max_output, datetime.datetime.now()))