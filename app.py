from pathlib import Path

import numpy as np
import streamlit as st
from PIL import Image


MODEL_PATH = Path(__file__).with_name("cat_dog_model (2).h5")
IMAGE_SIZE = (128, 128)


st.set_page_config(
	page_title="Cats vs Dogs Classifier",
	page_icon="🐾",
	layout="centered",
)


@st.cache_resource
def get_model():
	"""Load the trained model once and reuse it between Streamlit reruns."""
	from tensorflow.keras.models import load_model

	return load_model(MODEL_PATH)


def predict(image: Image.Image) -> tuple[str, float]:
	image_array = np.asarray(image.convert("RGB").resize(IMAGE_SIZE), dtype=np.float32)
	image_array = np.expand_dims(image_array / 255.0, axis=0)
	dog_probability = float(get_model().predict(image_array, verbose=0)[0][0])

	if dog_probability >= 0.5:
		return "Dog", dog_probability
	return "Cat", 1.0 - dog_probability


st.title("Cats vs Dogs Classifier")
st.write("Upload an image and let the trained CNN classify it.")

uploaded_file = st.file_uploader(
	"Choose a cat or dog image",
	type=["jpg", "jpeg", "png", "webp"],
)

if uploaded_file is None:
	st.info("Upload an image to begin.")
else:
	image = Image.open(uploaded_file)
	st.image(image, caption=uploaded_file.name, use_container_width=True)

	try:
		label, confidence = predict(image)
	except Exception as error:
		st.error(f"Prediction failed: {error}")
		st.stop()

	if label == "Dog":
		st.success(f"Prediction: {label} 🐶")
	else:
		st.success(f"Prediction: {label} 🐱")
	st.metric("Confidence", f"{confidence:.1%}")
