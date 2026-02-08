# 🚀 Team Tasker: Modular Full-Stack Docker Workshop

Welcome to the Team Tasker project! This is a modular Task Management System designed to demonstrate how **microservices** communicate and how **Docker** provides a unified development environment.

---

## 🏗️ Project Architecture
The project is split into four distinct modules:
* **`db/`**: Database schema initialization scripts.
* **`backend/`**: FastAPI REST API (The "Brain").
* **`frontend/`**: Streamlit Web UI (The "Face").
* **`common/`**: Shared Pydantic models used by both Backend and Frontend.



---

## 🛠️ Quick Start (The "One-Click" Setup)

1.  **Open in VS Code:** Open the `team-tasker` root folder.
2.  **Initialize Dev Container:**
    * When prompted, click **"Reopen in Container"**.
    * *If no prompt appears:* Press `F1`, type `Dev Containers: Rebuild and Reopen in Container`, and hit Enter.
3.  **Launch the System:** Once the container is ready and your terminal says `root@...:/app`, run:
    ```bash
    docker compose up --build
    ```

---

## 🔗 Access Points
Once the containers are running, access the services via your Windows browser:

* **Frontend UI:** [http://localhost:8501](http://localhost:8501)
* **Backend API Docs (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Database:** `localhost:5432` (User: `user` | Pass: `pass`)

---

## 👥 Member Roles & Responsibilities

### **Member 1: The Data Architect (`/db`)**
* **Focus:** Database reliability and schema.
* **Task:** Ensure `init_db.py` creates the necessary tables and handle connection retries.
* **Key File:** `db/init_db.py`

### **Member 2: The Logic Lead (`/backend`)**
* **Focus:** API development and DB integration.
* **Task:** Connect FastAPI to the Postgres service using the `DATABASE_URL` environment variable.
* **Key File:** `backend/main.py`

### **Member 3: The UI Specialist (`/frontend`)**
* **Focus:** User experience and API consumption.
* **Task:** Use the `requests` library to fetch/send data to `http://backend:8000`.
* **Key File:** `frontend/app.py`

---

## 💡 Important Technical Notes

### **1. Build Context**
We build from the **root directory**. This allows both the Frontend and Backend to "see" the `common/` folder during the Docker build process.

### **2. Internal Networking**
Inside the Docker network, containers talk to each other by **service name**, not `localhost`:
* The Frontend calls: `http://backend:8000`
* The Backend calls: `db:5432`

### **3. Hot Reloading**
We use **Docker Volumes** in `docker-compose.yml`. You can edit code in VS Code, and the change will reflect inside the running container immediately without a rebuild.

---

## 🛑 Useful Commands
* `docker compose up --build`: Build and start all services.
* `docker compose up --d`: Start all services in detached mode.
* `docker compose down`: Stop and remove all containers and networks.
* `docker compose logs -f [service]`: Tail logs for a specific service (e.g., `backend`).
* `docker compose ps`: Check the health status of all services.