from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import or_
from app.models.student_model import Student


# ✅ CREATE
def create_student(db: Session, student_data):

    # Check duplicate email or phone
    existing_student = db.query(Student).filter(
        or_(
            Student.email == student_data.email,
            Student.phone == student_data.phone
        )
    ).first()

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Email or Phone already exists"
        )

    new_student = Student(**student_data.dict())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# ✅ GET ALL
def get_students(db, page: int, limit: int, search: str = None, class_id: int = None):
    query = db.query(Student)

    if search:
        query = query.filter(Student.name.ilike(f"%{search}%"))

    if class_id:
        query = query.filter(Student.class_id == class_id)

    offset = (page - 1) * limit

    return query.offset(offset).limit(limit).all()



# ✅ GET ONE
def get_student_by_id(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


# ✅ UPDATE
def update_student(db: Session, student_id: int, update_data):

    student = get_student_by_id(db, student_id)

    # Check unique email/phone if updated
    if update_data.email or update_data.phone:
        existing_student = db.query(Student).filter(
            or_(
                Student.email == update_data.email,
                Student.phone == update_data.phone
            ),
            Student.id != student_id
        ).first()

        if existing_student:
            raise HTTPException(
                status_code=400,
                detail="Email or Phone already exists"
            )

    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)

    return student


# ✅ DELETE
def delete_student(db: Session, student_id: int):

    student = get_student_by_id(db, student_id)

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}