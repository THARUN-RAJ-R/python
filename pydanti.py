from pydantic import BaseModel,field_validator
from main import *

class req(BaseModel):
    name:str
    age:int
    year:int

    
    @field_validator("age")
    def age_check(cls,value):
        if value<=0:
            raise ValueError("age must be greater than 0")
        return value

student1=req(**student[1])

print(student1)
