from flask import Flask, request, jsonify, render_template
from rules import risk_simulation

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate_risk():
    try:
        data = request.json
        risk_simulation.input['budget'] = data['budget']
        risk_simulation.input['deadline'] = data['deadline']
        risk_simulation.input['complexity'] = data['complexity']
        risk_simulation.input['team_experience'] = data['team_experience']
        risk_simulation.input['uncertainty'] = data['uncertainty']
        
        risk_simulation.compute()
        risk_level = risk_simulation.output['risk']
        
        return jsonify({'risk': round(risk_level, 2)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)



