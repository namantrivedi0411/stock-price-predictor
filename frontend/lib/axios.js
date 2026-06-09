import axios from "axios";

const api = axios.create({
    baseURL: "https://stock-price-predictor-c30c.onrender.com/predict/",
});

export default api;