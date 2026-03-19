from fastapi import FastAPI
import uvicorn
# In a real setup, we'd import Task from common.models
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str

tasks_db = []

@app.get("/tasks")
def get_tasks():
    return tasks_db

@app.post("/tasks")
def add_task(task: Task):
    tasks_db.append(task)
    return {"message": "Task added successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)