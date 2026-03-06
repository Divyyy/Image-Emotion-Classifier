from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
import cv2
import base64

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model("models/emotion_model.h5")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return render_template("index.html")

    file = request.files["file"]

    if file.filename == "":
        return render_template("index.html")

    # Read file bytes
    file_bytes = file.read()

    # Convert for model
    img = cv2.imdecode(
        np.frombuffer(file_bytes, np.uint8),
        cv2.IMREAD_COLOR
    )

    if img is None:
        return render_template("index.html")

    # Preprocess
    img_resized = cv2.resize(img, (256, 256))
    img_resized = img_resized / 255.0
    img_resized = np.expand_dims(img_resized, 0)

    # Predict
    yhat = model.predict(img_resized)[0][0]

    # Correct probability logic
    if yhat > 0.5:
        prediction = "sad"
        confidence = float(yhat)
    else:
        prediction = "happy"
        confidence = float(1 - yhat)

    confidence = round(confidence, 2)

    # Convert image to base64 for HTML display
    img_base64 = base64.b64encode(file_bytes).decode("utf-8")

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        image_data=img_base64
    )


if __name__ == "__main__":
    app.run(debug=True)