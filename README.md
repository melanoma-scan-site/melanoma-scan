# Melanoma Detection Web Application

This is a web application designed to assist users in identifying potential melanoma in skin images. The app allows users to upload a photo of a skin lesion, which is then analyzed by a machine learning model hosted on a server. The model provides an initial assessment, indicating whether there is a likelihood of melanoma.

Project link [https://melanoma-scan.site/](https://melanoma-scan.site/)

**Key Features:** 
- Simple, intuitive user interface for uploading images 
- Server-based image analysis using a machine learning model (TensorFlow/Keras) 
- Secure API and encrypted data handling for user privacy 
- Accessibility support for users with disabilities 
- Dockerized setup for easy deployment and scalability

**Important Notice:** This application provides a preliminary assessment only and is not a substitute for professional medical advice. Always consult a qualified dermatologist for a comprehensive evaluation. 

**Technologies Used:** 
- FastAPI
- Svelte
- Docker
- TensorFlow/Keras
- Nginx

--- 

**Deployment:** The app is hosted on a Linux VPS with Docker Compose managing containerized services for frontend, backend, and reverse proxy. 

**Note:** This project is intended for educational purposes and should not be used as a standalone diagnostic tool.