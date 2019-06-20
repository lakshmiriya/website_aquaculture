import joblib
import pandas as pd
parameters=[35,33,7.9]#(temp,salinity,pH) in this format

def mlmodel(parameters):
    Saved_model=joblib.load("Water_quality.pkl")
    scaler = joblib.load("scaler.sav")
    scaler1=joblib.load("scaler1.sav")

    x=pd.DataFrame(scaler.transform([parameters]))
    print(x)
    pred=Saved_model.predict(x)
    p=scaler1.inverse_transform(pred)
    print("Dissolved Oxygen",p)
    return pred
dissolvedoxygen=mlmodel(parameters)
print(dissolvedoxygen)
