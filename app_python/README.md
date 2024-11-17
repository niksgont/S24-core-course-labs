# Moscow Time Web Application

## Overview
This web application displays the current time in Moscow. It is built using Python and the Flask framework.

## Features
- Displays the current time in Moscow.
- Refresh the page to get the latest time.

## Requirements
- Python 3.x
- Flask

## Installation
1. Run the app:
    python app_python/app.py

## Docker Instructions

### Build the Image
docker pull niksgont/flask-moscow-time:latest
### Pull from Docker Hub
docker build -t flask-moscow-time .
### Run
docker run -p 5000:5000 flask-moscow-time

## Unit Tests
Run the unit tests using the following command:
```bash
python -m unittest test_app.py

## CI Workflow

### Overview
This project uses GitHub Actions for continuous integration.

### CI Steps
1. **Dependencies**: Installs required Python packages.
2. **Linter**: Checks code quality using `flake8`.
3. **Unit Tests**: Runs automated tests using `unittest`.
4. **Docker**: Logs into Docker Hub, builds the image, and pushes it to the repository.
