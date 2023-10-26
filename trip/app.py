from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plan', methods=['POST'])
def plan_trip():
    destination = request.form['destination']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    # Add trip planning logic here
    return f'Trip planned to {destination} from {start_date} to {end_date}'

if __name__ == '__main__':
    app.run(debug=True)
