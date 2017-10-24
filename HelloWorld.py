import requests
from bs4 import BeautifulSoup
from pprint import pprint

#Setting up Requests
url = "https://pitchfork.com/artists/"
page = requests.get(url)

#Setting up Beautiful Soup
soup = BeautifulSoup(page.text, "html.parser")

#Testing for a response
print("Testing for a response:")
print(page.status_code)

if page.status_code == 200:
    print("Good to go.")
else:
    print("Something went wrong on their end.")

#Printed trending artists results
trending_artists = soup.find_all(class_="artist-image__name")
print("Currently trending artists")
pprint(trending_artists)