# Use a small Python image
FROM python:3.12-slim

# Inside-container working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Tell Flask to listen on all interfaces in the container
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Expose the port Flask will run on
EXPOSE 5000

# Start the app
CMD ["flask", "run"]
