from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    # Set the timezone to Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')
    # Get the current time in Moscow
    moscow_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    
    # Return the current time in Moscow as HTML
    return f"<h1>Current Time in Moscow: {moscow_time}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
