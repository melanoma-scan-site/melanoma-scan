import requests
from base64 import b64encode


url = "https://melanoma-scan.site/api/check"
headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}


file_path = "m.jpg"
encoded_string = ""
with open(file_path, "rb") as file:
    encoded_string = b64encode(file.read()).decode("utf-8")
    
response = requests.post(url, headers=headers, data={"base64_file": encoded_string})
print(response.json())