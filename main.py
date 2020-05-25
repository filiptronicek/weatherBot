from pyowm import OWM
import os
from creds import API_key, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
from twython import Twython

owm = OWM(API_key)
obs = owm.weather_at_place('Prague,CZ')
w = obs.get_weather()
weather = w.get_status().lower()

twitter_api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

tstatus = ""

if weather == "sunny":
    tstatus = "Yes, it is sunny @vlada_svoboda @filiptronicek"
else:
    tstatus = "No, the weather is "+weather+" @vlada_svoboda @filiptronicek"
twitter_api.update_status(status=tstatus)