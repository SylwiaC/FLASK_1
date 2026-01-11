import os
from flask import Flask, render_template, request

# 1. CREATE the app first
app = Flask(__name__)

# 2. DEFINE your data collection (the votes dictionary)
votes = {"Lando": 0, "Oscar": 0}

# 3. USE the app for routes
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    status = None  
    grid = None
    
    if request.method == 'POST':
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
                           grid=grid)

@app.route('/battle')
def battle():
    return render_template('battle.html')

if __name__ == '__main__':
    app.run(debug=True)