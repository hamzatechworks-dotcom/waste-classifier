from tensorflow.keras.models import load_model

model = load_model("9_waste_classifier_model.h5")

print("Model Loaded Successfully ✅")
model.summary()