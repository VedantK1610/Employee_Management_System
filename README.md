# Employee Management System

A simple Employee Management System built using Flask and MySQL. The application is containerized using Docker and automated using Jenkins CI/CD.

## Tech Stack

- Python Flask
- MySQL
- Docker
- Docker Compose
- Jenkins (Docker Container)
- GitHub Webhook

## Overview

This project demonstrates a complete DevOps workflow:

Developer → GitHub → Jenkins Container → Docker Build → Docker Compose Deployment → Flask + MySQL Containers

## Features

- Employee management CRUD operations
- Flask backend application
- MySQL database integration
- Docker containerization
- Automated CI/CD pipeline

## Project Structure

Employee_Management_System/
- backend/ - Flask application
- database/ - MySQL initialization files
- jenkins/ - Jenkins Docker setup
- docker-compose.yml - Application containers
- Jenkinsfile - CI/CD pipeline

## Run Application Locally

Clone repository:

git clone https://github.com/VedantK1610/Employee_Management_System.git

Go inside project:

cd Employee_Management_System

Start application:

docker compose up -d --build

Application:

http://localhost:5000

## Jenkins CI/CD Setup

Jenkins is running inside a Docker container.

Jenkins automatically triggers when code is pushed to GitHub using a webhook.

Pipeline steps:

1. Checkout latest code
2. Build Docker images
3. Stop old containers
4. Deploy updated containers using Docker Compose

## CI/CD Flow

Git Push → GitHub Webhook → Jenkins Pipeline → Docker Build → Docker Compose Deployment

## Completed

✔ Flask Application  
✔ MySQL Database  
✔ Docker Images  
✔ Docker Compose  
✔ Jenkins Container Setup  
✔ GitHub Webhook Integration  
✔ Automated Deployment Pipeline  

## Future Improvements

- Kubernetes Deployment
- Jenkins with Kubernetes
- Production deployment

## Author

Vedant K