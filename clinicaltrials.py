import bs4
from collections import defaultdict    
from bs4 import BeautifulSoup    
import requests

def clinicalTrialsGov(nctid):
    data = defaultdict(list)
    soup = BeautifulSoup(requests.get("https://clinicaltrials.gov/ct2/show/" + nctid + "?displayxml=true").text, "xml")
    subset = ['name','country','city','state','zip']
    for tag in soup.find_all(subset):
        data['ct{}'.format(tag.name.capitalize())].append(tag.get_text(strip=True))

    for key in data:
        print('{}: {}'.format(key, ', '.join(data[key])))

clinicalTrialsGov('NCT01592370')