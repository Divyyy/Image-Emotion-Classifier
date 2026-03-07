# Image-Emotion-Classifier (CNN)

This project focuses on building a **Convolutional Neural Network (CNN) for binary image classification** to distinguish between happy and sad facial expressions.

The core development and experimentation are implemented in the **Jupyter Notebook**, which contains the complete pipeline for data preprocessing, model training, and evaluation.

---

## Project Overview

Emotion recognition from images is an important problem in computer vision and human–computer interaction.  
This project builds a **deep learning based image classifier** capable of identifying whether a face expresses happiness or sadness.

The model is trained using a convolutional neural network and later integrated into a simple interface for prediction.

---

## Main Training Notebook

The primary development of this project is implemented in the Jupyter notebook.

```
image-classifier.ipynb
```

The notebook contains the complete machine learning workflow:

- Dataset loading and preprocessing
- Image resizing and normalization
- CNN model architecture design
- Model training
- Performance evaluation
- Training loss visualization

This notebook demonstrates the **end-to-end process of building a CNN-based image classifier**.

---

## Classification Task

The model performs **binary classification** between two emotion categories:

- Happy
- Sad

The model predicts the probability of each class and determines the most likely emotion for a given image.

---

## Model Architecture

The classifier is built using a **Convolutional Neural Network (CNN)**.

Typical pipeline:

```
Input Image
↓
Convolution Layer
↓
ReLU Activation
↓
Max Pooling
↓
Convolution Layers
↓
Flatten
↓
Dense Layers
↓
Output Layer (Sigmoid)
```

### Key Components

**Convolution Layers**

Extract spatial features such as edges, shapes, and patterns from the image.

**Pooling Layers**

Reduce spatial dimensions and help the model focus on dominant features.

**Dense Layers**

Perform classification based on extracted features.

**Sigmoid Output**

Produces a probability score for the binary classification task.

---

## Training Configuration

Training was performed using **TensorFlow / Keras**.

Typical configuration:

- Optimizer: Adam
- Loss Function: Binary Crossentropy
- Evaluation Metrics:
  - Accuracy
  - Loss

The training process tracks both **training loss and validation loss** to monitor model performance.

---

## Training Visualization

The notebook includes visualization of training progress to observe model convergence.

Tracking the loss curves helps evaluate:

- learning behavior
- potential overfitting
- model stability during training

---

## Project Structure

```
image-classifier/
│
├── image-classifier.ipynb
├── app.py
├── Dockerfile
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
```

---

## Model Inference

After training, the trained CNN model is used for prediction.

The application loads the trained model and processes input images to generate emotion predictions.

---

## Deployment

The trained model is integrated with a simple interface built using:

- Flask
- HTML
- CSS
- JavaScript

The application is containerized using **Docker** for reproducible deployment.

---

## Running with Docker

Build the Docker image:

```
docker build -t emotion-classifier .
```

Run the container:

```
docker run -p 5000:5000 emotion-classifier
```

---

## Concepts Demonstrated

- Computer Vision
- Convolutional Neural Networks
- Image preprocessing
- Binary classification
- Model evaluation
- TensorFlow training pipeline
- Containerized deployment using Docker

---
