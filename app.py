from flask import Flask, request, render_template, redirect, url_for, flash
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from datetime import datetime
try:
    # Explicit import of PIL
    from PIL import Image
except ImportError:
    import sys
    print("Pillow is required. Please install it with: pip install pillow")
    sys.exit(1)

app = Flask(__name__)
app.secret_key = 'cancer_detection_secret_key'

# Create upload folder if it doesn't exist
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load your trained model with error handling
try:
    model = load_model("model.h5")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Function to preprocess image
def preprocess_img(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file uploaded!", "error")
            return redirect(request.url)
        
        file = request.files["file"]
        if file.filename == "":
            flash("No file selected!", "error")
            return redirect(request.url)
        
        # Check file extension
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
        if not ('.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in allowed_extensions):
            flash("Invalid file type! Please upload an image.", "error")
            return redirect(request.url)
            
        # Generate unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{timestamp}_{file.filename}"
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)  # Save image
        
        # Predict using ML model
        if model is not None:
            try:
                pred = model.predict(preprocess_img(file_path))
                confidence = pred[0][0] if pred[0][0] > 0.5 else 1 - pred[0][0]
                confidence_percentage = f"{confidence * 100:.2f}%"
                
                if pred[0][0] > 0.5:
                    prediction = "No Cancer Detected"
                    status = "healthy"
                else:
                    prediction = "Cancer Detected"
                    status = "cancer"
                
                result_details = {
                    'prediction': prediction,
                    'confidence': confidence_percentage,
                    'status': status
                }
                
                return render_template("index.html", result=result_details, img_src=file_path)
            except Exception as e:
                flash(f"Error processing image: {e}", "error")
                return redirect(request.url)
        else:
            flash("Model not loaded. Please check server logs.", "error")
            return redirect(request.url)

    return render_template("index.html")

@app.route("/shutdown", methods=["POST"])
def shutdown():
    # Shutdown the server
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Server shutting down..."

if __name__ == "__main__":
    app.run(debug=True)
