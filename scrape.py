import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np


# getting scales from wikipedia with some webscraping
#  get name, intervals
#  convert interval values( W,H,3H) to steps as in H=1 W=2 (one step is a semitone)

def get_scales_from_wiki():
    url = 'https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes'
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")
    rows = soup.findAll('tr')
    scales = dict()

    for i, row in enumerate(rows[1:66]):
        columns = row.findAll('td')
        scale_name = columns[0].text
        intervals = columns[4].text
        if intervals.strip() == "—" or "Q" in intervals:  # skipping scales with no interval values or with quarter notes
            continue
        scales[scale_name] = intervals.strip().replace("(", "").replace(")", "")
    return scales


# seems like melodic minor has  a descending and an ascending value
# octatonic has two modes
# Istrian scale has 2 notes missing
def fix_melodic_and_octatonic(scales):
    interval = scales.pop('Melodic minor scale')
    scales['Melodic minor scale (descending)'] = interval.split('\n')[1][:13]
    intervals = scales.pop('Octatonic scale')
    scales['Octatonic (Mode 1)'] = intervals.split('\n\n')[0]
    scales['Octatonic (Mode 2)'] = intervals.split('\n\n')[1]
    scales['Istrian'] = 'H-W-H-W-H'
    return scales

def convert2step(note):
    if note == 'H':
        return 1
    elif note == "W":
        return 2
    else:
        coef = int(note[0])
        return coef*convert2step(note[1])

def notes2steps(scales):
    scales_with_steps = dict()
    for scale in scales:
        intervals = scales[scale]
        steps = [0]
        for note in intervals.split('-')[:-1]:
            base = steps[-1]
            steps.append(base + convert2step(note))
        scales_with_steps[scale.replace(" scale", "").strip()] = steps
    return scales_with_steps

def get_scales():
    wiki_scales = get_scales_from_wiki()
    fixed_scales = fix_melodic_and_octatonic(wiki_scales)
    scales_with_steps = notes2steps(fixed_scales)
    return scales_with_steps

