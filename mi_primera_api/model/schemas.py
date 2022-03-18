from pydantic import BaseModel

class Student(BaseModel):
    id:int
    nombre:str
    codigo:str
    edad:int
    semestre:int

class StudentCreate(BaseModel):
    nombre:str
    codigo:str
    edad:int
    semestre:int