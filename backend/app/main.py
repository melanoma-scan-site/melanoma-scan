from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Form

from models import dto
from services import image_service
from services import ml_service


app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

@app.post("/check", response_model=dto.MelanomaStatus)
def check_for_melanoma(base64_file: str = Form()):
    # validate base64
    image_bytes = image_service.base64_to_bytes(base64_file)
    if image_bytes == b'':
        raise HTTPException(422, "Image is not base64 encoded")
    
    # validate image
    if image_service.image_is_valid(image_bytes) is False:
        raise HTTPException(422, "Image type is not supported")
    
    # make prediction
    model_prediction = ml_service.predict(image_bytes)
    return dto.MelanomaStatus.get_from_float(model_prediction)