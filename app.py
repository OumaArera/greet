from flask import Flask, render_template, request, jsonify
import redis
import datetime
import os

app = Flask(__name__)
app.redis = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.json.get('name')
    app.redis.set('name', name)
    now = datetime.datetime.now()
    time_of_day = 'morning' if now.hour < 12 else 'afternoon' if now.hour < 18 else 'evening'
    greeting = f"<br>Hello, {name}.<br>"
    greeting += f"I trust you're enjoying your {time_of_day}.<br>"
    greeting += "How may I help you?"
    return jsonify({'greeting': greeting})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
