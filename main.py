from pyowm import OWM
from twython import Twython
from os import environ
import random

sayings = ["lol", "lmao", "lmfao", "... very epic", "(laugh now)", "- so exciting indeed", "... now this is getting awkward",". I blame it on politics", ". Poggers" ]

if environ.get('API_key') is None:
    from creds import API_key, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
else:
    API_key = environ.get('API_key')
    CONSUMER_KEY = environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = environ.get('CONSUMER_SECRET')
    ACCESS_KEY = environ.get('ACCESS_KEY')
    ACCESS_SECRET = environ.get('ACCESS_SECRET')

owm = OWM(API_key)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('Prague,CZ')
w = obs.weather
weather = w.status.lower()

twitter_api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

tstatus = ""

if weather == "sunny":
    tstatus = "Yes, it is sunny"
elif weather == "thunderstorm":
    tstatus = "It's like the upposite of sunny. It's raining lighting bolts!"
else:
    tstatus = "No, the weather is "+weather

def tweet():
    try:
        twitter_api.update_status(status=tstatus+" "+random.choice(sayings))
    except Exception:
        tweet()


tweet()
