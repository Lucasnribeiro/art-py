import pytumblr
import json
import time
import os


# Authenticate via OAuth
client = pytumblr.TumblrRestClient(

  '                                                  ',
  '                                                  ',
  '                                                  ',
  '                                                  '
)

# Make the request
blog = client.blog_info('artstation-py')

os.chdir('artstation')


with open('name_db.txt') as name:
    names_bot = json.load(name)


with open('link_db.txt') as link:
    source_bot = json.load(link)

with open('title_db.txt') as title:
	title_bot = json.load(title)
      
counter = 0
for artwork_image in os.listdir('.'):
    print(artwork_image)
    print(title_bot)
    post = "Artist: "
    post += names_bot[counter]
    post += "\nSource: " 
    post += source_bot[counter]
    if artwork_image == title_bot[counter]:
    	client.create_photo('artstation-py', state="published", tags=["artstation"],
    						caption=post,
    						data=artwork_image)
    else:
    	print("Failed to find image")	
    counter += 1
