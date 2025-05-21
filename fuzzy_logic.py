import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

# Вхідні змінні
budget = ctrl.Antecedent(np.arange(0, 101, 1), 'budget')
deadline = ctrl.Antecedent(np.arange(0, 101, 1), 'deadline')
complexity = ctrl.Antecedent(np.arange(0, 101, 1), 'complexity')
team_experience = ctrl.Antecedent(np.arange(0, 101, 1), 'team_experience')
uncertainty = ctrl.Antecedent(np.arange(0, 101, 1), 'uncertainty')

# Вихідна змінна
risk = ctrl.Consequent(np.arange(0, 101, 1), 'risk')

# Визначення нечітких множин (5 рівнів)
levels = ['very_low', 'low', 'medium', 'high', 'very_high']
budget.automf(5, names=levels)
deadline.automf(5, names=levels)
complexity.automf(5, names=levels)
team_experience.automf(5, names=levels)
uncertainty.automf(5, names=levels)

risk['very_low'] = fuzz.trimf(risk.universe, [0, 0, 25])
risk['low'] = fuzz.trimf(risk.universe, [10, 30, 50])
risk['medium'] = fuzz.trimf(risk.universe, [30, 50, 70])
risk['high'] = fuzz.trimf(risk.universe, [50, 70, 90])
risk['very_high'] = fuzz.trimf(risk.universe, [75, 100, 100])



