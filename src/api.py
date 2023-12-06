from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import pandas as pd
import numpy as np
import joblib
import logging
 
logging.basicConfig(level=logging.DEBUG)
 
pipeline = joblib.load('./Model/pipeline3.joblib')
encoder = joblib.load('./Model/encoder.joblib')
 
app = FastAPI(
    title= "Sepsis Analysis API"
)
 
# Input Features
class SmartFeatures(BaseModel):
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance: int
   
@app.get('/')
def read_root():
    explanation = {
        'message': "Welcome to the Sepsis Analysis API",
        'description': "This API allows you to predict Sepsis based on patient data.",
        'usage': "Submit a POST request to predict patient data to make predictions."
    }
    return explanation
 
@app.post('/predict_Sepsis')
def predict_sepsis_infection(sepsis_features: SmartFeatures):
    try:
        df = pd.DataFrame([sepsis_features.model_dump()])
       
        predict = pipeline.predict(df)[0]
       
        if predict not in encoder.classes_:
            encoder.classes_ = np.append(encoder.classes_, predict)
            predict_encoder = encoder.inverse_transform([predict])[0]
           
           
        return {'Prediction': predict_encoder}
 
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="The Server is down! Please contact the administrator. Thank you.")