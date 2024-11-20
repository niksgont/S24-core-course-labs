# Kubernetes Deployment

## Overview
This setup deploys the `web-app` application in a Minikube Kubernetes cluster, making it accessible via a Service.

## Resources
### Deployment
- Name: `web-app`
- Replicas: 2
- Image: `mydockerhubaccount/my_web_app:latest`

### Service
- Name: `web-app-service`
- Type: `NodePort`
- Ports: 80 -> 5000
Image is in the same folder.