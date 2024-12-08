from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI,HTTPException
from models import Gender, Role, User,UpdateUser
app = FastAPI()
db: List[User] = [
    User(
        id=uuid4(),
        first_name="Surya",
        last_name="R",
        gender=Gender.male,
        roles=[Role.admin],
        ),
    User(
        id=uuid4(),
        first_name="Balaji",
        last_name="R",
        gender=Gender.male,
        roles=[Role.user],
        ),
    User(
        id=uuid4(),
        first_name="Logesh",
        last_name="S",
        gender=Gender.male,
        roles=[Role.user],
        ),
]

@app.get("/")
def index():
    return {"Message":"Welcome"}

@app.get("/api/v1/users")
def get_users():
   return db
@app.post("/api/v1/users")
def add_users(user:User):
    db.append(user)
    return {"id":user.id}
@app.put("/api/v1/users/{user_id}")  
def update_user(user_update: UpdateUser, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.gender is not None:
                user.gender = user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"message": "User updated successfully", "user": user}
    
    raise HTTPException(
        status_code=404,
        detail=f"User with id {user_id} does not exist in the list" 
    )
@app.delete("/api/v1/users/{user_id}")
def delete_user(user_id:UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return {"Message":"Deleted the user successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"User with id {user_id} does not exist in the list" 
    )