import React, { useState, useEffect } from "react";
import { getAcademic, updateAcademic } from "../api/academicApi";

const AcademicSection = ({ studentId }) => {
  const [academic, setAcademic] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getAcademic(studentId);
        setAcademic(data);
      } catch (err) {
        setError("Academic data not found");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [studentId]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  const handleUpdate = async () => {
    // Example: update attendance
    const updatedData = {
      ...academic,
      attended_classes: academic.attended_classes + 1
    };
    const updated = await updateAcademic(studentId, updatedData);
    setAcademic(updated);
  };

  return (
    <div>
      <h2>Academic Details</h2>
      <p>Total Classes: {academic.total_classes}</p>
      <p>Attended Classes: {academic.attended_classes}</p>
      <p>Attendance %: {academic.attendance_percentage.toFixed(2)}</p>
      <p>Total Marks: {academic.total_marks}</p>
      <p>Percentage: {academic.percentage.toFixed(2)}</p>
      <p>Grade: {academic.grade}</p>
      <p>Result: {academic.result}</p>

      <button onClick={handleUpdate}>Increment Attendance</button>
    </div>
  );
};

export default AcademicSection;
