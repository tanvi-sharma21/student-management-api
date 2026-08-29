from fastapi import FastAPI , HTTPException
from pydantic import BaseModel , Field
app =FastAPI()

students = {
    101: {
        "name": "Aditi",
        "age": 20,
        "email": "aditi@gmail.com",
        "course": "CSE",
        "year": 3,
        "semester": 5,
        "phone": "9876543210",
        "city": "Delhi",
        "attendance": 82.5,
        "cgpa": 8.4,
        "status": "active"
    },

    102: {
        "name": "Rahul",
        "age": 21,
        "email": "rahul@gmail.com",
        "course": "IT",
        "year": 3,
        "semester": 5,
        "phone": "9876543211",
        "city": "Noida",
        "attendance": 74.0,
        "cgpa": 7.8,
        "status": "active"
    },

    103: {
        "name": "Priya",
        "age": 20,
        "email": "priya@gmail.com",
        "course": "CSE",
        "year": 2,
        "semester": 4,
        "phone": "9876543212",
        "city": "Ghaziabad",
        "attendance": 91.0,
        "cgpa": 8.9,
        "status": "active"
    },

    104: {
        "name": "Arjun",
        "age": 22,
        "email": "arjun@gmail.com",
        "course": "ECE",
        "year": 4,
        "semester": 7,
        "phone": "9876543213",
        "city": "Meerut",
        "attendance": 68.0,
        "cgpa": 7.2,
        "status": "active"
    },

    105: {
        "name": "Neha",
        "age": 20,
        "email": "neha@gmail.com",
        "course": "CSE",
        "year": 3,
        "semester": 5,
        "phone": "9876543214",
        "city": "Delhi",
        "attendance": 95.0,
        "cgpa": 9.1,
        "status": "active"
    },

    106: {
        "name": "Karan",
        "age": 21,
        "email": "karan@gmail.com",
        "course": "IT",
        "year": 3,
        "semester": 5,
        "phone": "9876543215",
        "city": "Faridabad",
        "attendance": 72.5,
        "cgpa": 7.5,
        "status": "inactive"
    }
}

class Student(BaseModel):
    
     name : str
     age :int
     email:str
     course : str
     year : int
     semester : int
     phone : int
     city:str
     attendance : int
     cgpa:int
     status : str






@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id:int):
    if student_id in students:
        return students[student_id]
    raise HTTPException (status_code=404,detail="student not found")

@app.post("/student")
def create_student(student:Student):
         return students
# put used to update the context 
@app.put("/student/{student_id}")
def update_student(
    student_id: int,
    name: str,
    email: str,
    semester: int,
    phone: str,
    attendance: float,
    cgpa: float,
    status: str
):
    if student_id in students:

        students[student_id]["name"] = name
        students[student_id]["email"] = email
        students[student_id]["semester"] = semester
        students[student_id]["phone"] = phone
        students[student_id]["attendance"] = attendance
        students[student_id]["cgpa"] = cgpa
        students[student_id]["status"] = status

        return {
            "message": "Student updated successfully",
            "student": students[student_id]
        }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
    
@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    
    if student_id in students:
        del students[student_id]
        return{"message": "student deleted successfully"}
    raise HTTPException(status_code = 404 ,detail= "student not found") 
@app.get("/students/search")
def search_student(student_name:str):
 for student in students.values():
    if student["name"] == student_name:
        return student
@app.get("/students")
def filter_students(
    course: str = None,
    year: int = None,
    status: str = None
):
    result=[]
    for student in student.values:
        if course and student["course"]!= course:
            continue
        if year and student["year"]!= year:
            continue
        if status and student["status"]!= status:
            continue
        result.append(student)
        return result
    
@app.get("student/low_attendence")
def low_attendance_students():
    result=[]
    
    for student in student.values():
      if student["attendance"]<75:
        result.append(student)
    return result 
@app.get("/students/top")
def top_students():

    sorted_students = sorted(
        students.values(),
        key=lambda student: student["cgpa"],
        reverse=True
    )

    return sorted_students[:3]

@app.get("/students/stats")
def student_stats():

    total_students = len(students)

    total_cgpa = 0
    total_attendance = 0

    for student in students.values():
        total_cgpa = total_cgpa + student["cgpa"]
        total_attendance = total_attendance + student["attendance"]

    average_cgpa = total_cgpa / total_students
    average_attendance = total_attendance / total_students

    return {
        "total_students": total_students,
        "average_cgpa": average_cgpa,
        "average_attendance": average_attendance
    }