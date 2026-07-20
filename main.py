from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FlyRank!"}


@app.get("/health")
def health():
    return {"status": "!WOW"}

tasks = [
    {
        "id": 1,
        "title": "Do SQL LeetCode",
        "completed": False
    },
    {
        "id": 2,
        "title": "Learn Pandas",
        "completed": False
    }
]


class Task(BaseModel):
    title: str
    completed: bool


@app.get("/tasks")
def get_tasks():
    return tasks



@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks")
def create_task(task: Task):

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)

    return new_task


@app.put("/tasks/{id}")
def update_task(id: int, updated_task: Task):

    for task in tasks:
        if task["id"] == id:
            task["title"] = updated_task.title
            task["completed"] = updated_task.completed
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{id}")
def delete_task(id: int):

    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")