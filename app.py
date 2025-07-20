from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis service by its service name from docker-compose
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = r.incr('hits')  # Increment a Redis key on every visit
    return f'Hello from Flask! 🔥 Hit count: {count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
