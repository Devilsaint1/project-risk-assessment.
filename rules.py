from fuzzy_logic import budget, deadline, complexity, team_experience, uncertainty, risk
import skfuzzy.control as ctrl

rules = [
    ctrl.Rule(budget['very_low'] | deadline['very_low'] | complexity['very_high'] | uncertainty['very_high'], risk['very_high']),
    ctrl.Rule(budget['low'] | deadline['low'] | complexity['high'] | uncertainty['high'], risk['high']),
    ctrl.Rule(budget['medium'] & deadline['medium'] & complexity['medium'] & team_experience['medium'], risk['medium']),
    ctrl.Rule(budget['high'] & deadline['high'] & complexity['low'] & team_experience['high'], risk['low']),
    ctrl.Rule(budget['very_high'] & deadline['very_high'] & complexity['very_low'] & team_experience['very_high'], risk['very_low']),
    ctrl.Rule(complexity['high'] & uncertainty['high'] & team_experience['low'], risk['high']),
    ctrl.Rule(deadline['very_low'] & budget['very_high'], risk['medium']),
    ctrl.Rule(deadline['very_high'] & complexity['very_low'] & team_experience['very_high'], risk['very_low']),
    ctrl.Rule(budget['low'] & team_experience['very_low'], risk['very_high']),
    ctrl.Rule(deadline['medium'] & complexity['high'] & team_experience['medium'] & uncertainty['medium'], risk['medium'])
]

risk_ctrl = ctrl.ControlSystem(rules)
risk_simulation = ctrl.ControlSystemSimulation(risk_ctrl)



