from flask import Flask, render_template, request, redirect, url_for
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

app = Flask(__name__)

# Load the trained model
model = load_model('model/plant_disease_model.h5')

# Upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Class labels and remedies
classes = [
    'Pepper bell: Bacterial spot', 'Pepper bell: Healthy', 'Potato: Early blight', 'Potato: Healthy',
    'Potato: Late blight', 'Tomato: Target Spot', 'Tomato: Tomato mosaic virus', 
    'Tomato: Tomato YellowLeaf Curl Virus', 'Tomato: Bacterial spot', 'Tomato: Early blight', 
    'Tomato: Healthy', 'Tomato: Late blight', 'Tomato: Leaf Mold', 'Tomato: Septoria leaf spot', 
    'Tomato: Spider mites Two-spotted spider mite'
]

remedies = {
    'Pepper bell: Bacterial spot': "Remove infected leaves, use copper-based fungicides, and avoid overhead watering.",
    'Pepper bell: Healthy': "No action needed. Your plant is healthy!",
    'Potato: Early blight': "Use fungicides, rotate crops, and remove plant debris to prevent reinfection.",
    'Potato: Healthy': "No action needed. Your plant is healthy!",
    'Potato: Late blight': "Apply fungicides, remove infected plants, and ensure good air circulation.",
    'Tomato: Target Spot': "Apply fungicides and ensure proper crop spacing for air circulation.",
    'Tomato: Tomato mosaic virus': "Remove infected plants and control pests that spread the virus.",
    'Tomato: Tomato YellowLeaf Curl Virus': "Use resistant varieties, control whiteflies, and remove infected plants.",
    'Tomato: Bacterial spot': "Use copper-based sprays and avoid working in wet plants to reduce spread.",
    'Tomato: Early blight': "Remove affected leaves and apply fungicides as needed.",
    'Tomato: Healthy': "No action needed. Your plant is healthy!",
    'Tomato: Late blight': "Apply fungicides and remove infected plants immediately.",
    'Tomato: Leaf Mold': "Improve ventilation and apply appropriate fungicides.",
    'Tomato: Septoria leaf spot': "Use fungicides and avoid overhead watering.",
    'Tomato: Spider mites Two-spotted spider mite': "Use miticides and remove heavily infested leaves."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Preprocess image
        img = load_img(filepath, target_size=(128, 128))
        img = img_to_array(img) / 255.0
        img = np.expand_dims(img, axis=0)
        
        # Prediction
        prediction = model.predict(img)
        predicted_class = classes[np.argmax(prediction)]
        remedy = remedies.get(predicted_class, "No remedy found for the detected disease.")
        
        return render_template('result.html', prediction=predicted_class, remedy=remedy, image_path=filepath)

if __name__ == '__main__':
    app.run(debug=True)
