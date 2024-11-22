from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Define the visits file path
VISITS_FILE = 'visits'

# Ensure the visits file exists
if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, 'w') as f:
        f.write('0')

def get_visits():
    """Read visit count from the file."""
    with open(VISITS_FILE, 'r') as f:
        return int(f.read().strip())

def increment_visits():
    """Increment and write visit count to the file."""
    visits = get_visits() + 1
    with open(VISITS_FILE, 'w') as f:
        f.write(str(visits))
    return visits

@app.route('/')
def home():
    """Display current time in Moscow."""
    moscow_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({"Moscow Time": moscow_time})

@app.route('/visits')
def visits():
    """Display the visit count."""
    increment_visits()
    visits = get_visits()
    return jsonify({"Visit Count": visits})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)