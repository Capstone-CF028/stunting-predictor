import axios from 'axios';

const app = document.getElementById('app');

function createHome() {
  const container = document.createElement('div');
  container.className = 'container mt-5';

  const title = document.createElement('h1');
  title.textContent = 'Stunting Prediction App';
  container.appendChild(title);

  const btnGroup = document.createElement('div');
  btnGroup.className = 'btn-group mt-4';

  const btnStunting = document.createElement('button');
  btnStunting.className = 'btn btn-primary';
  btnStunting.textContent = 'Prediksi Stunting';
  btnStunting.onclick = () => {
    createPredictionForm('stunting');
  };

  const btnWasting = document.createElement('button');
  btnWasting.className = 'btn btn-secondary';
  btnWasting.textContent = 'Prediksi Wasting';
  btnWasting.onclick = () => {
    createPredictionForm('wasting');
  };

  btnGroup.appendChild(btnStunting);
  btnGroup.appendChild(btnWasting);
  container.appendChild(btnGroup);

  app.innerHTML = '';
  app.appendChild(container);
}

function createPredictionForm(type) {
  const container = document.createElement('div');
  container.className = 'container mt-5';

  const backBtn = document.createElement('button');
  backBtn.className = 'btn btn-link mb-3';
  backBtn.textContent = '← Kembali';
  backBtn.onclick = createHome;
  container.appendChild(backBtn);

  const title = document.createElement('h2');
  title.textContent = `Form Input ${type === 'stunting' ? 'Stunting' : 'Wasting'}`;
  container.appendChild(title);

  const form = document.createElement('form');

  const fields = [
    { label: 'Usia (bulan)', name: 'age', type: 'number', min: 0, max: 60 },
    { label: 'Berat Badan (kg)', name: 'weight', type: 'number', step: '0.1' },
    { label: 'Tinggi Badan (cm)', name: 'height', type: 'number', step: '0.1' },
    { label: 'Jenis Kelamin', name: 'gender', type: 'select', options: ['Laki-laki', 'Perempuan'] }
  ];

  fields.forEach(field => {
    const formGroup = document.createElement('div');
    formGroup.className = 'mb-3';

    const label = document.createElement('label');
    label.className = 'form-label';
    label.textContent = field.label;
    label.htmlFor = field.name;
    formGroup.appendChild(label);

    let input;
    if (field.type === 'select') {
      input = document.createElement('select');
      input.className = 'form-select';
      input.name = field.name;
      field.options.forEach(opt => {
        const option = document.createElement('option');
        option.value = opt;
        option.textContent = opt;
        input.appendChild(option);
      });
    } else {
      input = document.createElement('input');
      input.type = field.type;
      input.className = 'form-control';
      input.name = field.name;
      if (field.min !== undefined) input.min = field.min;
      if (field.max !== undefined) input.max = field.max;
      if (field.step !== undefined) input.step = field.step;
      input.required = true;
    }
    formGroup.appendChild(input);
    form.appendChild(formGroup);
  });

  const submitBtn = document.createElement('button');
  submitBtn.type = 'submit';
  submitBtn.className = 'btn btn-primary';
  submitBtn.textContent = 'Prediksi';
  form.appendChild(submitBtn);

  form.onsubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => {
      data[key] = value;
    });
    try {
      const response = await axios.post(`http://localhost:3002/predict/${type}`, data);
      showResult(response.data, type);
    } catch (error) {
      alert('Error saat memproses prediksi');
      console.error(error);
    }
  };

  container.appendChild(form);
  app.innerHTML = '';
  app.appendChild(container);
}

function showResult(result, type) {
  const container = document.createElement('div');
  container.className = 'container mt-5';

  const backBtn = document.createElement('button');
  backBtn.className = 'btn btn-link mb-3';
  backBtn.textContent = '← Kembali ke Form';
  backBtn.onclick = () => createPredictionForm(type);
  container.appendChild(backBtn);

  const title = document.createElement('h2');
  title.textContent = 'Hasil Prediksi';
  container.appendChild(title);

  const resultText = document.createElement('p');
  resultText.textContent = `Kategori ${type === 'stunting' ? 'Stunting' : 'Wasting'}: ${result.category}`;
  container.appendChild(resultText);

  const articlesTitle = document.createElement('h3');
  articlesTitle.textContent = 'Rekomendasi Artikel';
  container.appendChild(articlesTitle);

  const articlesList = document.createElement('ul');
  articlesList.className = 'list-group';

  result.articles.forEach(article => {
    const item = document.createElement('li');
    item.className = 'list-group-item list-group-item-action';
    item.textContent = article.title;
    item.style.cursor = 'pointer';
    item.onclick = () => {
      window.open(article.url, '_blank');
    };
    articlesList.appendChild(item);
  });

  container.appendChild(articlesList);

  app.innerHTML = '';
  app.appendChild(container);
}

createHome();
