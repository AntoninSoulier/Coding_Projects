"""
import adafruit_dht

from datetime import datetime
from time import strftime

dht = adafruit_dht.DHT11(board.D2)

import csv

#Read values from DHT11 sensor and store the values in a CSV file
with open('Projet_Final/data.csv','w') as f:
    label = ['Temperature', 'Humidity', 'Date', 'Time']
    writer = csv.writer(f)
    writer.writerow(label)
while True:
    try:
        data = []
        temperature = dht.temperature
        humidity = dht.humidity
        data.append(temperature)
        data.append(humidity)
        data.append(datetime.today().strftime('%Y-%m-%d'))
        data.append(datetime.today().strftime('%H:%M:%S'))
        with open('Projet_Final/data.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    except RuntimeError as e:
        print("Reading from DHT failure: ", e.args)
"""

#Import libraries
from time import time
from tkinter import Y
import matplotlib.pyplot as plt
import http.client as httplib2
import numpy as np
import urllib
import csv
from twilio.rest import Client

#Function to send data to Thing Speak Cloud

def thermometer(temperature):
    key = "Z2W2ZDENXCPD3UY4"
    while True:
        temp = temperature
        params =  urllib.parse.urlencode({'field1': temp, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib2.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print("Value " + temp + " sent to ThingSpeak!")
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("Connection failed")
        break

#Function to send text message to my own phone

def sendTextMessage(text):
    account_sid = "AC0377d0ca8d0fc552668de72938e37048"
    auth_token = "714093711604a69f8288d00d0ee51fb5"
    alert = "Temperature is exceeding " + str(text) + " degrees !"
    client = Client(account_sid, auth_token)
    message = client.api.account.messages.create(to="+33778685057",from_="+15672294714",body=alert)

import twitter

def sendTweet(text):
    auth = twitter.OAuth(consumer_key="aaY1e536Lp44Apytesb7ZJ9L6",
                         consumer_secret="xNgN1d9dg6U7MORfyF3ZAMOPISR2sGutZtU0K3obMK5gO1qGHB",
                         token="1485564928169857024-eEa2vMvp49B2Ej4bbCad6nVboA1q67",
                         token_secret="LkFPD43ultdOqT7tlI1v2Nslw0fDdH2Cj4uQTXsH7s1eX"
                        )
    tweet = twitter.Twitter(auth=auth)

    alert = "Temperature is exceeding " + str(text) + " degrees !"

    #Publish
    tweet.statuses.update(status=alert)

#Read values from a CSV file

with open("Projet_Final/data.csv") as d:
	reader = csv.reader(d)
	data = [ line for line in reader ]

data = np.array(data) #array containing all data

temperature = []
humidity = []
time_values = []

for i in range(1,len(data)):
    temperature.append(data[i][0]) #Temperature
    if(float(data[i][0]) > 32):
        thermometer(data[i][0])    #send value to ThingSpeak if temperature > 32
        sendTextMessage(data[i][0])            
        sendTweet(data[i][0])                
    humidity.append(data[i][1])    #Humidity
    time_values.append(data[i][2] + "\n at \n" + data[i][3]) # date and time | "\n" to gain space on the x axis when I display the values on the graph

temperature = list(map(float, temperature))
humidity = list(map(float, humidity))

#Function to draw a graph
def drawGraph(time_values,variable,label):
    fig = plt.figure()
    plt.plot(time_values,variable)
    plt.title(label + " over time", fontweight="bold")
    plt.xlabel("Date/Time")
    plt.ylabel(label)
    fig.set_figheight(8)
    fig.set_figwidth(12)
    plt.show()

"""#Draw temperatures over time 
drawGraph(time_values,temperature,"Temperature")

#Draw humdidity over time
drawGraph(time_values,humidity,"Humidity")"""

#Function to calculate average temperature
def calc_avg_temp():
    average = sum(temperature)/len(temperature)
    if(average > 32):
        print("Switching on AC")
    else:
        print("Switching off AC")

calc_avg_temp()

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
from math import sqrt
import pandas as pd

# function AMIRA model
def arima_model(temperature):
    X = temperature
    size = int(len(X) * .44)

    train, test = X[0:size], X[size:len(X)]

    h = [x for x in train]
    pred = list()
    length = len(test)
    for value in range(length):
        model = ARIMA(h,order=(1,1,0))
        model_fit = model.fit()
        res = model_fit.forecast()
        predicted = res[0]
        pred.append(predicted)
        expected = test[value]
        h.append(expected)
        print("predicted: " + str(predicted) + "   expected: " + str(expected))

    print("test: " + str(test))
    print("pred: " + str(pred))
    print("expected: " + str(h))

    rmse = sqrt(mean_squared_error(test, pred))
    print("RMSE = " + str(round(rmse,6)) + " (which is quite good)")

    return(pred)


#Draw the temperature predictions on a graph

from datetime import timedelta, date
dates_values = []
predictions = arima_model(temperature)

#Starting from the day you execute the code, it predicts the temperatures for the next 7 days
for i in range(1,len(predictions)+1):
    Date_required = date.today() + timedelta(days=i)
    dates_values.append(Date_required)

#drawGraph(dates_values,predictions,"Temperature predictions")

#sendTextMessage(32)
sendTweet(32)