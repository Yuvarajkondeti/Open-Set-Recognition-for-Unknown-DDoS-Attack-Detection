# DDoS Attack Detection using CNN and Open-Set Recognition (OSR)

## 📌 Overview
This project implements a **DDoS Attack Detection System** using a **Convolutional Neural Network (CNN)** combined with **Open-Set Recognition (OSR)**.  
Unlike traditional closed-set classifiers, this system can detect **known DDoS attacks** and also **identify unknown (previously unseen) attacks** by measuring feature-space distance.

The project includes:
- Data preprocessing and model training
- A Flask-based backend API
- A simple web-based frontend dashboard
- A Jupyter Notebook for data analysis and evaluation

---

## 🧠 Key Features
- CNN-based network traffic classification
- Open-Set Recognition for unknown DDoS detection
- Real-world Kaggle DDoS dataset
- Data cleaning (handling IPs, timestamps, NaN, infinity)
- REST API using Flask
- Frontend dashboard (HTML/CSS/JavaScript)
- Jupyter Notebook for EDA and evaluation
- Accuracy, Precision, Recall, F1-score, Confusion Matrix

---

## 📂 Project Structure
ddos/
│
├── backend/
│ ├── app.py # Flask API
│ ├── train.py # Model training script
│ ├── model.py # CNN + OSR logic
│ └── requirements.txt
│
├── frontend/
│ ├── index.html # Dashboard UI
│ ├── script.js # Frontend logic
│ └── style.css # Styling
│
├── data/
│ └── final_dataset.csv # Dataset (not pushed to GitHub)
│
├── saved_model/
│ └── cnn_model.pth # Trained model (not pushed to GitHub)
│
├── DDoS_Model_Evaluation.ipynb # Jupyter Notebook (EDA + testing)
├── .gitignore
└── README.md


## 📊 Dataset

### Dataset Source
Kaggle – DDoS Datasets  
🔗 https://www.kaggle.com/datasets/devendra416/ddos-datasets

### Dataset Description
- Flow-based network traffic features
- Includes benign and DDoS attack traffic
- Very large dataset (millions of rows)

### Dataset Setup
1. Download the dataset from Kaggle
2. Extract the CSV file(s)
3. Choose or merge a CSV file
4. Rename it to: final_dataset
5. Place it inside: an new folder called data


⚠️ The dataset is **not included** in this repository due to its size.

---

## 🛠️ Requirements & Installation

### Python
- Python **3.10+** recommended

Check version:
python --version

Install Dependencies

From the project root directory:
python -m pip install -r backend/requirements.txt

If PyTorch fails to install:
pip install torch --index-url https://download.pytorch.org/

raining the Model

To train the CNN model:

python backend/train.py

What the training script does:

Loads the Kaggle dataset

Drops non-numeric columns (IP addresses, Flow ID, Timestamp)

Replaces infinity values and removes NaNs

Samples data to prevent memory overload

Trains a CNN model

Saves the trained model to:

saved_model/cnn_model.pth

🌐 Running the Backend (Flask API)

Start the backend server:

python backend/app.py


Expected output:

Running on http://127.0.0.1:5000

API Endpoint

POST /predict

Input: JSON array of features

Output: Prediction (Known Traffic / Unknown DDoS) and distance score

🖥️ Running the Frontend

Navigate to:

frontend/


Open:

index.html


Click Analyze Traffic

The frontend:

Simulates network traffic features

Sends them to the Flask backend

Displays prediction results in real time

📓 Jupyter Notebook (Data Analysis & Evaluation)

Start Jupyter Notebook:

jupyter notebook


Open:

DDoS_Model_Evaluation.ipynb

Notebook Contents

Exploratory Data Analysis (EDA)

Label distribution analysis

Data cleaning steps

Loading the trained CNN model

Accuracy, Precision, Recall, F1-score

Confusion Matrix visualization

Open-Set Recognition testing

📈 Evaluation Metrics

Accuracy

Precision

Recall

F1-score

Confusion Matrix

Unknown attack detection count

}'

🎓 Academic Explanation

This project demonstrates how Open-Set Recognition improves DDoS detection by allowing the model to reject unknown attacks instead of forcing them into known classes.
It is suitable for final-year projects, research demonstrations, and cybersecurity studies.

⚠️ Notes

Dataset and trained model files are excluded from GitHub using .gitignore

Training is performed on a sampled subset for memory efficiency

OSR logic is simplified for academic demonstration purposes



