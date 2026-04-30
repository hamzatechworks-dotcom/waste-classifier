from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.applications.mobilenet import preprocess_input

img_path = "Enter test image"

img = image.load_img(img_path, target_size=(224,224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

img_array = preprocess_input(img_array)

prediction = model.predict(img_array)

classes = list(train_data.class_indices.keys())
print("Prediction:", classes[np.argmax(prediction)])