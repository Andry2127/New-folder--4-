from fastapi import FastAPI, Query
import uvicorn

import db 

app = FastAPI()


@app.get("/")
async def index():
    return dict(msg="Welcome to our system")


@app.post("/add_data/")
async def add_data(name: str = Query(), data: str = Query()):
    if name not in db.data:
        db.data.update({name: data})
        return dict(msg="Data is succesfully saved")
    else:
        return dict(msg="Data is already exist")


@app.get("/data/")
async def get_data():
    return dict(data=db.data, msg="All the data is shown here")


if __name__ == "__main__":
    uvicorn.run("main:app")


    









