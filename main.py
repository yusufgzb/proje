# fastapi model servisi
from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel


app = FastAPI()
model = joblib.load('model_best_9986.pkl')

# veri modeli
class Data(BaseModel):
    sensor_1: float
    sensor_2: float
    sensor_3: float
    sensor_4: str
    sensor_5: str
    sensor_6: float
    sensor_7: float
    sensor_8: float
    sensor_9: float
    sensor_10: float
    sensor_11: float
    sensor_12: float
    sensor_13: float
    sensor_14: float
    sensor_15: float
    sensor_16: float
    sensor_17: float
    sensor_18: float
    sensor_19: float
    sensor_20: float
    sensor_21: float
    sensor_22: float
    sensor_23: float
    sensor_24: float
    sensor_25: float
    sensor_26: float
    sensor_27: float
    sensor_28: float
    sensor_29: float
    sensor_30: float
    sensor_31: float
    sensor_32: float


@app.post('/predict')
def get_predict(data: Data):
    try:
        sensor_4 = float(data.sensor_4)
        sensor_5 = float(data.sensor_5)
        print("veri okundu")
    except:
        return {'type': 'Error'}        
    
    data = np.array([data.sensor_1, data.sensor_2, data.sensor_3, sensor_4, sensor_5, data.sensor_6, data.sensor_7, data.sensor_8, data.sensor_9, data.sensor_10, data.sensor_11, data.sensor_12, data.sensor_13, data.sensor_14, data.sensor_15, data.sensor_16, data.sensor_17, data.sensor_18, data.sensor_19, data.sensor_20, data.sensor_21, data.sensor_22, data.sensor_23, data.sensor_24, data.sensor_25, data.sensor_26, data.sensor_27, data.sensor_28, data.sensor_29, data.sensor_30, data.sensor_31, data.sensor_32]).reshape(1, -1)
 
    try:
        prediction = model.predict(data)
    except:
        return {'prediction': 'Error'}
    return {'prediction': prediction[0]}


