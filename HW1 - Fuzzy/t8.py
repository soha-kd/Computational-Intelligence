import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

food = ctrl.Antecedent(np.arange(0, 11, 1), 'food')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(4, 26, 1), 'tip')
food['rancid'] = fuzz.trimf(food.universe, [0,0,3])
food['good'] = fuzz.trimf(food.universe, [2,5,8])
food['delecious'] = fuzz.trimf(food.universe, [7,10,10])
service['poor'] = fuzz.trimf(service.universe, [0,0,4])
service['average'] = fuzz.trimf(service.universe, [3,6,9])
service['good'] = fuzz.trimf(service.universe, [8,10,10])
tip['cheap'] = fuzz.trimf(tip.universe, [5,5,13])
tip['average'] = fuzz.trimf(tip.universe, [12,18,23])
tip['generous'] = fuzz.trimf(tip.universe, [16,25,25])
rule1 = ctrl.Rule(food['delicious'] | service['good'], tip['generous'])
rule2 = ctrl.Rule(food['rancid'] | service['poor'], tip['cheap'])
rule3 = ctrl.Rule(food['good'] | service['average'], tip['average'])
rule4 = ctrl.Rule(food[' rancid '], tip['cheap'])
tip_ctrl = ctrl.ControlSystem([rule1, rule2, rule3 , rule4])
tipping.input['quality'] = 4
tipping.input['service'] = 7.2
tipping.compute()
print tipping.output['tip']



