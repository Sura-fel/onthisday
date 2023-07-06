#!/data/data/com.termux/files/usr/bin/python
import datetime, json
from os import path as paths
from random import randint
import requests
today = datetime.datetime.now()
date = today.strftime('%m/%d')
file_name = today.strftime('%m.%d.json')
url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/' + date 
#headers = { 'Authorization': 'Bearer YOUR_ACCESS_TOKEN', 'User-Agent': 'YOUR_APP_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)' }
path = f'/data/data/com.termux/files/home/.local/tmp/{file_name}'
if not paths.exists(path):
	try :
		response = requests.get(url)#, headers=headers)
		data = response.json()
		dict_data = data['selected']
		print(data['selected'][0]['text'])
		with open(path, 'x') as file:
			json.dump(dict_data,file, indent=2)
	except ConnectionError:
		print('No Connection')
		exit()
		
with open(path,'r') as file:
	dict_data = json.load(file)
	#real_dict = json.dumps(dict_data,indent=2)
try:	
	i = randint(0,(len(dict_data) -1))
	print(dict_data[i]['pages'][0]['title'],'\n',dict_data[i]['text'],'\n',dict_data[i]['pages'][0]["content_urls"]['mobile']['page'])
	del dict_data[i]
	with open(path,'w') as file:
		json.dump(dict_data,file)
except ValueError:
	print('No more events on my database')
	exit()