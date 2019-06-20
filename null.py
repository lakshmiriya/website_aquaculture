#Data from thingsnetwork
import requests
url = "https://12345678901051.data.thethingsnetwork.org/api/v2/query?last=2d"
auth_header =  {"Accept":"application/json", "Authorization":"key ttn-account-v2.ZSvRze20imaAA-E_JJ2Td8cHWgtkW_uupFiSsokqdoY"}
response=requests.request("GET",url,headers=auth_header)
response=response.json()
# print(response)#whole dictionary
# def latest_data(response):#use this fun to get latest data
length=len(response)
    # global l
# response[length-1]["humidity"]=15300
# print(response[length-1]["humidity"])
# l=response[length-1]["humidity"]
p=response[length-1]["pH"]
a=response[length-1]["alk"]
t=response[length-1]["temp"]/100
print(response)
print(response[0])
    # if l==None:
    #     for i in range(2,len(response)+1):
    #         print(i)
    #         l=response[length-i]["humidity"]
    #         if l==None:
    #             continue
    #         else:
    #             print("l",l)
    #             break
# l=l/1000
    # print("None")
# print(l)
z=[]


# humidity=latest_data(response)
print("\n Latest Humidity data",t,p,a)



# machine learning Model
# import joblib
# import pickle
# import pandas as pd
# parameters=[31,33,7.9]
# def mlmodel(parameters):
#     with open("pickleb","rb") as j:
#         model=pickle.load(j)
#         j.close()
#     scaler = joblib.load("scaler.sav")
#     scaler1=joblib.load("scaler1.sav")
#     # print("s")
#     x=pd.DataFrame(scaler.transform([parameters]))
#     pred=model.predict(x)
#     pred=scaler1.inverse_transform(pred)
#     print("Dissolved Oxygen",pred[0][0])
#     return pred[0][0]
# dissolvedoxygen=mlmodel(parameters)
