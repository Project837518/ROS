import os
import pefile
from PIL import Image
import numpy as np
import joblib


model_file = '/app/svm_model.pkl'
if not os.path.isfile(model_file):
    print(f"{model_file} does not exist.")
    exit(1)
else: 
	print("abrakadabra")

model = joblib.load(model_file)


pe = pefile.PE('putty.exe')
raw_bytes = bytes(pe.__data__)
image = Image.frombytes('L', (32, 32), raw_bytes)

normalized_image = np.array(image) / 255.0
reshaped_image = normalized_image.reshape(1, 32, 32, 1)

predictions = model.predict(reshaped_image)

print(predictions)
