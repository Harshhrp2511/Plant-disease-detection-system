from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model("plant_disease_model.h5")

# Define image size
img_height, img_width = 224, 224

# Prediction function
def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(img_height, img_width))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    
    prediction = model.predict(img_array)
    class_names = ["Healthy", "Diseased"]  # Update according to your classes
    return class_names[np.argmax(prediction)]

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    # Save the file
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    
    # Predict the disease
    disease = predict_disease(file_path)
    return jsonify({"prediction": disease})

if __name__ == '__main__':
    app.run(debug=True)
