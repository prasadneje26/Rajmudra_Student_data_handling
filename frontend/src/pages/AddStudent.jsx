import { useEffect, useState } from "react";
import { createStudent } from "../api/studentApi";
import axios from "axios";
import StudentForm from "../components/StudentForm";
import { useNavigate } from "react-router-dom";

const AddStudent = () => {

  const [classes, setClasses] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get("http://localhost:8000/classes")
      .then((res) => setClasses(res.data));
  }, []);

  const handleSubmit = async (data) => {
    try {
      await createStudent(data);
      alert("Student Added Successfully");
      navigate("/");
    } catch (error) {
      alert("Error adding student");
    }
  };

  return (
    <div>
      <h2>Add Student</h2>
      <StudentForm classes={classes} onSubmit={handleSubmit} />
    </div>
  );
};

export default AddStudent;