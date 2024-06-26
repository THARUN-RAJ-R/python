from fastapi import FastAPI
from typing import  Optional
from pydantic import BaseModel
student={1:{'name':'john','age':20,'year':2}}

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

#request method
class req(BaseModel):
    name:str
    age:int
    year:Optional[int]

@app.post("/user/{stdid}")
def user(stdid,stud:req):
    student.update({stdid:stud})
    return student


