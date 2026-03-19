FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for PostgreSQL (if using real DB)
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copy requirements relative to the build context (root)
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend source and the shared common folder
COPY ./backend ./backend
COPY ./common ./common

# Set PYTHONPATH so 'import common' works inside the 'backend' folder
ENV PYTHONPATH=/app

# Move into the backend directory to run the app
WORKDIR /app/backend

EXPOSE 8000

# Run the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]