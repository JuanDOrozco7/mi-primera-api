from fastapi import FastAPI, APIRouter, Query, HTTPException
from model.schemas import Student, StudentCreate

app = FastAPI(title = "Mi primera API")

api_router = APIRouter()

students = [
    {
        "id": 1,
        "nombre": "Juan David",
        "codigo": "2019214012",
        "edad": 23,
        "semestre": 6
    },
    {
        "id": 2,
        "nombre": "Johan",
        "codigo": "2019214098",
        "edad": 20,
        "semestre": 6
    },
    {
        "id": 3,
        "nombre": "Guillermo",
        "codigo": "2019114001",
        "edad": 22,
        "semestre": 7
    },
    {
        "id": 4,
        "nombre": "David",
        "codigo": "2017214042",
        "edad": 27,
        "semestre": 9
    }
]

@api_router.get("/students/")
def student_list() -> dict:
    return students

@api_router.get("/student/{student_id}", status_code = 200, response_model = Student)
def fetch_student(*, student_id: int) -> any:
    result = [student for student in students if student["id"] == student_id]
    if not result:
        raise HTTPException(status_code = 404, details = " Student with id {student_id} not found")
    
    return result[0]

#Query parameters
# http://localhost:8000/students/?semestre = 6
@api_router.get("/students/search/")
def search_students_by_semestre(*, semestre: int = Query(...)) -> dict:
    results = filter(lambda student: semestre == student["semestre"], students)
    return list(results)

@api_router.post("/students/", status_code = 201, response_model = Student)
def create_student(*, student_in: StudentCreate) -> dict:
    new_entry_id = len(students) + 1
    student_entry = Student(
        id = new_entry_id,
        nombre = student_in.nombre,
        codigo = student_in.codigo,
        edad = student_in.edad,
        semestre = student_in.semestre
    )
    students.append(student_entry.dict())
    return student_entry

app.include_router(api_router)