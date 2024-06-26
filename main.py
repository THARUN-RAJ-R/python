from fastapi import FastAPI
from typing import  Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return "hi" 

@app.get("/about")
def about():
    return {"data": "about page"}

# {id} is path parameter
@app.get("/about/{id}")
#limit and l are query parameter
#doubt what is use of optional
def dec(id:int,limit:int=None,l:Optional[int]=76):
    return {"data": id,"limit":limit,"l":l}

#request body
class req(BaseModel):
    name:str
    age:int
    phone:Optional[int]

@app.post("/create")
def create(blog:req):
    return blog