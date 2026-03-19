FROM python:3.11-slim

WORKDIR /app

# Copy requirements relative to the build context (root)
COPY frontend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the frontend source and the shared common folder
COPY ./frontend ./frontend
COPY ./common ./common

# Set PYTHONPATH so 'import common' works inside the 'frontend' folder
ENV PYTHONPATH=/app

# Move into the frontend directory to run the app
WORKDIR /app/frontend

EXPOSE 8501

# Run Streamlit
# --server.address=0.0.0.0 is critical for WSL/Docker networking
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]