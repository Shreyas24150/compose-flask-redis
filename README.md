**🚀 Flask + Redis App with Docker Compose**

This repository provides a minimal Flask application that tracks how many times a specific route is requested. The app uses Redis to persist the count and is deployed inside a fully containerized environment with Docker Compose.

**📦 Stack**

Flask – A lightweight web framework for Python
Redis – A fast in-memory key-value store (acts as the counter)
Docker – The standard for containerizing applications
Docker Compose – A tool for managing multi-container setups

**🧱 Project Structure**

.  
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md  

**RUN IT 🚀**

cd compose-flask-redis
docker-compose up --build

**✅ Test the App**

http://localhost:5000

o/p : **Hello from Flask! 🔥 Hit count: 1**

Refresh the page, and the hit count will increase each time - Redis is storing the count.
