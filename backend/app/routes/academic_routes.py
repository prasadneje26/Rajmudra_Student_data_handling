from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.academic_schema import AcademicCreate, AcademicUpdate, AcademicResponse
from app.services.academic_service import (
    create_academic,
    get_academic_by_student,
    update_academic,
    delete_academic,
    list_all_academics
)
from app.core.database import get_db

router = APIRouter(
    prefix="/academics",
    tags=["Academics"]
)

# Create new academic record
@router.post("/", response_model=AcademicResponse)
def create_academic_record(academic_in: AcademicCreate, db: Session = Depends(get_db)):
    existing = get_academic_by_student(db, academic_in.student_id)
    if existing:
        raise HTTPException(status_code=400, detail="Academic record already exists for this student")
    return create_academic(db, academic_in)

# Get academic record by student_id
@router.get("/{student_id}", response_model=AcademicResponse)
def read_academic(student_id: int, db: Session = Depends(get_db)):
    record = get_academic_by_student(db, student_id)
    if not record:
        raise HTTPException(status_code=404, detail="Academic record not found")
    return record

# Update academic record
@router.put("/{student_id}", response_model=AcademicResponse)
def update_academic_record(student_id: int, academic_in: AcademicUpdate, db: Session = Depends(get_db)):
    record = update_academic(db, student_id, academic_in)
    if not record:
        raise HTTPException(status_code=404, detail="Academic record not found")
    return record

# Delete academic record
@router.delete("/{student_id}")
def delete_academic_record(student_id: int, db: Session = Depends(get_db)):
    success = delete_academic(db, student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Academic record not found")
    return {"detail": "Academic record deleted successfully"}

# List all academic records
@router.get("/", response_model=List[AcademicResponse])
def list_academics(db: Session = Depends(get_db)):
    return list_all_academics(db)
