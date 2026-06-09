import { useState } from "react";
import axios from "axios";
import api from "../lib/axios";

function App() {
  const [ticker, setTicker] = useState("");
  const [prediction, setPrediction] = useState(null);

  const predict = async () => {
    try {
      const res = await api.get(
        `${ticker}`
      );

      setPrediction(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 flex items-center justify-center px-4">
      <div className="bg-slate-800 p-8 rounded-2xl shadow-xl w-full max-w-md">

        <h1 className="text-3xl font-bold text-center text-white mb-6">
          Stock Price Predictor
        </h1>

        <input
          type="text"
          placeholder="Enter Code of Stock"
          value={ticker}
          onChange={(e) => setTicker(e.target.value)}
          className="w-full p-3 rounded-lg bg-slate-700 text-white outline-none"
        />

        <button
          onClick={predict}
          className="w-full mt-4 bg-green-500 hover:bg-green-600 text-white py-3 rounded-lg font-semibold"
        >
          Predict
        </button>

        {prediction && (
          <div className="mt-6 bg-slate-700 rounded-lg p-4">
            <h2 className="text-xl text-white font-semibold">
              {prediction.ticker}
            </h2>

            <p className="text-green-400 text-2xl font-bold mt-2">
              ${prediction.predicted_price.toFixed(2)}
            </p>
          </div>
        )}

      </div>
    </div>
  );
}

export default App;