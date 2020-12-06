import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np

# getting scales from wikipedia with some webscraping
# TODO: save them as a dictionary for main
#  get name, intervals
#  convert interval values( W,H,3H) to steps as in H=1 W=2 (one step is a semitone)

url = 'https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes'
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")
table = soup.findAll('table')
rows = soup.findAll('tr')