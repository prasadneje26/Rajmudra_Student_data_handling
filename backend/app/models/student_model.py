from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)
    gender = Column(String(10), nullable=False)
    dob = Column(Date, nullable=False)

    phone = Column(String(15), nullable=False)
    school = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    address = Column(String(255))

    parent_name = Column(String(100), nullable=False)
    parent_phone = Column(String(15), nullable=False)

    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)

    class_relation = relationship("Class", back_populates="students")
