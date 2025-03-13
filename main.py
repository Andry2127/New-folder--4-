from fastapi import FastAPI, Query
import uvicorn

import db 

app = FastAPI()
users = []

@app.get("/get_users/")
def get_users():
    return {"users": users}


@app.post("/add_user/")
def add_data(name: str = Query()):
    if name not in db.data:
        users.append(name)
        return dict(msg="Data is succesfully saved")


@app.delete("/delete_user/")
def del_data(name: str = Query()):
    if name not in users:
        return dict(msg="name does not exists")
    users.remove(name)
    return dict(msg="name is deleted")


if __name__ == "__main__":
    uvicorn.run("main:app")



    









