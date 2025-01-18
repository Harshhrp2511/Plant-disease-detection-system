from flask import Flask, render_template, request, redirect, url_for, flash
import os
from tensorflow.keras.models import load_model  # type: ignore
from tensorflow.keras.preprocessing.image import load_img, img_to_array  # type: ignore
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Load the pre-trained model
model = load_model('model/plant_disease_model.h5')

# Configuration for uploaded files
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Classes corresponding to the model's predictions
classes = [
    'Pepper bell: Bacterial spot', 'Pepper bell: Healthy', 'Potato: Early blight', 'Potato: Healthy',
    'Potato: Late blight', 'Tomato: Target Spot', 'Tomato: Tomato mosaic virus',
    'Tomato: Tomato YellowLeaf Curl Virus', 'Tomato: Bacterial spot', 'Tomato: Early blight',
    'Tomato: Healthy', 'Tomato: Late blight', 'Tomato: Leaf Mold', 'Tomato: Septoria leaf spot',
    'Tomato: Spider mites Two-spotted spider mite'
]

# Remedies for plant diseases
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

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling image uploads and predictions
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        flash("No file provided. Please upload an image.")
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash("No file selected. Please choose an image.")
        return redirect(request.url)

    if file:
        # Save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Preprocess the image
        img = load_img(filepath, target_size=(128, 128))
        img = img_to_array(img) / 255.0
        img = np.expand_dims(img, axis=0)
        
        # Make a prediction
        prediction = model.predict(img)
        max_prob = np.max(prediction)
        confidence_threshold = 0.7  # Set a high confidence threshold
        
        if max_prob < confidence_threshold:
            # If the confidence is below the threshold, treat it as irrelevant
            predicted_class = "Unrecognized or irrelevant image."
            remedy = "Please upload a clear image of a plant to get a proper diagnosis."
        else:
            predicted_class = classes[np.argmax(prediction)]
            remedy = remedies.get(predicted_class, "No remedy found for the detected disease.")
            
        # Render the result page with prediction and remedy
        return render_template('result.html', prediction=predicted_class, remedy=remedy, image_path=filepath)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
