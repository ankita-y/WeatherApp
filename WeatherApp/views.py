from django.http import response
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
import requests
from datetime import datetime

api_key = "your API key"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Create your views here.
def home(request):
    
    if request.method == "GET":
        city_name = request.GET.get('search') or ''
        complete_url = base_url + "q="+ city_name + "&appid=" + api_key
        output = requests.get(complete_url)
        output_json = output.json()
        print(output_json)
        now = datetime.now()
        dt_string = now.strftime(" %d/%m/%Y %H:%M:%S")
   
        data ={
                "date":dt_string,
                "country_code":"NA/-",
                "city":"NA/-",
                "temp":"NA/-",                
                "humidity": "NA/-",
                "pressure":"NA/-",
                "description": "NA/-",
            }
        
        if city_name is not '':        
            if str(output_json["cod"]) == "200":

                x = output_json["main"]
                temp = output_json['main']['temp']
                temp = round(temp - 272.15,2)
                data = {
                    "date":dt_string,
                    "country_code":str(output_json['sys']['country']),
                    "city":str(output_json['name']),
                    "temp":str(temp)+"°",                
                    "humidity": str(output_json['main']['humidity'])+"%",
                    "pressure":str(output_json['main']['pressure'])+"mBar",
                    "description":output_json['weather'][0]['description'],
                }
                print(data)
        return render(request,'home.html',data)
    else:
        return render(request,'home.html')
