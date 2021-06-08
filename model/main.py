import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import mlflow.tensorflow

mlflow.set_tracking_uri("sqlite:///mlruns.db")
mlflow.tensorflow.autolog()
# mlflow ui --backend-store-uri sqlite:///mlruns.db

datagen = ImageDataGenerator(rescale=1./255)

train_generator = datagen.flow_from_directory(
    directory= "data",
    target_size=(150, 150),
    color_mode="rgb",
    batch_size=32,
    class_mode='binary',
    shuffle=True,
)

test_generator = datagen.flow_from_directory(
    directory= "data",
    target_size=(150, 150),
    color_mode="rgb",
    batch_size=32,
    class_mode='binary',
    shuffle=True,
)


model = tf.keras.models.Sequential([
    # Note the input shape is the desired size of the image 150x150 with 3 bytes color
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2), 
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'), 
    tf.keras.layers.MaxPooling2D(2,2),
    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(), 
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu'), 
    # Only 1 output neuron. It will contain a value from 0-1 where 0 for 1 class ('cats') and 1 for the other ('dogs')
    tf.keras.layers.Dense(1, activation='sigmoid')  
])

model.compile(loss='binary_crossentropy',
             optimizer='adam',
             metrics=['accuracy'])

with mlflow.start_run() as run:
    run_uuid = run.info.run_uuid
    print("MLflow Run ID: %s" % run_uuid)
    model.fit(train_generator,
             epochs=10,
             validation_data=test_generator)
    results = model.evaluate(test_generator,batch_size=128)
    mlflow.log_metric("test_loss", results[0])
    mlflow.log_metric("test_accuracy", results[1])
print("test loss, test acc:", results)