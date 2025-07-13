# Django Web App Deployment on AWS ECS

This repository demonstrates how to containerize a simple Django application and deploy it on AWS ECS (Fargate) using:

- Amazon ECR (Elastic Container Registry)  
- ECS Cluster with Fargate Launch Type  
- Load Balancer for traffic distribution  
- Auto Scaling Group for scalability  

---

## 🚀 What Was Done

### Containerization with Docker
- A `Dockerfile` was created to build the Django app image.
- The project was made compatible for containerization (adding `requirements.txt`, etc.)
- Docker image was tested locally using `docker run`.

### AWS ECR (Elastic Container Registry)
- Created an ECR repository to host the Docker image.
- Logged in to ECR and pushed the image.

### ECS Cluster Setup
- Created an ECS Cluster using the Fargate launch type.
- Defined a **Task Definition** pointing to the image on ECR.
- Created a **Service** in ECS that manages tasks and integrates with:
  - Application Load Balancer
  - Auto Scaling policies

### Networking & Load Balancing
- Configured:
  - VPC & Subnets
  - Security Groups to allow inbound HTTP traffic
- Set up a Load Balancer to route traffic to ECS tasks.

### Auto Scaling
- Added auto-scaling rules based on CPU usage.
- Enabled ECS Service Auto Scaling via Target Tracking policy.

---

## 🖼️ Screenshots

Screenshots included in the `aws/` folder cover:

- ECS Cluster  
- Task Definitions  
- Load Balancer Configuration  
- Auto Scaling Group  
- ECR Image Push  
- Container Logs & Errors  
- Successful deployment  

These visuals serve as documentation of the full deployment process.

---

## 🧽 Cleanup

To avoid unnecessary AWS charges, the following resources were terminated after deployment testing:

- ECS Cluster  
- Task Definitions  
- Load Balancer  
- Auto Scaling Group  
