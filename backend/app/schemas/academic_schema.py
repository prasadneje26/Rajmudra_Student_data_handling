from pydantic import BaseModel, Field, validator
from typing import Optional

# Common schema for shared fields
class AcademicBase(BaseModel):
    total_classes: int = Field(..., ge=0)
    attended_classes: int = Field(..., ge=0)
    subject1_marks: float = Field(..., ge=0)
    subject2_marks: float = Field(..., ge=0)
    subject3_marks: float = Field(..., ge=0)

    @validator("attended_classes")
    def check_attendance(cls, v, values):
        if "total_classes" in values and v > values["total_classes"]:
            raise ValueError("attended_classes cannot exceed total_classes")
        return v

# Schema for creating a new record
class AcademicCreate(AcademicBase):
    student_id: int

# Schema for updating record
class AcademicUpdate(AcademicBase):
    pass

# Schema for response
class AcademicResponse(AcademicBase):
    id: int
    student_id: int
    attendance_percentage: float
    total_marks: float
    percentage: float
    grade: Optional[str]
    result: Optional[str]

    class Config:
        orm_mode = True
