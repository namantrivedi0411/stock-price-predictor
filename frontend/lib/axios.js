import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:5000/predict/",
});

export default api;