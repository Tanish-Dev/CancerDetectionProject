# Cancer Detection System

A deep learning web application for cancer detection from medical images.

## Project Overview

This application uses a trained convolutional neural network (CNN) to analyze medical images and detect signs of cancer. The system provides:

- An intuitive web interface for uploading medical images
- Real-time analysis and prediction
- Confidence scores for predictions
- Dark mode UI with responsive design

## Features

- **User-friendly Interface**: Simple drag-and-drop or click-to-upload functionality
- **Real-time Analysis**: Quick processing and display of results
- **Confidence Scoring**: Displays the model's confidence in its prediction
- **Medical Disclaimer**: Reminds users that this is a screening tool, not a replacement for professional medical diagnosis

## Technology Stack

- **Backend**: Python, Flask
- **Machine Learning**: TensorFlow/Keras
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **UI Components**: Font Awesome, Google Fonts

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/cancer-detection-system.git
   cd cancer-detection-system
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:

   ```
   python app.py
   ```

4. Open a browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

1. Access the web interface
2. Upload a medical image using drag-and-drop or file selection
3. Click "Analyze Image" to process
4. View the prediction results and confidence score

## Dataset

The model was trained on a dataset with two classes:

- **Class 1**: Normal tissue images
- **Class 2**: Cancer tissue images

## Model

The model (`model.h5`) is a pre-trained convolutional neural network. It was trained on the included dataset using the `train_model.py` script.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Developed by Tanish

## Disclaimer

This application is intended for educational and demonstration purposes only. It should not be used for actual medical diagnosis. Always consult healthcare professionals for medical advice and diagnosis.
