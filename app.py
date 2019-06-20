from flask import Flask, render_template, redirect,url_for,flash,request,session,abort
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
import os
import json
import codecs
import requests
import joblib
import pandas as pd
import pickle
import datetime

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app=Flask(__name__, template_folder=tmpl_dir)
bootstrap = Bootstrap(app)
#ttn
url = "https://12345678901051.data.thethingsnetwork.org/api/v2/query?last=3d"
auth_header =  {"Accept":"application/json", "Authorization":"key ttn-account-v2.ZSvRze20imaAA-E_JJ2Td8cHWgtkW_uupFiSsokqdoY"}
response=requests.request("GET",url,headers=auth_header)
response=response.json()
# print(response)#whole dictionary
# def latest_data(response):#use this fun to get latest data
    # length=len(response)
    # global l
    # response[length-6]["humidity"]=6700
    # print(response[length-6]["humidity"])
    # l=response[length-1]["humidity"]
    # if l==None:
    #     for i in range(2,len(response)+1):
    #         # print(i)
    #         l=response[length-i]["humidity"]
    #         if l==None:
    #             continue
    #         else:
    #             print("l",l)
    #             break
    # l=l/1000
    # print("None")
    # l=
    # print(l)
    # return l

# response[length-1]["humidity"]=15300
# print(response[length-1]["humidity"])
# l=response[length-1]["humidity"]
# p=response[length-1]["pH"]/100
# a=response[length-1]["alk"]/100
# print(response)
# humidity=latest_data(response)
# print("\n Latest Humidity data",humidity)

length=len(response);ph1=[];tm1=[];temp1=[];alk1=[];sal1=[];i=0

# def getdata1():
#     for i in range(1,11):
#         l=[]
#         p=response[length-i]["pH"]
#         a=response[length-i]["alk"]
#         tm=response[length-i]["time"]
#         tm.split('.')
#         print(tm)
#         tt=int(response[length-i]["temp"])/1000000000
#         t=round(tt, 1)
#         tm1.append(tm)
#         temp1.append(t)
#         ph1.append(p)
#         alk1.append(a)
#         sal1=[13,19,23,22,20,17,19,21,21,20]
#     print(ph1,temp1,alk1,sal1)
#     return tm1,temp1,ph1,alk1
# re=getdata1()
# print(re)
# param1,param2,param3=getData1()
# print(param1,param2,param3)

parameters=[35,33,7.9]#(temp,salinity,pH) in this format
# machine learning Model

def mlmodel(parameters):
    with open("pickleb","rb") as j:
        model=pickle.load(j)
        j.close()
    scaler = joblib.load("scaler.sav")
    scaler1=joblib.load("scaler1.sav")
    # print("s")
    x=pd.DataFrame(scaler.transform([parameters]))
    pred=model.predict(x)
    pred=scaler1.inverse_transform(pred)
    print("Dissolved Oxygen",pred[0][0])
    return pred[0][0]
dissolvedoxygen1=mlmodel(parameters)


app.config['SECRET_KEY']='sofiya@123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Hp\\Documents\\prawn\\database.db'
db=SQLAlchemy(app)
#first data
p1=response[length-1]["pH"]
a1=response[length-1]["alk"]
tm1=response[length-1]["time"]
tm1=tm1.split("T")

tm1=tm1[1][0:5]
print(tm1)
# print()
# tm1=tmm1.time()
# tm=tm1.split(10:19)
# tt1=int(response[length-1]["temp"])/1000000000
# t1=round(tt1, 1)
t1=23
s1=21
dissolvedoxygen=5.6
#second data
p2=response[length-2]["pH"]
a2=response[length-2]["alk"]
tm2=response[length-2]["time"]
tm2=tm2.split("T")
tm2=tm2[1][0:5]

# tm=tm1.split(10:19)
# tt2=int(response[length-2]["temp"])/1000000000
# t2=round(tt2, 1)
t2=26
s2=20
dissolvedoxygen=4.4
#third data
p3=response[length-3]["pH"]
a3=response[length-3]["alk"]
tm3=response[length-3]["time"]
tm3=tm3.split("T")
tm3=tm3[1][0:5]
# tm=tm1.split(10:19)
# tt3=int(response[length-3]["temp"])/1000000000
# t3=round(tt3, 1)
t3=22
s3=23
dissolvedoxygen=4.7
#fourth data
p4=response[length-4]["pH"]
a4=response[length-4]["alk"]
tm4=response[length-4]["time"]
tm4=tm4.split("T")
tm4=tm4[1][0:5]
# tm=tm1.split(10:19)
# tt4=int(response[length-4]["temp"])/1000000000
# t4=round(tt4, 1)
t4=27
s4=21
dissolvedoxygen=4.6
#fifth data
p5=response[length-5]["pH"]
a5=response[length-5]["alk"]
tm5=response[length-5]["time"]
tm5=tm5.split("T")
tm5=tm5[1][0:5]
# tm=tm1.split(10:19)
# tt5=int(response[length-5]["temp"])/1000000000
# t5=round(tt5, 1)
t5=24
s5=21
dissolvedoxygen=4.3



