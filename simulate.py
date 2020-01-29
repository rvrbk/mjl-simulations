# https://www.quora.com/The-wheel-diameter-is-0-3-meters-how-many-times-does-the-wheel-rotate-for-each-kilometer-travelled
# https://www.researchgate.net/post/What_is_the_maximum_voltage_and_amphere_for_a_single_piezoelectric_element_recorded_is_it_PZT_lead_titanate_ceramics_or_lead_metaniobate_ceramics (2nd answer)

from models import scenario 
from database import db

d = db.DB()

scenarios = d.all('SELECT * FROM scenarios;')

for data_scenario in scenarios:
    s = scenario.Scenario(data_scenario[0])

    s.play()