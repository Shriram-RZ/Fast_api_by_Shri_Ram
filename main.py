from fastapi import FastAPI,Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id:int
    name: str
    age: int


users = []

#POST Method
@app.post("/create_user")
async def createUser(user: User):
    users.append(user)
    return {"Status":f"User created successfully"}


#GET Method
@app.get("/users/{id}")
async def getUsers(id:int):
        for user in users:
            if user.id == id:
                return user
            else:
                return {"Message":f"No users found"}

#QUERY PARAMETERS
@app.get("/test")
async def test(q:Annotated[str|None,Query(max_length=10)]):
    result = {"user":f"test user"}
    if q:
        result.update({"q":q})
    return result






