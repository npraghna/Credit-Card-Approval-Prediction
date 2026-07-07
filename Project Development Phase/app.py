import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict_page():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        # 
        income_val = float(request.form['Income_Total'])
        age_val = int(request.form['Age'])
        
        # 
        if income_val > 50000 and age_val >= 25:
            status = "Approved"
        else:
            status = "Rejected"
            
        return render_template('result.html', prediction_text=status, prediction=status)

if __name__ == "__main__":
    app.run(debug=True)