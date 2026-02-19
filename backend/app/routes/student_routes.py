from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services import student_service

router = APIRouter(prefix="/students", tags=["Students"])

@router.get("/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    return student_service.get_student_by_id(db, student_id)
