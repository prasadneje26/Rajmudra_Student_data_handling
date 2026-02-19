from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Academic(Base):
    __tablename__ = "academics"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), unique=True, nullable=False)
    
    # Attendance
    total_classes = Column(Integer, nullable=False, default=0)
    attended_classes = Column(Integer, nullable=False, default=0)
    attendance_percentage = Column(Float, nullable=False, default=0.0)
    
    # Marks
    subject1_marks = Column(Float, nullable=False, default=0.0)
    subject2_marks = Column(Float, nullable=False, default=0.0)
    subject3_marks = Column(Float, nullable=False, default=0.0)
    total_marks = Column(Float, nullable=False, default=0.0)
    percentage = Column(Float, nullable=False, default=0.0)
    
    # Grade & Result
    grade = Column(String(5), nullable=True)
    result = Column(String(10), nullable=True)  # Pass / Fail

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship with Student
    student = relationship("Student", back_populates="academic")
