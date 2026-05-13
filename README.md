# Secure Notes DevSecOps Platform

## Overview

Secure Notes is a microservices-based DevSecOps project designed to demonstrate a complete Secure Software Development Lifecycle (Secure SDLC) pipeline using modern DevOps and security tools.

The project automates:

* Continuous Integration (CI)
* Continuous Delivery/Deployment (CD)
* Static Code Analysis
* Secret Detection
* Container Vulnerability Scanning
* Kubernetes Deployment
* Security Monitoring
* Log Aggregation
* Automated Security Testing
* Intrusion Prevention

The entire workflow is integrated using Jenkins pipelines triggered automatically through GitHub webhooks.

---

# Architecture

## Microservices

The application consists of three independent services:

| Service       | Description                               |
| ------------- | ----------------------------------------- |
| Auth Service  | Handles authentication-related operations |
| Notes Service | Handles secure note management            |
| Audit Service | Stores and tracks audit logs              |

---

# Tech Stack

## DevOps & CI/CD

* Jenkins
* GitHub Webhooks
* Docker
* Docker Compose
* Kubernetes (Minikube)
* Ansible

## Security Tools

* SonarQube
* GitLeaks
* Trivy
* OWASP ZAP
* Fail2Ban
* Ansible Vault

## Monitoring & Logging

* Prometheus
* Grafana
* Loki
* Promtail
* cAdvisor

---

# Project Structure

```bash
.
├── ansible
├── auth-service
├── notes-service
├── audit-service
├── docker-compose.yml
├── Jenkinsfile
├── monitoring
├── logging
├── nginx
├── security
└── README.md
```

---

# DevSecOps Pipeline Workflow

## 1. GitHub Webhook Trigger

Every git push automatically triggers the Jenkins pipeline using GitHub webhooks and ngrok tunneling.

---

## 2. Source Code Checkout

Jenkins clones the latest code from GitHub.

---

## 3. SonarQube Static Analysis

The pipeline performs static code analysis to detect:

* Code smells
* Bugs
* Security vulnerabilities
* Reliability issues

A customized Quality Gate is used for the project.

---

## 4. GitLeaks Secret Detection

GitLeaks scans the repository for:

* Hardcoded passwords
* API keys
* Secrets
* Tokens

Sensitive files are protected using `.gitignore` and Ansible Vault.

---

## 5. Docker Image Build

Separate Docker images are built for:

* auth-service
* notes-service
* audit-service

---

## 6. Trivy Vulnerability Scanning

Trivy scans container images for:

* Critical vulnerabilities
* High severity CVEs
* OS package vulnerabilities

The pipeline blocks deployment if critical vulnerabilities are detected.

---

## 7. Kubernetes Deployment Using Ansible

Ansible automates Kubernetes deployment using reusable roles.

Features:

* Infrastructure as Code
* Modular automation
* Kubernetes deployment automation
* Secret handling using Ansible Vault

Kubernetes resources include:

* Deployments
* Services
* Horizontal Pod Autoscaler (HPA)

---

## 8. OWASP ZAP Security Testing

OWASP ZAP performs automated Dynamic Application Security Testing (DAST) after deployment.

It scans for:

* Security misconfigurations
* Insecure headers
* Common web vulnerabilities

---

# Monitoring Stack

## Prometheus

Used for metrics collection.

---

## Grafana

Used for dashboard visualization.

---

## cAdvisor

Used for container-level monitoring and metrics.

---

# Logging Stack

## Loki + Promtail

Centralized logging is implemented using:

* Loki
* Promtail

Nginx access logs are collected and visualized through Grafana.

---

# Security Hardening

## Nginx Reverse Proxy

Security headers configured:

* X-Frame-Options
* X-Content-Type-Options
* X-XSS-Protection
* Cache-Control

Server tokens are disabled to hide Nginx version information.

---

## Fail2Ban Intrusion Prevention

Fail2Ban monitors Nginx access logs and automatically bans IP addresses generating excessive failed requests.

Implemented Features:

* Custom Fail2Ban filter
* Automated IP banning
* Protection against malicious traffic
* Log-based intrusion prevention

---

## Ansible Vault

Secrets are encrypted using Ansible Vault.

Example use cases:

* Database credentials
* API keys
* Sensitive configuration values

---

# Innovation Implemented

## Automated Intrusion Prevention with Fail2Ban

As an additional security innovation, the project integrates Fail2Ban with Nginx logs to automatically detect and block suspicious traffic patterns.

This demonstrates:

* Real-time security response
* Automated attack mitigation
* Security monitoring integration

---

# Kubernetes Features

## Horizontal Pod Autoscaler (HPA)

The application supports auto-scaling based on resource utilization.

Benefits:

* High availability
* Better scalability
* Improved fault tolerance

---

# CI/CD Pipeline Stages

| Stage              | Purpose                           |
| ------------------ | --------------------------------- |
| Clone              | Fetch latest code                 |
| SonarQube Analysis | Static code analysis              |
| GitLeaks Scan      | Secret detection                  |
| Build Docker Image | Containerization                  |
| Trivy Scan         | Vulnerability scanning            |
| Deploy Containers  | Kubernetes deployment via Ansible |
| OWASP ZAP Scan     | Dynamic security testing          |
| Email Notification | Pipeline status alerts            |

---

# Email Notifications

Jenkins automatically sends:

* Success notifications
* Failure alerts

with:

* Build number
* Build URL
* Pipeline status

---

# Screenshots included
<img width="1798" height="904" alt="image" src="https://github.com/user-attachments/assets/91c73c6c-451c-47b4-9b9b-7be9a9e013c2" />

* Jenkins pipeline
* SonarQube dashboard
* Grafana dashboards
* Kubernetes pods
* OWASP ZAP scan
* Fail2Ban banning demonstration
* Loki logs in Grafana

---

# How to Run the Project

## Start Infrastructure

```bash
sudo systemctl start docker
minikube start
```

---

## Start Monitoring Stack

```bash
docker compose -f monitoring-compose.yml up -d
```

---

## Run Jenkins Pipeline

Push changes to GitHub:

```bash
git add .
git commit -m "update"
git push
```

The Jenkins pipeline will automatically trigger.

---

# Future Improvements

Possible future enhancements:

* Helm charts
* ArgoCD GitOps deployment
* ELK Stack integration
* Terraform infrastructure provisioning
* JWT authentication
* Frontend UI
* Automated unit testing
* Kubernetes Ingress Controller

---

# Learning Outcomes

This project demonstrates practical implementation of:

* Secure SDLC
* DevSecOps pipelines
* Container security
* Infrastructure as Code
* Kubernetes orchestration
* Monitoring and logging
* Security automation
* CI/CD workflows

---

# Authors
Md Maroof Hasan Khan and Piyush Singh
Developed as part of the Software Production Engineering (SPE) course project.

---

# License

This project is intended for educational and academic purposes.

