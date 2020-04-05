import os
from twython import Twython

API_KEY = os.getenv("API_KEY", "YOUR TWITTER API KEY")
API_SECRET = os.getenv("API_SECRET", "YOUR TWITTER API SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "YOUR TWITTER ACCESS TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET", "YOUR TWITTER ACCESS TOKEN SECRET")

print(ACCESS_TOKEN)
print(ACCESS_TOKEN_SECRET)
twitter_client = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter_client.update_status(status="Hello World!")
