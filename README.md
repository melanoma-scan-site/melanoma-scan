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

---

## Installation Guide for Melanoma Detection Web Application

This guide explains how to set up the Melanoma Detection web application using Docker Compose. Ensure that Docker and Docker Compose are installed on your system before proceeding.

### Prerequisites

- **Docker**: Install Docker engine from [Docker’s official website](https://docs.docker.com/engine/install/).

### Step 1: Clone the Repository

Clone this GitHub repository to your local machine:
```bash
git clone https://github.com/your-username/melanoma-detection.git
cd melanoma-detection
```

### Step 2: SSL serteficates

Need to create SSL certificates for a secure connection. Afterwards, two files need to be replaced in the `ssl` directory:
- **cert.key** - private key
- **cert.pem** - public key

### Step 3: Start docker containers

Use this command to build and start
```shell
docker compose up -d --build
```