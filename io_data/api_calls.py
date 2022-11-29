# API calls

# Imports
import requests as r
from settings import *

def weather_month_avg(start_month=None, end_month=None):
    
    location = "London,GB"
    url = f"https://history.openweathermap.org/data/2.5/aggregated/month?q={location}&appid={API_KEY}"
    req = r.get(url)
    print(req.json())
