import requests
import psycopg2
import os
import time

def test_system():
    """
    Smoke test to verify that the Database, Backend, and Frontend 
    containers are reachable within the Docker network.
    """
    print("====================================================")
    print("🔍 STARTING SYSTEM INTEGRATION TEST")
    print("====================================================\n")

    # 1. Test Database Connectivity
    print("Step 1: Checking Database connectivity ('db' service)...")
    try:
        conn = psycopg2.connect(
            host="db",
            database=os.getenv("POSTGRES_DB", "task_db"),
            user=os.getenv("POSTGRES_USER", "user"),
            password=os.getenv("POSTGRES_PASSWORD", "pass"),
            connect_timeout=5
        )
        print("✅ SUCCESS: Network connection to PostgreSQL established.\n")
        conn.close()
    except Exception as e:
        print("❌ FAILED: Database unreachable. Ensure 'db' service is running.")
        print(f"   Error: {e}\n")

    # 2. Test Backend API
    print("Step 2: Checking Backend API responsiveness ('backend' service)...")
    try:
        response = requests.get("http://backend:8000/docs", timeout=5)
        if response.status_code == 200:
            print("✅ SUCCESS: Backend API is up and serving documentation.\n")
        else:
            print(f"⚠️  WARNING: Backend reached but returned status {response.status_code}.\n")
    except Exception as e:
        print("❌ FAILED: Backend unreachable. Check if Uvicorn is running on 0.0.0.0.")
        print(f"   Error: {e}\n")

    # 3. Test Frontend UI
    print("Step 3: Checking Frontend UI availability ('frontend' service)...")
    try:
        response = requests.get("http://frontend:8501", timeout=5)
        if response.status_code == 200:
            print("✅ SUCCESS: Frontend Streamlit UI is active.\n")
    except Exception as e:
        print("❌ FAILED: Frontend unreachable. Check Streamlit port 8501.")
        print(f"   Error: {e}\n")

    print("====================================================")
    print("🏁 INTEGRATION TEST COMPLETE")
    print("====================================================")

if __name__ == "__main__":
    test_system()