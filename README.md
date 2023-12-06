# Introduction
In this project, we employ Machine Learning Models to accurately predict Sepsis of patients using an API built using the FastAPI framework. FastAPI provides a high-performance and easy-to-use platform for developing robust APIs with Python. This repository contains our ML Notebook, Datasets used to train the models, and links to access the API and a Web article.


## Description of the Dataset (Features)

| Column   Name                | Attribute/Target | Description                                                                                                                                                                                                  |
|------------------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID                           | N/A              | Unique number to represent patient ID                                                                                                                                                                        |
| PRG           | Attribute1       |  Plasma glucose|
| PL               | Attribute 2     |   Blood Work Result-1 (mu U/ml)                                                                                                                                                |
| PR              | Attribute 3      | Blood Pressure (mm Hg)|
| SK              | Attribute 4      | Blood Work Result-2 (mm)|
| TS             | Attribute 5      |     Blood Work Result-3 (mu U/ml)|                                                                                  
| M11     | Attribute 6    |  Body mass index (weight in kg/(height in m)^2|
| BD2             | Attribute 7     |   Blood Work Result-4 (mu U/ml)|
| Age              | Attribute 8      |    patients age  (years)|
| Insurance | N/A     | If a patient holds a valid insurance card|
| Sepssis                 | Target           | Positive: if a patient in ICU will develop a sepsis , and Negative: otherwise |

# Setup

Create a new virtual environment (venv) and activate the virtual environment, upgrade pip and install the required pacakages by running the following code:

- Windows:

        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:

        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt

## LinkedIn Article

## Screenshots of App
![Alt text](<Screenshot (31).png>)

![Alt text](<Screenshot (32).png>)

## Link to Deployed App
- https://hub.docker.com/repository/docker/pakornor/sepsis_api/general

# Author
- Philip Akornor