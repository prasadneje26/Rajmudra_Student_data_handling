from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas.student_schema import (
    StudentCreate,
    StudentResponse,
    StudentUpdate,
)
from app.services import student_service
from app.core.security import get_current_user  # 🔐 Auth dependency

router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


# ➕ Create Student
@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_student_api(
    student: StudentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),  # 🔐 Protected
):
    return student_service.create_student(db, student)


# 📚 Get All Students (Pagination + Search)
@router.get("/", response_model=List[StudentResponse])
def get_students(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=100),
    search: Optional[str] = None,
    class_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return student_service.get_students(
        db=db,
        page=page,
        limit=limit,
        search=search,
        class_id=class_id,
    )


# 📚 Get Students by Class
@router.get("/class/{class_id}", response_model=List[StudentResponse])
def get_students_by_class(
    class_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return student_service.get_students_by_class_id(db, class_id)


# 📖 Get Single Student
@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return student_service.get_student_by_id(db, student_id)


# ✏ Update Student
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return student_service.update_student(db, student_id, student)


# ❌ Delete Student
@router.delete(
    "/{student_id}",
    status_code=status.HTTP_200_OK,
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    student_service.delete_student(db, student_id)
    return {"message": "Student deleted successfully"}