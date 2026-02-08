FROM python:3.11-slim

WORKDIR /app

# Install the PostgreSQL driver
RUN pip install --no-cache-dir psycopg2-binary

# Copy the initialization script
COPY db/init_db.py .

# Run the script
CMD ["python", "init_db.py"]