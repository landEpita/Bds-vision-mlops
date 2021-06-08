import requests
import tensorflow as tf
import json
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

datagen = ImageDataGenerator(rescale=1./255)
test_generator = datagen.flow_from_directory(
    directory= "../src_image/data",
    target_size=(150, 150),
    color_mode="rgb",
    batch_size=32,
    class_mode='binary',
    shuffle=True,
)

#print(test_generator[0][0][0:2].shape)
images = test_generator[0][0][0:9].tolist()
print(test_generator[0][0][0:9].shape)
print(test_generator[0][1][0:9])


# images = np.random.randint(0, 1, size=(10,150, 150, 3)).tolist()


data = json.dumps({"signature_name": "serving_default", "data": images})
headers = {"content-type": "application/json"}
json_response = requests.post(f'http://127.0.0.1:5001/predict/model', data=data, headers=headers)
js = json_response.text 
if js:
    predictions = js
    print(predictions)
else:
    print("not enough images")