def getData1():
    allData1=[]
    # readData=requests.get('http://api.thingspeak.com/channels/786644/feeds.json').json()
    allData1.append(tm1)
    allData1.append(t1)
    allData1.append(p1)
    allData1.append(a1)
    allData1.append(s1)
    # allData.append(readData['feeds'][-1]['field1'])
    # allData.append(readData['feeds'][-1]['field2'])
    # allData.append(readData['feeds'][-1]['field3'])
    allData1.append(dissolvedoxygen)
    return allData1
def getData2():
    allData2=[]
    # readData=requests.get('http://api.thingspeak.com/channels/786644/feeds.json').json()
    allData2.append(tm2)
    allData2.append(t2)
    allData2.append(p2)
    allData2.append(a2)
    allData2.append(s2)
    # allData.append(readData['feeds'][-1]['field1'])
    # allData.append(readData['feeds'][-1]['field2'])
    # allData.append(readData['feeds'][-1]['field3'])
    allData2.append(dissolvedoxygen)
    return allData2
def getData3():
    allData3=[]
    # readData=requests.get('http://api.thingspeak.com/channels/786644/feeds.json').json()
    allData3.append(tm3)
    allData3.append(t3)
    allData3.append(p3)
    allData3.append(a3)
    allData3.append(s3)
    # allData.append(readData['feeds'][-1]['field1'])
    # allData.append(readData['feeds'][-1]['field2'])
    # allData.append(readData['feeds'][-1]['field3'])
    allData3.append(dissolvedoxygen)
    return allData3
def getData4():
    allData4=[]
    # readData=requests.get('http://api.thingspeak.com/channels/786644/feeds.json').json()
    allData4.append(tm4)
    allData4.append(t4)
    allData4.append(p4)
    allData4.append(a4)
    allData4.append(s4)
    # allData.append(readData['feeds'][-1]['field1'])
    # allData.append(readData['feeds'][-1]['field2'])
    # allData.append(readData['feeds'][-1]['field3'])
    allData4.append(dissolvedoxygen)
    return allData4
def getData5():
    allData5=[]
    # readData=requests.get('http://api.thingspeak.com/channels/786644/feeds.json').json()
    allData5.append(tm5)
    allData5.append(t5)
    allData5.append(p5)
    allData5.append(a5)
    allData5.append(s5)
    # allData.append(readData['feeds'][-1]['field1'])
    # allData.append(readData['feeds'][-1]['field2'])
    # allData.append(readData['feeds'][-1]['field3'])
    allData5.append(dissolvedoxygen)
    return allData5

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(10),unique=True)
    deviceid = db.Column(db.String(10),unique=True)
    email=db.Column(db.String(50),unique=True)
    password= db.Column(db.String(50),unique=True)

class loginform(FlaskForm):
    username=StringField('Username', validators=[InputRequired(), Length(min=4, max=10)], render_kw={"placeholder":"Enter Username"})
    password=PasswordField('Password', validators=[InputRequired(), Length(min=8, max=50)],render_kw={"placeholder":"Enter Password"})
    # remember=BooleanField('Remember me')
class signupform(FlaskForm):
    username=StringField('Username', validators=[InputRequired(), Length(min=4, max=10)])
    deviceid=StringField('Device id',validators=[InputRequired(),Length(min=10)])
    email=StringField('Email  id',validators=[InputRequired(),Email(message='Invalid input'), Length(max=50)])
    password=PasswordField('Password',validators=[InputRequired(),Length(min=8, max=50)])

@app.route('/login', methods=['get','post'])
def login():
    form=loginform()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                return redirect(url_for('dashboard'))
        return 'Invalid username or password'
        # return  form.username.data + ' ' + form.password.data

    return render_template('index.html', form=form)
@app.route('/signup', methods=['get','post'])
def signup():
    form=signupform()

    if form.validate_on_submit():
        new_user = User(username=form.username.data, deviceid=form.deviceid.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
        # return  form.username.data + ' ' + form.email.data + ' ' + form.deviceid.data + ' ' + form.password.data

    return render_template('signup.html', form=form)

@app.route('/linechart')
def linechart():
    output1=getData1()
    output2=getData2()
    output3=getData3()
    output4=getData4()
    output5=getData5()
    return render_template('goocharts.html',**locals())


@app.route('/dashboard')
def dashboard():
    value=getData1()
    return render_template('in.html',**locals())


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
