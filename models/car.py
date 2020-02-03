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
        units = int(scenario.setup.amount_sidewall + scenario.setup.amount_base)

        amp = ((scenario.setup.piezo.width + scenario.setup.piezo.length) / 2) * 0.1

        min_units_output_per_spin = units * scenario.setup.piezo.min_output
        max_units_output_per_spin = units * scenario.setup.piezo.max_output

        meters_per_spin =  3.14 * (scenario.setup.tire.diameter / 1000)
        spins_per_m = 1 / meters_per_spin
        spins_per_km = (1000 * spins_per_m)

        min_output_kw = ((spins_per_km * (scenario.distance / 1000) * min_units_output_per_spin) * amp) / 1000
        max_output_kw = ((spins_per_km * (scenario.distance / 1000) * max_units_output_per_spin) * amp) / 1000

        min_output_kwh = min_output_kw * (scenario.distance / scenario.speed)
        max_output_kwh = max_output_kw * (scenario.distance / scenario.speed)

        print('units: {0}, min_units_output_per_spin: {1}, max_units_output_per_spin: {2}, meters_per_spin: {3}, spins_per_km: {4}, min_output: {5}, max_output: {6}'.format(units, min_units_output_per_spin, max_units_output_per_spin, meters_per_spin, spins_per_km, min_output_kw, max_output_kw))

        #self.d.query('INSERT INTO results(setup_id, scenario_id, min_output, max_output, created) VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\')'.format(scenario.setup.id, scenario.id, min_output_kw, max_output_kw, datetime.datetime.now()))