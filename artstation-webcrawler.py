import requests
import json
import os
import re
import time

permalink = list()
img_link = list()
full_name = list()
artwork_name = list()
info_list = list()
img_link_bot = ""
artwork_name_bot = ""
title_db = list()
pages = ['1', '2', '3', '4', '5', '6']

if not os.path.exists('artstation'):
    os.makedirs('artstation', mode=0o777)
# move to new directory
os.chdir('artstation')


pass
counter = 0
url = 'https://www.artstation.com/projects.json?page=1&sorting=trending'
page = requests.get(url)
json_data = json.loads(page.text)


for data in json_data['data']:
	print("Image: ", counter)
	time.sleep(1)
	permalink.append(data['permalink'])
	img_link.append(data['cover']['medium_image_url'])
	full_name.append(data['user']['full_name'])
	artwork_name.append(data['title'])
	with open('link_db.txt', 'w') as filehandle:	
		json.dump(permalink , filehandle)
	
	with open('name_db.txt', 'w') as filehandle:	
		json.dump(full_name , filehandle)

	artwork_name_bot = data['title']
	clean_name = re.sub('[^A-Za-z0-9]+','', artwork_name_bot)
	title_db.append(clean_name)
	
	with open('title_db.txt', 'w') as filehandle:
		json.dump(title_db , filehandle)
	
	img_link_bot = data['cover']['medium_image_url']
		
	print(clean_name)
	img_link_bot = data['cover']['medium_image_url']
	img_file = requests.get(img_link_bot).content 
	with open("{}".format(counter) + "-" + clean_name + '.jpg', 'wb') as handler:
    		handler.write(img_file)
    		counter += 1
print(artwork_name)