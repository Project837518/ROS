import pefile
from PIL import Image
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import joblib

svm_model = SVC(kernel='linear')

pe = pefile.PE('/app/putty.exe')  
raw_bytes = bytes(pe.__data__)
image = Image.frombytes('L', (32, 32), raw_bytes)

normalized_image = np.array(image) / 255.0
reshaped_image = normalized_image.reshape(1, -1)
svm_model = joblib.load('/app/svm_model.pkl') 

scaler = StandardScaler()
scaled_image = scaler.fit_transform(reshaped_image)
predictions = svm_model.predict(scaled_image)

if predictions == 1:
    print("It is certainly a virus.")
elif predictions >= 0.75:
    print("Most likely it is a virus.")
elif predictions >= 0.5:
    print("It is somewhat likely to be a virus.")
elif predictions >= 0.25:
    print("It is unlikely to be a virus.")
else:
    print("It is highly unlikely to be a virus.")

