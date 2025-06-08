// src/hasil.js
console.log("Hasil Prediksi Page is running...");

// Ambil data dari localStorage
const stunting = localStorage.getItem("stunting");
const wasting = localStorage.getItem("wasting");
const articles = JSON.parse(localStorage.getItem("articles") || "[]");

console.log("DEBUG → Stunting:", stunting);
console.log("DEBUG → Wasting:", wasting);

// Buat teks informatif untuk stunting
let stuntingText;
switch (stunting?.toLowerCase()) {
  case "normal":
    stuntingText = "✅ Tinggi badan anak tergolong normal sesuai usianya.";
    break;
  case "stunting":
    stuntingText = "❗ Tinggi badan anak berada di bawah normal (stunting ringan).";
    break;
  case "sangat stunting":
    stuntingText = "⚠️ Tinggi badan anak sangat pendek untuk usianya (stunting berat).";
    break;
  case "tinggi":
    stuntingText = "✅ Tinggi badan anak berada di atas rata-rata untuk usianya.";
    break;
  default:
    stuntingText = "⚠️ Data stunting tidak dikenali.";
}

let wastingText;
switch (wasting?.toLowerCase()) {
  case "normal":
    wastingText = "✅ Berat badan anak tergolong normal.";
    break;
  case "kurus":
    wastingText = "❗ Berat badan anak kurang dari normal (kurus).";
    break;
  case "sangat kurus":
    wastingText = "❗❗ Berat badan anak sangat rendah untuk usianya (sangat kurus).";
    break;
  case "risiko kegemukan":
    wastingText = "⚠️ Anak berisiko mengalami kelebihan berat badan.";
    break;
  default:
    wastingText = "⚠️ Data wasting tidak dikenali.";
}

// Tampilkan di halaman
document.getElementById("predictionResult").innerHTML = `
  <p>${stuntingText}</p>
  <p>${wastingText}</p>
`;

// Tampilkan artikel
const articleCards = document.getElementById("articleCards");
articles.forEach(article => {
  const card = document.createElement("div");
  card.className = "col-md-4";
  card.innerHTML = `
    <div class="card h-100 shadow-sm">
      <div class="card-body">
        <h5 class="card-title">${article.title}</h5>
        <p class="card-text">${article.snippet || ""}</p>
        <a href="${article.link}" target="_blank" class="btn btn-primary">Baca Selengkapnya</a>
      </div>
    </div>
  `;
  articleCards.appendChild(card);
});
