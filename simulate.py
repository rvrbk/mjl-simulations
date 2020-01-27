from models import scenario 
from database import db

d = db.DB()

scenarios = d.all('SELECT * FROM scenarios;')

for data_scenario in scenarios:
    s = scenario.Scenario(data_scenario[0])

    s.play()






# https://www.quora.com/The-wheel-diameter-is-0-3-meters-how-many-times-does-the-wheel-rotate-for-each-kilometer-travelled
# https://www.researchgate.net/post/What_is_the_maximum_voltage_and_amphere_for_a_single_piezoelectric_element_recorded_is_it_PZT_lead_titanate_ceramics_or_lead_metaniobate_ceramics (2nd answer)

#import yaml

#piezos = []
#cars = []

#with open('piezos.yaml', 'r') as file: 
#    piezos = yaml.load(file, Loader=yaml.FullLoader)

#with open('cars.yaml', 'r') as file:
#    cars = yaml.load(file, Loader=yaml.FullLoader)

#for car in cars:
#    for piezo in piezos:
#        print(car['name'] + ' with ' + piezo['name'])
        
#        units_under_pressure_per_spin = int(piezo['amount'] / 6)
#        units_under_pressure = int(units_under_pressure_per_spin * 4)
#        unit_output_per_spin = 1 * (piezo['size'] * piezo['max_output_per_mm']) 
#        units_output_per_spin = 1 * (units_under_pressure_per_spin * unit_output_per_spin)
#        meters_per_spin =  3.14 * car['wheel_size']
#        spins_per_km = 4 * (1000 / (meters_per_spin / 1))

#        print('- Units under pressure per spin per tire: ' + str(units_under_pressure_per_spin))
#        print('- Combined units under pressure: ' + str(units_under_pressure))
#        print('- Power output per unit (per spin): ' + str(unit_output_per_spin) + 'v')
#        print('- Combined power output (per spin): ' + str(units_output_per_spin) + 'v')
#        print('- Combined power output per 10km: ' + str((spins_per_km * 10) * units_output_per_spin) + 'v')