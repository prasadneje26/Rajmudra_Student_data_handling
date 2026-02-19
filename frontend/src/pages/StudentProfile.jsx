import React, { useState } from "react";
import AcademicSection from "./AcademicSection";

const StudentProfile = ({ studentId }) => {
  const [activeTab, setActiveTab] = useState("personal");

  return (
    <div>
      <button onClick={() => setActiveTab("personal")}>Personal</button>
      <button onClick={() => setActiveTab("academic")}>Academic</button>

      {activeTab === "personal" && <div>Personal Info Here...</div>}
      {activeTab === "academic" && <AcademicSection studentId={studentId} />}
    </div>
  );
};

export default StudentProfile;
