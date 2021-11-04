# Importing modules.

import os
import string
import random
from bs4 import BeautifulSoup # Beautiful Soup(bs4) is a Python library for pulling data out of HTML and XML files.
from lxml import html 
import requests # Requests allows you to send HTTP/1.1 requests extremely easily.
import cloudscraper # Bypasses cloudflare anti-bot for requests.
from colorama import init, Fore, Back, Style
init(convert=True)

# Creating output folder.

print(Style.BRIGHT)
print(Fore.CYAN + 'Creators Discord: appelsiensam#3693 \n')

if not os.path.exists('screenshots'):
    os.mkdir('screenshots')
    print(Fore.YELLOW + "Creating output folder!")
else:    
    print(Fore.YELLOW + "Output folder already exists!")

# Config for user.

amount = int(input('Amount of screenshots: '))

# URL ID list generator.

urllist = [] 

for x in  range(amount):
    characters = string.ascii_lowercase + string.digits
    id = ''.join(random.choice(characters) for y in range(6))
    url = 'https://prnt.sc/' + id
    urllist.append(url)

print(Fore.YELLOW + "Url list generated!")

# Fetching image from prnt.sc/{ID}.

print(Fore.YELLOW + 'Trying to save screenshots! \n')

bypasser = cloudscraper.create_scraper()

total_saved = amount
    
for z in urllist:

    htmldata = bypasser.get(z).text
    soup = BeautifulSoup(htmldata, 'html.parser') 
    screenshot = soup.find('img', {'class': 'no-click screenshot-image'})
    try: 
        
        src_url = screenshot['src'] # TEST = https://i.imgur.com/W4OnbYm.png

        # Saving image.

        print(Fore.GREEN + 'Saving screenshot from ' + z + "/")
        r = bypasser.get(src_url)
        if src_url[-3] == "p":
            with open("screenshots/" + z[16:22] + ".png", "wb") as f:
                f.write(r.content)
        else:
            with open("screenshots/" + z[16:22] + ".jpg", "wb") as f:
                f.write(r.content)
    
    except:
        total_saved -= 1
        print(Fore.RED + z + " can't fetch a screenshot! (Check yourself)")

print('\n' + Fore.YELLOW + str(total_saved) + ' screenshot(s) successfully saved!')