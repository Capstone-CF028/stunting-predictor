console.log("Form Prediksi Page is running...");

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("predictionForm");
  const loading = document.getElementById("loading");

  form.onsubmit = async function (e) {
    e.preventDefault();

    loading.classList.remove("d-none");

    const gender = parseInt(document.getElementById("gender").value);
    const age = parseInt(document.getElementById("age").value);
    const height = parseFloat(document.getElementById("height").value);
    const weight = parseFloat(document.getElementById("weight").value);

    if (isNaN(gender) || isNaN(age) || isNaN(height) || isNaN(weight)) {
      alert("Mohon lengkapi semua field dengan benar.");
      loading.classList.add("d-none");
      return;
    }

    const inputData = [[gender, age, height, weight]];

    try {
      const response = await axios.post("https://render-production-ce00.up.railway.app/predict-and-recommend", {
        data: inputData
      });

      const result = response.data;

      // Simpan hasil ke localStorage
      localStorage.setItem("stunting", result.stunting);
      localStorage.setItem("wasting", result.wasting);
      localStorage.setItem("articles", JSON.stringify(result.articles));

      // Redirect ke hasil
      window.location.href = "hasil.html";
    } catch (error) {
      alert("Terjadi kesalahan saat melakukan prediksi.");
      console.error("Prediction error:", error);
    } finally {
      loading.classList.add("d-none");
    }
  };
});
