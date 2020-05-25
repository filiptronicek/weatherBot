from pyowm import OWM
from twython import Twython
from os import environ

if environ.get('API_key') is None:
    from creds import API_key, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
else:
    API_key = environ.get('API_key')
    CONSUMER_KEY = environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = environ.get('CONSUMER_SECRET')
    ACCESS_KEY = environ.get('ACCESS_KEY')
    ACCESS_SECRET = environ.get('ACCESS_SECRET')

owm = OWM(API_key)
obs = owm.weather_at_place('Prague,CZ')
w = obs.get_weather()
weather = w.get_status().lower()

twitter_api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

tstatus = ""

if weather == "sunny":
    tstatus = "Yes, it is sunny"
else:
    tstatus = "No, the weather is "+weather
twitter_api.update_status(status=tstatus)