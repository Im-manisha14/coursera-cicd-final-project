# Coursera CI/CD Final Project

## Project objective

This project demonstrates a complete CI/CD workflow for a small Flask application. GitHub Actions performs linting and unit tests, while Tekton provides reusable tasks and a pipeline for OpenShift.

## Technologies

- Python
- Flask
- GitHub Actions
- flake8
- nose
- Tekton
- Red Hat OpenShift
- YAML

## Project structure

```text
app.py                    Flask application
test_app.py               Unit tests
requirements.txt          Python dependencies
Dockerfile                OpenShift-compatible container image
.github/workflows/        GitHub Actions workflow
.tekton/                  Tekton tasks and pipeline
openshift/                Deployment, service, and PVC resources
```

## Install dependencies

Create and activate a virtual environment, then install the pinned dependencies:

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell:
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the application

```bash
python app.py
```

Open <http://localhost:8080/> in a browser.

## Run linting and unit tests

```bash
flake8 app.py test_app.py
nosetests -v
```

## GitHub Actions

The workflow in `.github/workflows/workflow.yml` runs for pushes and pull requests. It checks out the repository, sets up Python, installs dependencies, runs flake8, and executes the nose test suite.

## Tekton and OpenShift

The `.tekton/tasks.yml` file defines cleanup and nose test tasks. `.tekton/pipeline.yml` connects those tasks in the `oc-pipelines-oc-final` pipeline. The resources under `openshift/` define a PVC, a deployment, and a service.

Replace the example image in `openshift/deployment.yaml` with an image available to your OpenShift cluster before applying it. Cluster login, image publishing, resource creation, and pipeline execution require access to a real OpenShift cluster and are intentionally not represented as successful here.
