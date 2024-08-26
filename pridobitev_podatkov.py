

import json
import requests
import bs4

url = "https://olympics.com/en/paris-2024/medals/medallists"

r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html = r.content

soup = bs4.BeautifulSoup(html, "html.parser")

data = json.loads(soup.find("script", type="application/json").string)

atleti = []
for athlete in data["props"]["pageProps"]["initialMedallist"]["athletes"]:
    athlete.pop('code')
    athlete.pop('initialName')
    athlete.pop('tvName')
    athlete.pop('tvInitialName')
    athlete.pop('extraData')
    athlete.pop('organisationName')
    for medalje in athlete['medals']:
        medalje.pop('event')
        medalje.pop('date')
        medalje.pop('disciplineCode')
        medalje.pop('official')
        medalje.pop('extraData')
    #print(athlete)
    atleti.append(athlete)

#print(atleti)