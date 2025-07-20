FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose Flask's port
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
