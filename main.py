from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import User
from models import Gender, Role

app = FastAPI()


db: List[User] = [
    User(
        id="bf5fa37a-9d1f-4ac1-a100-d66d07429a9b",
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id="120aa3aa-2496-48da-99f6-9cd13fec2f41",
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
async def root():
    return {"Hello": "Fadhil"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return "user successfully deleted"
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )