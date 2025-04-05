# Cancer Detection System

A deep learning-based web application for early detection of cancer through medical image analysis.

## Overview

This application uses a trained neural network to analyze medical images and determine whether they contain signs of cancer. The system provides a user-friendly web interface built with Flask, allowing users to upload and analyze medical images.

## Features

- User-friendly web interface with drag-and-drop functionality
- Real-time image analysis with deep learning
- Clear visualization of results with confidence scores
- Responsive design that works on desktop and mobile devices
- Dark mode UI for reduced eye strain in clinical environments

## Technologies Used

- **Flask**: Web framework for the application
- **TensorFlow/Keras**: Deep learning framework for the cancer detection model
- **Bootstrap**: Frontend framework for responsive design
- **HTML/CSS/JavaScript**: Frontend web development

## Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/cancer-detection-system.git
cd cancer-detection-system
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

5. Open your browser and navigate to http://127.0.0.1:5000/

## Model Information

The system uses a convolutional neural network trained on medical images to classify them as either showing signs of cancer or being cancer-free. The model has been trained on a dataset of medical images and achieves high accuracy in preliminary testing.

Note: This tool is meant for screening purposes only and does not replace professional medical advice.

## Directory Structure

```
├── app.py                 # Main application file
├── model.h5               # Trained neural network model
├── requirements.txt       # Project dependencies
├── train_model.py         # Script used to train the model
├── dataset/               # Training and test datasets
│   ├── test/
│   └── train/
├── static/                # Static files (CSS, uploads)
│   ├── index.css
│   └── uploads/
└── templates/             # HTML templates
    └── index.html
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This application is intended for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.