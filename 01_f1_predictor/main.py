import os
from flask import Flask, render_template, request

# This correctly finds the templates folder next to this app.py
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

# 1. CREATE the app first
app = Flask(__name__, template_folder=template_dir)

# 2. DEFINE your data collection
votes = {"Lando": 0, "Oscar": 0}

# 3. USE the app for routes
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    status = None  
    grid = None
    driver = None # <--- ADDED: Initialize driver variable
    
    if request.method == 'POST':
        driver = request.form.get('driver') # <--- ADDED: Capture driver name from dropdown
        grid = request.form.get('grid')
        
        if grid:
            grid_num = int(grid)
            
            # Logic for Prediction AND Status
            if grid_num <= 3:
                prediction = "Podium Contender"
                status = "Great Qualifying! 🚀"
            elif grid_num <= 10:
                prediction = "Points Finish"
                status = "Solid Start. 👍"
            else:
                prediction = "Tough Race Ahead"
                status = "Overtaking needed! ⚠️"

    return render_template('index.html', 
                           prediction=prediction, 
                           status=status, 
                           grid=grid,
                           driver=driver) # <--- ADDED: Pass driver back to HTML

@app.route('/battle')
def battle():
    return render_template('battle.html')

if __name__ == '__main__':
    app.run(debug=True)