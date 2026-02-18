from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    # Basic Details
    name = Column(String(100), nullable=False)
    gender = Column(String(10), nullable=False)
    dob = Column(Date, nullable=False)
    school_name = Column(String(100), nullable=False)

    mobile = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    # Address
    house_no = Column(String(50))
    street = Column(String(100))
    city = Column(String(100))
    district = Column(String(100))
    state = Column(String(100))
    pin_code = Column(String(10))

    # Admission
    admission_date = Column(Date)
    academic_year = Column(String(20))
    current_status = Column(String(20), default="Active")

    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)

    class_relation = relationship("Class", back_populates="students")

    # Relationships
    parent_details = relationship("ParentDetails", back_populates="student", uselist=False)
    academic_details = relationship("AcademicDetails", back_populates="student", uselist=False)
    financial_details = relationship("FinancialDetails", back_populates="student", uselist=False)
    performance_details = relationship("PerformanceDetails", back_populates="student", uselist=False)


    academic = relationship("Academic", back_populates="student", uselist=False)


uselist=False → ensures 1:1 relationship (1 student → 1 academic record).