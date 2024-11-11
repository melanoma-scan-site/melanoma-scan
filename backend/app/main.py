from random import random

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Form

from models import dto
from services import image_service


app = FastAPI()

@app.post("/check", response_model=dto.MelanomaStatus)
def check_for_melanoma(base64_file: str = Form()):
    # validate base64
    image_bytes = image_service.base64_to_bytes(base64_file)
    if image_bytes == b'':
        raise HTTPException(422, "Image is not base64 encoded")
    
    # validate image
    if image_service.image_is_valid(image_bytes) is False:
        raise HTTPException(422, "Image type is not supported")
    
    # preprocess image to model
    # to_predict = preprocess_image(image_bytes)
    # if to_predict is None:
    #     raise HTTPException(422, "Image preprocessing failed")
    
    # predict
    # prediction = model.predict(to_predict)
    # if prediction is None:
    #     raise HTTPException(422, "Model prediction failed")
    
    return dto.MelanomaStatus.get_from_float(random())