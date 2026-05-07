import requests
import datetime
ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
api="591af82a8de698d4c882de05a01ca8d1"
CHAT_ID=5042249349
BOT_TOKEN="8740798913:AAEqQdidYoBB2VSQs5YXKBO-RW9WwzWtVG4"

latitude=22.4490371
longitude=88.3774292
weather_parameter={
    "lat":latitude,
    "lon":longitude,
    "appid":api,
    "cnt":4,
} #https://api.openweathermap.org/data/2.5/weather?lat=22.57&lon=88.36&appid=YOUR_API_KEY
response=requests.get(ENDPOINT,params=weather_parameter)
print(response.status_code)
weather_data=response.json()
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

now = datetime.datetime.now()
 
will_rain=False
for i in  range(weather_parameter["cnt"]):
    if 300<weather_data['list'][i]['weather'][0]['id'] < 600:
       will_rain=True
       break
if will_rain:  
    message="It is going to train,get an umbrella"    
   
else:
    message="no worry"
send_to={
    "chat_id":CHAT_ID,
    "text":message
}  
requests.get(url,params=send_to)
        
        