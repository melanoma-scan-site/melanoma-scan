from os.path import exists

import tensorflow as tf
import keras

from utils.config import CONFIG


# show error if model file is not found
if not exists(CONFIG.TF_MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {CONFIG.TF_MODEL_PATH}")

MODEL: keras.models.Sequential = keras.saving.load_model(CONFIG.TF_MODEL_PATH) # type: ignore
    
def predict(image_bytes: bytes) -> float:
    image = tf.io.decode_image(image_bytes, channels=3)
    resized_image = tf.image.resize(image, (224, 224)) 
    
    # make prediction
    prediction = MODEL.predict(tf.expand_dims(resized_image, axis=0), verbose="0")
    
    # ['Melanoma', 'NotMelanoma'] types
    # first element is the probability of melanoma
    return round(prediction[0][0], 2)
