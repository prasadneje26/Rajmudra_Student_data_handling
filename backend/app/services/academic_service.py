from sqlalchemy.orm import Session
from app.models.academic_model import Academic
from app.schemas.academic_schema import AcademicCreate, AcademicUpdate, AcademicResponse
from app.utils.grade_calculator import calculate_grade

def create_academic(db: Session, academic_in: AcademicCreate) -> Academic:
    # Calculate attendance percentage
    attendance_percentage = 0.0
    if academic_in.total_classes > 0:
        attendance_percentage = (academic_in.attended_classes / academic_in.total_classes) * 100

    # Calculate total marks and percentage
    total_marks = academic_in.subject1_marks + academic_in.subject2_marks + academic_in.subject3_marks
    percentage = total_marks / 3  # assuming 3 subjects

    # Calculate grade and result
    grade_result = calculate_grade(percentage)
    grade = grade_result["grade"]
    result = grade_result["result"]

    # Create Academic object
    academic_obj = Academic(
        student_id=academic_in.student_id,
        total_classes=academic_in.total_classes,
        attended_classes=academic_in.attended_classes,
        attendance_percentage=attendance_percentage,
        subject1_marks=academic_in.subject1_marks,
        subject2_marks=academic_in.subject2_marks,
        subject3_marks=academic_in.subject3_marks,
        total_marks=total_marks,
        percentage=percentage,
        grade=grade,
        result=result
    )

    db.add(academic_obj)
    db.commit()
    db.refresh(academic_obj)
    return academic_obj

def get_academic_by_student(db: Session, student_id: int) -> Academic:
    return db.query(Academic).filter(Academic.student_id == student_id).first()

def update_academic(db: Session, student_id: int, academic_in: AcademicUpdate) -> Academic:
    academic_obj = db.query(Academic).filter(Academic.student_id == student_id).first()
    if not academic_obj:
        return None

    # Update fields
    academic_obj.total_classes = academic_in.total_classes
    academic_obj.attended_classes = academic_in.attended_classes
    academic_obj.subject1_marks = academic_in.subject1_marks
    academic_obj.subject2_marks = academic_in.subject2_marks
    academic_obj.subject3_marks = academic_in.subject3_marks

    # Recalculate
    academic_obj.attendance_percentage = (academic_obj.attended_classes / academic_obj.total_classes * 100
                                          if academic_obj.total_classes > 0 else 0.0)
    academic_obj.total_marks = (academic_obj.subject1_marks +
                                academic_obj.subject2_marks +
                                academic_obj.subject3_marks)
    academic_obj.percentage = academic_obj.total_marks / 3  # 3 subjects
    grade_result = calculate_grade(academic_obj.percentage)
    academic_obj.grade = grade_result["grade"]
    academic_obj.result = grade_result["result"]

    db.commit()
    db.refresh(academic_obj)
    return academic_obj

def delete_academic(db: Session, student_id: int) -> bool:
    academic_obj = db.query(Academic).filter(Academic.student_id == student_id).first()
    if not academic_obj:
        return False
    db.delete(academic_obj)
    db.commit()
    return True

def list_all_academics(db: Session):
    return db.query(Academic).all()
