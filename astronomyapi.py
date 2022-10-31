import requests


url = "https://astronomy.p.rapidapi.com/api/v2/studio/moon-phase"

payload = {
    "format": "png",
    "observer": {
        "date": "2020-11-01",
        "latitude": 6.56774,
        "longitude": 79.88956
    },
    "style": {
        "backgroundColor": "red",
        "backgroundStyle": "stars",
        "headingColor": "white",
        "moonStyle": "sketch",
        "textColor": "red"
    },
    "view": {
        "type": "portrait-simple"
    }
}
headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY",
    'x-rapidapi-host': "astronomy.p.rapidapi.com"
    }

response = requests.get(url, data=payload, headers=headers)

print(response.text)
