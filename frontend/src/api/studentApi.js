import axiosInstance from "./axiosInstance";

/**
 * 🎓 Student API Service
 * Fully scalable • Auth-ready • Production ready
 */

const handleResponse = (response) => response.data;

const handleError = (error) => {
  const message =
    error?.response?.data?.detail ||
    error?.response?.data?.message ||
    "Something went wrong";

  throw new Error(message);
};

export const studentApi = {
  /**
   * ➕ Create Student
   */
  create: async (data) => {
    try {
      const res = await axiosInstance.post("/students/", data);
      return handleResponse(res);
    } catch (error) {
      handleError(error);
    }
  },

  /**
   * 📖 Get Single Student
   */
  getById: async (id) => {
    try {
      const res = await axiosInstance.get(`/students/${id}`);
      return handleResponse(res);
    } catch (error) {
      handleError(error);
    }
  },

  /**
   * ✏ Update Student
   */
  update: async (id, data) => {
    try {
      const res = await axiosInstance.put(`/students/${id}`, data);
      return handleResponse(res);
    } catch (error) {
      handleError(error);
    }
  },

  /**
   * ❌ Delete Student
   */
  delete: async (id) => {
    try {
      const res = await axiosInstance.delete(`/students/${id}`);
      return handleResponse(res);
    } catch (error) {
      handleError(error);
    }
  },

  /**
   * 📚 Get Students (with pagination + search)
   */
  getAll: async ({ page = 1, limit = 10, search = "", classId }) => {
    try {
      const res = await axiosInstance.get("/students/", {
        params: {
          page,
          limit,
          search,
          class_id: classId,
        },
      });
      return handleResponse(res);
    } catch (error) {
      handleError(error);
    }
  },

  /**
   * 📚 Get Students by Class
   */
  getByClass: async (classId) => {
    try {
      const res = await axiosInstance.get(`/students/class/${classId}`);
      return handleResponse(res);
    } catch (error) {
      handleError(error);
    }
  },
};