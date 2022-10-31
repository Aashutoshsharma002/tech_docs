import m3u8
import requests

url = "https://s3.amazonaws.com/vooplayerv4-111621/111621720-e.m3u8"

data = requests.get(url)
# print(data.text)

master_m3u8 = m3u8.loads(data.text)
segment = master_m3u8.data['segments'][0]['uri']
print(master_m3u8.data)
print(segment) #print data
