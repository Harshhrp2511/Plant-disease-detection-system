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

# Class labels
classes = ['Peppe bell: Bacterial spot', 'Peppe bell: healthy', 'Potato: Early blight', 'Potato: healthy',
           'Potato: Late blight', 'Tomato: Target Spot', 'Tomato: Tomato mosaic virus', 'Tomato: Tomato YellowLeaf Curl Virus',
           'Tomato: Bacterial spot', 'Tomato: Early blight', 'Tomato: healthy', 'Tomato: Late blight', 'Tomato: Leaf Mold',
           'Tomato: Septoria leaf spot', 'Tomato: Spidermites Two spotted spider mite']  # Replace with actual class names

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
        
        return render_template('result.html', prediction=predicted_class, image_path=filepath)

if __name__ == '__main__':
    app.run(debug=True)
