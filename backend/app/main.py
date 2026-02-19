from fastapi import FastAPI
from app.routes import academic_routes

app = FastAPI(title="Student Data Handling")

app.include_router(academic_routes.router)
from app.routes import student_routes

app.include_router(student_routes.router)
