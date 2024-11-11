from io import BytesIO
from base64 import b64decode

from magic import from_buffer


def _get_mime(content: bytes) -> str:
    mime = ""

    file_obj = BytesIO(content)
    mime_type = from_buffer(file_obj.read(2048), True)

    if mime_type:
        mime = mime_type

    return mime

def image_is_valid(content: bytes) -> bool:
    mime = _get_mime(content)
    
    allowed_types = [
        'image/jpeg',
        'image/png',
    ]

    return mime in allowed_types

def base64_to_bytes(base64_file: str) -> bytes:
    try:
        # convert base64 string to bytes
        return b64decode(base64_file)
    except Exception as e:
        print("Image is not base64 encoded", e)
        return b''
