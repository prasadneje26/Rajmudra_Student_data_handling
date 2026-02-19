from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class ParentSchema(BaseModel):
    father_name: Optional[str]
    father_contact: Optional[str]
    father_occupation: Optional[str]
    mother_name: Optional[str]
    mother_contact: Optional[str]
    mother_occupation: Optional[str]
    guardian_name: Optional[str]
    emergency_contact: Optional[str]


class AcademicSchema(BaseModel):
    section: Optional[str]
    roll_number: Optional[str]
    previous_school: Optional[str]
    tc_number: Optional[str]


class FinancialSchema(BaseModel):
    fee_category: Optional[str]
    scholarship_details: Optional[str]
    payment_status: Optional[str]
    payment_history: Optional[str]


class PerformanceSchema(BaseModel):
    attendance_percentage: Optional[float]
    exam_marks: Optional[str]
    grades: Optional[str]
    teacher_remarks: Optional[str]


class StudentCreate(BaseModel):
    name: str
    gender: str
    dob: date
    school_name: str
    mobile: str
    email: EmailStr

    house_no: Optional[str]
    street: Optional[str]
    city: Optional[str]
    district: Optional[str]
    state: Optional[str]
    pin_code: Optional[str]

    admission_date: Optional[date]
    academic_year: Optional[str]
    current_status: Optional[str]

    class_id: int

    parent_details: Optional[ParentSchema]
    academic_details: Optional[AcademicSchema]
    financial_details: Optional[FinancialSchema]
    performance_details: Optional[PerformanceSchema]