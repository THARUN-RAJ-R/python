from fastapi import FastAPI
from typing import  Optional

app = FastAPI()

@app.get("/")
def index():
    return "hi" 

@app.get("/about")
def about():
    return {"data": "about page"}

@app.get("/about/{id}")
def dec(id:int,limit:int=10,l:int=20,):
    return {"data": id,"limit":limit,"l":l}