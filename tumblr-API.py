import pytumblr
import json
import time
import os
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    
    return [ atoi(c) for c in re.split('(\d+)', text) ]

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  'gPsUK6nFPuNBFJuDCCsQzVwLJ9Z7AlJr3qdDB8mkUsIWgfoyA5',
  '                                                  ',
  '                                                  ',
  '                                                  '
)

# Make the request
blog = client.blog_info('artstation-py')

os.chdir('artstation')
current_dir = os.getcwd()
print(current_dir)
db_avoid = ["link_db.txt", "name_db.txt", "title_db.txt"]



with open('name_db.txt') as name:
    names_bot = json.load(name)


with open('link_db.txt') as link:
    source_bot = json.load(link)

with open('title_db.txt') as title:
	title_bot = json.load(title)

dir_images = os.listdir('.')
dir_images.sort(key=natural_keys)
print(dir_images)

current_dir2 = os.getcwd()
print(current_dir2)
'''print(ordered_files)'''
   
counter = 0

for artwork_image in dir_images:
    time.sleep(40)
    if artwork_image not in db_avoid: 
    		print(artwork_image)

	    	post = "Artist: "
    		post += names_bot[counter]
    		post += "\nSource: " 
    		post += source_bot[counter]
    		client.create_photo('art-py', state="published", tags=["artstation"],
    							caption=post,
    							data=artwork_image)	
    counter += 1
