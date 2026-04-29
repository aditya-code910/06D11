# Group 06 D11 - Manufacturing App Deployment on Kubernetes 

## Description:
This project demonstrates containerizing and deploying a Python Flask-based Manufacturing Application on Kubernetes with rolling updates, self-healing, and zero-downtime deployment.

---

##  Tech Stack
- Python (Flask)
- Docker
- Docker Hub
- Kubernetes (Docker Desktop / Minikube)
- GitHub Actions (CI/CD Concept)

---

##  Architecture Overview
Developer → GitHub → Docker Image Build → Docker Hub → Kubernetes Deployment → Service (NodePort) → End User
The application runs inside Docker containers managed by Kubernetes.

---

##  Docker Image
Docker Hub Image:
aaditibhale/manufacturing-app:v2

---

##  How To Run The Project (Fresh Setup)

### 1️ Prerequisites
- Install Docker Desktop
- Enable Kubernetes in Docker Desktop

### 2 Verify Kubernetes:
- kubectl get nodes

### 3 Deploy Application
From project root folder:
- kubectl apply -f deployment.yaml
- kubectl apply -f service.yaml

### 4 Verify Deployment
- kubectl get pods
- kubectl get svc

### 5 Access Application
Open browser:

http://localhost:30007

---

## APIs
- / : Dashboard UI 
- /status : Machine Status JSON 
- /health : Health check endpoint (used by Kubernetes) 

---

##  Key Features Implemented

- Dockerized Flask application
- Kubernetes Deployment with 2 replicas
- RollingUpdate strategy (maxSurge=1, maxUnavailable=0)
- Liveness & Readiness Probes
- Environment-based versioning
- NodePort exposure
- Zero downtime deployment
- Self-healing capability
- Horizontal scaling

---

##  Project Status

 1. Containerization Completed  
 2. Docker Hub Integration Completed  
 3. Kubernetes Deployment Completed 
 4. Rolling Updates Implemented  
 5. Self-Healing Verified  
 6. Scaling Verified
