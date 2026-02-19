from fastapi import FastAPI
from app.routes import academic_routes

app = FastAPI(title="Student Data Handling")

app.include_router(academic_routes.router)
