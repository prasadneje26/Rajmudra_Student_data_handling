from fastapi import FastAPI

from app.core.database import engine, Base

from app.models.student_model import Student
from app.models.class_model import Class

Base.metadata.create_all(bind=engine)

app = FastAPI()

from app.routes import student_routes
app.include_router(student_routes.router)

from app.routes import academic_routes

app = FastAPI(title="Student Data Handling")

app.include_router(academic_routes.router)
from app.routes import student_routes

app.include_router(student_routes.router)
