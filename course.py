from fastapi import APIRouter
from model import Course
import json

course_router = APIRouter()


def load_courses():
    with open("courses.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_courses(data):
    with open("courses.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@course_router.get("/courses")
async def get_courses() -> list:
    return load_courses()

@course_router.post("/courses")
async def add_course(course: Course) -> dict:
    courses = load_courses()
    courses.append(course.dict())
    save_courses(courses)
    return {
        "msg": "course added success"
    }