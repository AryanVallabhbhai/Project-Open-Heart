from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/live_condition')
def live_condition():
    return render_template('live_condition.html')

@app.route('/medical_record')
def medical_record():
    return render_template('medical_record.html')

@app.route('/patients')
def patients():
    return render_template('patients.html')

@app.route('/patient_status')
def patient_status():
    return render_template('patient_status.html')

if __name__ == "__main__":
    app.run(debug=True)