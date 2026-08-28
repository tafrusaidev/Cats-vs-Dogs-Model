# 🐾 Cats vs Dogs Classifier

A Convolutional Neural Network (CNN) that classifies images as **cats** or **dogs**, wrapped in a simple, interactive **Streamlit** web app for real-time predictions.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange?logo=tensorflow&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

This project trains a deep learning model to distinguish between images of cats and dogs, then serves the trained model through a lightweight web interface. Upload any image, and the app returns a prediction along with a confidence score.

- 📓 **`Cats_vs_Dogs_Model.ipynb`** — notebook covering data preparation, model architecture, and training
- 🧠 **`cat_dog_model (2).h5`** — the trained Keras model
- 🎛️ **`app.py`** — Streamlit app for interactive inference
- 📦 **`requirements.txt`** — project dependencies

---

## ✨ Features

- 🖼️ Upload a JPG, JPEG, PNG, or WEBP image and get an instant prediction
- 🐶🐱 Clean output with a predicted label and confidence percentage
- ⚡ Cached model loading for fast repeated predictions
- 🧩 Simple, single-file Streamlit app — easy to read, easy to extend

---

## 🗂️ Project Structure

```
Cats-vs-Dogs-Model/
├── .vscode/                     # Editor settings
├── Cats_vs_Dogs_Model.ipynb     # Training notebook
├── app.py                       # Streamlit inference app
├── cat_dog_model (2).h5         # Trained model weights
├── requirements.txt             # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/tafrusaidev/Cats-vs-Dogs-Model.git
cd Cats-vs-Dogs-Model
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`. Upload an image of a cat or dog and see the model's prediction!

---

## 🧠 How It Works

1. The uploaded image is converted to RGB and resized to **128×128** pixels.
2. Pixel values are normalized to the `[0, 1]` range.
3. The trained CNN (`cat_dog_model (2).h5`) predicts the probability that the image shows a dog.
4. A probability **≥ 0.5** is classified as **Dog 🐶**; otherwise, it's classified as **Cat 🐱**.
5. The predicted label and confidence score are displayed in the app.

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Deep Learning | TensorFlow / Keras |
| Image Processing | Pillow, OpenCV |
| Data Handling | NumPy, Pandas |
| Visualization | Matplotlib |
| Web App | Streamlit |

---

## 📓 Model Training

The full training pipeline — including data loading, augmentation, model architecture, and evaluation — is documented step-by-step in [`Cats_vs_Dogs_Model.ipynb`](./Cats_vs_Dogs_Model.ipynb). Open it in Jupyter or Google Colab to explore or retrain the model.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is available under the MIT License. Feel free to use and adapt it.

---

## 👤 Author

**tafrusaidev**
GitHub: [@tafrusaidev](https://github.com/tafrusaidev)

---

<p align="center">If you found this project useful, consider giving it a ⭐!</p>
