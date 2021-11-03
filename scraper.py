# Importing modules.

import os
import string
import random
from bs4 import BeautifulSoup # Beautiful Soup(bs4) is a Python library for pulling data out of HTML and XML files.
from lxml import html 
import requests # Requests allows you to send HTTP/1.1 requests extremely easily.
import cloudscraper # Bypasses cloudflare anti-bot for requests.

# Creating output folder.

if not os.path.exists('screenshots'):
    os.mkdir('screenshots')
    print("Creating output folder!")
else:    
    print("Output folder already exists!")

# Config for user.

amount = int(input('Amount of screenshots: '))

# URL ID list generator.

urllist = [] 

for x in  range(amount):
    characters = string.ascii_lowercase + string.digits
    id = ''.join(random.choice(characters) for y in range(6))
    url = 'https://prnt.sc/' + id
    urllist.append(url)

print("Url list generated!")

# Fetching image from prnt.sc/{ID}.

print('Trying to save screenshots!')

bypasser = cloudscraper.create_scraper()
    
for z in urllist:
    
    htmldata = bypasser.get(z).text
    soup = BeautifulSoup(htmldata, 'html.parser') 
    screenshot = soup.find('img', {'class': 'no-click screenshot-image'})
    try: 
        
        src_url = screenshot['src'] # TEST = https://i.imgur.com/W4OnbYm.png

        # Saving image.

        print('Saving screenshot from ' + z + "/")
        r = bypasser.get(src_url)
        if src_url[-3] == "p":
            with open("screenshots/" + z[16:22] + ".png", "wb") as f:
                f.write(r.content)
        else:
            with open("screenshots/" + z[16:22] + ".jpg", "wb") as f:
                f.write(r.content)
    
    except:
        print(z + " no image found on this url!")

print(str(amount) + ' screenshot(s) saved!')
print('Creators Discord: appelsiensam#3693')