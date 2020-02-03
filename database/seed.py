import db

d = db.DB()

cars = []
piezos = []
tires = []
setups = []
scenarios = []

cars.append({ 'id': 1, 'name': 'Tesla Model 3', 'weight': 1611 })
cars.append({ 'id': 2, 'name': 'Rivian R1T', 'weight': 1800 })

piezos.append({ 'id': 1, 'name': 'DuraAct', 'weight': 20, 'width': 35, 'length': 61, 'height': 1, 'min_output': 10, 'max_output': 1000 })

tires.append({ 'id': 1, 'name': '225/45 R17', 'section_width': 225, 'aspect_ratio': 0.45, 'wheel_diameter': 17, 'weight': 4000 })

setups.append({ 'id': 1, 'name': 'Partial replacement', 'description': '', 'piezo_id': 1, 'tire_id': 1, 'amount_sidewall': 34, 'amount_base': 0 })

scenarios.append({ 'id': 1, 'car_id': 1, 'setup_id': 1, 'speed': 100, 'distance': 10000 })
scenarios.append({ 'id': 2, 'car_id': 1, 'setup_id': 1, 'speed': 80, 'distance': 5000 })

for car in cars:
    p = d.one('SELECT id FROM cars WHERE id = {0}'.format(car['id']))

    if(p == None):
        d.query('INSERT INTO cars(id, name, weight) VALUES(\'{0}\', \'{1}\', \'{2}\')'.format(car['id'], car['name'], car['weight']))

for piezo in piezos:
    p = d.one('SELECT id FROM piezos WHERE id = {0}'.format(piezo['id']))

    if(p == None):
        d.query('INSERT INTO piezos(id, name, weight, width, length, height, min_output, max_output) VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\', \'{6}\', \'{7}\')'.format(piezo['id'], piezo['name'], piezo['weight'], piezo['width'], piezo['length'], piezo['height'], piezo['min_output'], piezo['max_output']))

for tire in tires:
    p = d.one('SELECT id FROM tires WHERE id = {0}'.format(tire['id']))

    if(p == None):
        d.query('INSERT INTO tires(id, name, section_width, aspect_ratio, wheel_diameter, weight) VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\')'.format(tire['id'], tire['name'], tire['section_width'], tire['aspect_ratio'], tire['wheel_diameter'], tire['weight']))

for setup in setups:
    p = d.one('SELECT id FROM setups WHERE id = {0}'.format(setup['id']))

    if(p == None):
        d.query('INSERT INTO setups(id, name, description, piezo_id, tire_id, amount_sidewall, amount_base) VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\', \'{6}\')'.format(setup['id'], setup['name'], setup['description'], setup['piezo_id'], setup['tire_id'], setup['amount_sidewall'], setup['amount_base']))

for scenario in scenarios:
    p = d.one('SELECT id FROM scenarios WHERE id = {0}'.format(scenario['id']))

    if(p == None):
        d.query('INSERT INTO scenarios(id, car_id, setup_id, speed, distance) VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\')'.format(scenario['id'], scenario['car_id'], scenario['setup_id'], scenario['speed'], scenario['distance']))
