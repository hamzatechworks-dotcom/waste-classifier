# waste-classifier
# ♻️ Waste Classifier Model

A deep learning-based waste classification system that categorizes different types of waste into 9 classes using a pretrained MobileNet model. This project helps in smart waste management and recycling.

---

## 📌 Features

- Classifies waste into 9 categories
- Uses pretrained MobileNet for efficient performance
- Lightweight and fast
- Suitable for real-time applications
- Easy to integrate into web or mobile apps

---

## 🗂️ Classes

- Paper  
- Cardboard  
- Textile Waste  
- Metal  
- Plastic  
- Glass  
- Organic Waste  
- Other classes 

---

## 🧠 Model Details

- Architecture: MobileNet (Pretrained)
- Framework: TensorFlow / PyTorch
- Input Size: 224 x 224
- Output: 9 classes (Softmax)

---

## 📁 Project Structure

waste-classifier/
│
├── model/
│   ├── waste_model.h5
│
├── test_model.py/
│   ├── load model
│  
├── prediction.py/
│   ├── code to make prediction
│
└── README.md

---

## ⚙️ Installation

git clone https://github.com/your-username/waste-classifier.git  
cd waste-classifier  
pip install -r requirements.txt  

---

## 🚀 Usage

### Run Inference

from model import load_model  
from utils import preprocess_image  

model = load_model("model/waste_model.h5")  

img = preprocess_image("sample.jpg")  
prediction = model.predict(img)  

print("Predicted Class:", prediction)  

---

### Run Web App (Optional)

streamlit run app/app.py  

---

## 📊 Training

- Dataset contains labeled waste images
- Data augmentation used (rotation, flipping, scaling)
- Transfer learning with MobileNet
- Fine-tuned on custom dataset

---

## 🎯 Applications for future use

- Smart recycling systems  
- Waste segregation automation  
- Environmental monitoring  
- Educational tools  

## 📜 License

This project is open-source under the MIT License.
