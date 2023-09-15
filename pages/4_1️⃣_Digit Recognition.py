import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import model_from_json
from tensorflow.keras.optimizers import SGD
from PIL import Image
import cv2

model_architecture = "pages/Model/digit_config.json"
model_weights = "pages/Model/digit_weight.h5"
model = model_from_json(open(model_architecture).read())
model.load_weights(model_weights)

optim = SGD()
model.compile(loss="categorical_crossentropy", optimizer=optim, metrics=["accuracy"])

mnist = keras.datasets.mnist
(_, _), (X_test, _) = mnist.load_data()
X_test_image = X_test

RESHAPED = 784

X_test = X_test.reshape(10000, RESHAPED)
X_test = X_test.astype("float32")

# Normalize in [0,1]
X_test /= 255


@st.cache(allow_output_mutation=True)
def generate_random_digits():
    index = np.random.randint(0, 9999, 150)
    digit_random = np.zeros((10 * 28, 15 * 28), dtype=np.uint8)
    for i in range(0, 150):
        m = i // 15
        n = i % 15
        digit_random[m * 28 : (m + 1) * 28, n * 28 : (n + 1) * 28] = X_test_image[index[i]]
    cv2.imwrite("pages/Model/digit_random.png", digit_random)
    return digit_random, index


def recognize_digits(image, index):
    X_test_sample = np.zeros((150, 784), dtype=np.float32)
    for i in range(0, 150):
        X_test_sample[i] = X_test[index[i]]

    prediction = model.predict(X_test_sample)
    results = ""
    for i in range(0, 150):
        result = np.argmax(prediction[i])
        results += str(result) + " "
        if (i + 1) % 15 == 0:
            results += "\n"

    return results


def main():
    st.title("NHẬN DẠNG CHỮ SỐ VIẾT TAY")
    st.text("Hãy tạo ra ngẫu nhiên những chữ số và nhận diện chúng")

    if "image_data" not in st.session_state:
        st.session_state.image_data = None

    if "index" not in st.session_state:
        st.session_state.index = None

    if "results" not in st.session_state:
        st.session_state.results = ""

    if st.button("Tạo ảnh"):
        digit_random, index = generate_random_digits()
        st.session_state.image_data = Image.fromarray(digit_random)
        st.session_state.index = index

    if st.button("Nhận dạng"):
        results = recognize_digits(st.session_state.image_data, st.session_state.index)
        st.session_state.results = results

    if st.session_state.image_data is not None:
        st.image(st.session_state.image_data, use_column_width=True)

    st.text_area("KẾT QUẢ", value=st.session_state.results, height=150)


if __name__ == "__main__":
    main()
