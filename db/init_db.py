import psycopg2
import os
import time

def initialize_db():
    # Get credentials from environment variables (set in docker-compose)
    dbname = os.getenv("POSTGRES_DB", "task_db")
    user = os.getenv("POSTGRES_USER", "user")
    password = os.getenv("POSTGRES_PASSWORD", "pass")
    host = os.getenv("DB_HOST", "db")

    print("Connecting to database...")
    
    # Retry logic because the DB container might take a few seconds to boot
    for i in range(10):
        try:
            conn = psycopg2.connect(
                dbname=dbname, user=user, password=password, host=host
            )
            cursor = conn.cursor()
            
            # Create the tasks table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'pending'
                );
            """)
            
            conn.commit()
            cursor.close()
            conn.close()
            print("Successfully initialized the database schema!")
            return
        except Exception as e:
            print(f"Database not ready yet (attempt {i+1}/10)...")
            time.sleep(2)

if __name__ == "__main__":
    initialize_db()