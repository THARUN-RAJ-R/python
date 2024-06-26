from fastapi import FastAPI
from typing import  Optional
from pydantic import BaseModel

student={1:{'name':'john','age':20,'year':2},2:{'name':'ram','age':25,'year':3}}

app = FastAPI()


@app.get("/")
def index():
    return "details" 

#get method
# {id} is path parameter
@app.get("/show/{id}")
#limit and l are query parameter
def show(id:int,limit:int=20):
    return f'{student[id]['name']} has limit ={limit}'

#request method
class req(BaseModel):
    name:str
    age:int
    year:Optional[int]

@app.post("/user/{stdid}")
def user(stdid,stud:req):
    student.update({stdid:stud})
    return student


#put method
class updatestd(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    year:Optional[int]=None

@app.put("/show/{stdid}")
def update(stdid:int,updat:updatestd):
    if updat.name is not None:
        student[stdid]['name'] = updat.name
    if updat.age is not None:
        student[stdid]['age'] = updat.age
    if updat.year is not None:
        student[stdid]['year'] = updat.year
    return student


#delete method
@app.delete("/show/{stdid}")
def delete(stdid:int):
    del student[stdid]
    return student
