import axios from "axios";

const BASE_URL = "http://localhost:8000/academics";

export const createAcademic = async (data) => {
  const res = await axios.post(`${BASE_URL}/`, data);
  return res.data;
};

export const getAcademic = async (studentId) => {
  const res = await axios.get(`${BASE_URL}/${studentId}`);
  return res.data;
};

export const updateAcademic = async (studentId, data) => {
  const res = await axios.put(`${BASE_URL}/${studentId}`, data);
  return res.data;
};

export const deleteAcademic = async (studentId) => {
  const res = await axios.delete(`${BASE_URL}/${studentId}`);
  return res.data;
};

export const listAcademics = async () => {
  const res = await axios.get(BASE_URL);
  return res.data;
};
