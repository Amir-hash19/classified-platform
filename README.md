# Classified Platform

A containerized classified advertisements platform built with Django REST Framework and PostgreSQL, progressively deployed and operated on Kubernetes.

## 📖 Overview

This project is a backend implementation of a classified ads platform (similar to Divar/Craigslist). It allows users to post advertisements, browse categories, and manage accounts.

The primary focus of this repository is the **DevOps lifecycle**, demonstrating a complete CI/CD pipeline, containerization, and orchestration using Kubernetes.

## 🛠 Tech Stack

- **Backend:** Python, Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose
- **Orchestration:** Kubernetes (K8s)
- **CI/CD:** GitHub Actions
- **Code Quality:** Black, Isort, Ruff (Linting)

## 🏗 Architecture & DevOps Features

This project is fully containerized and designed to run on a Kubernetes cluster.

### Kubernetes Resources
The manifests are located in the `k8s/` directory and include:
- **Deployment:** Manages the application pods with **3 replicas** for high availability.
- **StatefulSet:** Manages the PostgreSQL database to ensure stable network identities and persistent storage.
- **Service:**
  - `NodePort` for exposing the application to external traffic.
  - `ClusterIP` for internal database communication.
- **ConfigMap & Secrets:** Externalized configuration and sensitive data (DB credentials, Secret Keys) management.
- **Health Checks:** Configured **Liveness** and **Readiness** probes via dedicated endpoints (`/health/`) to ensure traffic is only routed to healthy pods.

### CI/CD Pipeline (GitHub Actions)
The CI pipeline ensures code quality and consistency before merging:
- **Linting:** Runs `Ruff` for fast Python linting.
- **Formatting:** Checks code style with `Black` and `Isort`.
- **Docker Build:** Validates the Dockerfile build process.

## 🚀 Getting Started

You can run this project either locally using **Docker Compose** (recommended for development) or deploy it to a **Kubernetes** cluster (recommended for production/staging).

### Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/install/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/) (Kubernetes CLI)
- A running Kubernetes cluster (e.g., [Minikube](https://minikube.sigs.k8s.io/docs/start/), [Kind](https://kind.sigs.k8s.io/), or a cloud provider like GKE/EKS)
- [Git](https://git-scm.com/)

---

### 🐳 Option 1: Running with Docker Compose (Local Development)

This is the fastest way to get the project up and running on your local machine.

**1. Clone the repository:**
```bash
git clone https://github.com/Amir-hash19/classified-platform.git
cd classified-platform
docker-compose up 
or docker-compose down