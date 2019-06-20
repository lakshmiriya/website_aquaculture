# import pickle
# import pandas as pd
# file=open('pb','rb')
# print("p")
# model=pickle.load(file)
# print("b")
# file.close()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import joblib
import pickle

data=pd.read_csv("data.csv")

data=data[data["Mooring_Id"]=="A"]#second way but efficient
data=data[data.Water_Depth==7]
data=data[data.Temperature!=-9999]
data=data[data.Salinity!=-9999]
data=data[data.pH!=-9999]
l=["Mooring_Id","Site_Description","Latitude","Longitude","Start_Date","End_Date","Deployment_No","Water_Depth","Sensor_ID","Date","Time"]
data=data.drop(l,axis=1)

data["Temperature"]=data["Temperature"]+16
y_data=data["Oxygen"]
data=data.drop("Oxygen",axis=1)

print("half")
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_data=pd.DataFrame(scaler.fit_transform(data))

scaler1 = StandardScaler()
y_data=(scaler1.fit_transform(y_data.values.reshape(-1,1)))

joblib.dump(scaler,"scaler.sav")
joblib.dump(scaler1,"scaler1.sav")

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.1,random_state=0)

# print(x_train.iloc[1:10,1])
from sklearn import neighbors
model = neighbors.KNeighborsRegressor(n_neighbors =8,n_jobs=-1)
model.fit(x_train, y_train)
print(model.score(x_train,y_train))#best model

y_predict = model.predict(x_test)

y_test=scaler1.inverse_transform(y_test)
y_predict=scaler1.inverse_transform(y_predict)

print(y_test[210])
print(y_predict[210])

with open("pickleb","wb") as p:
    pickle.dump(model,p)
    p.close()


with open("joblibb", "wb") as j:
    joblib.dump(model,j)
    j.close()

print("end")
