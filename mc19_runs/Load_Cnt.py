
from bs4 import BeautifulSoup as bs
from bs4 import *
import requests
import os
from textparser import *
import wget

import tweepy 
import webbrowser
import pandas as pd


consumer_key = "BGK0F5EWsbpypm6w59hFBHzOw"
consumer_secret ="0Z38Oy747x4A83EZirdX5h6SGlDIUfAJ7wRxjLsi0B5REkkrta"
access_token = "1375070617448423428-IrNB2BAP2KLUXBFv4yyE95eH4mZYvm"
access_token_secret ="p2uSfFvL8Ch7XUIcVnW8UiNUUhV0awQ1UCcyIptIv0ZLc"

#callback_uri ='oob' #https://twitter.com/APS_Officiel/status/1374674907376857088
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#ID = 1186628409524404226
#status = api.get_status(1186628409524404226)


for status in tweepy.Cursor(api.home_timeline, screen_name = "@MinisteredelaS1").items(1186628409524404226):
	print(status.text)

