# Kubernetes Helm CI/CD

An intermediate-level DevOps project demonstrating containerized application deployment to Kubernetes using Helm and GitHub Actions.

## Architecture

Developer
    |
    v
GitHub
    |
    v
GitHub Actions
    |
    +--> Python Tests
    |
    +--> Docker Build
    |
    +--> Docker Hub Push
    |
    +--> Helm Lint
    |
    +--> Helm Template
    |
    v
Kubernetes
    |
    v
Helm Deployment
    |
    +--> Deployment
    |
    +--> Service
    |
    +--> Liveness Probe
    |
    +--> Readiness Probe


## Technologies

- Python
- Flask
- Docker
- Docker Hub
- Kubernetes
- Helm
- GitHub Actions
- pytest


## Features

- Flask REST API
- Dockerized application
- Kubernetes Deployment
- Kubernetes Service
- Helm chart
- Two application replicas
- Rolling updates
- Liveness probe
- Readiness probe
- CPU and memory resource limits
- Automated Python tests
- Automated Docker image build
- Docker Hub image push
- Helm chart validation


## Project Structure

```text
k8s-helm-cicd/
├── app/
│   ├── __init__.py
│   └── app.py
├── tests/
│   └── test_app.py
├── helm/
│   └── k8s-helm-cicd/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── _helpers.tpl
│           ├── deployment.yaml
│           └── service.yaml
├── .github/
│   └── workflows/
│       └── pipeline.yml
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
