import requests as rq
import math
from bs4 import BeautifulSoup as bs

class webscraping:
    def fetch_game_status(web):
        if web.status_code == 404: return print(f'Invalid  . . . {web.url}')
        new = bs(web.text, 'html.parser') # Let's BeautifulSoup read text respone from request.
        web.close()
        fetch = new.find_all("p", {"class":"text-lead font-caption-body wait-for-i18n-format-render"}) # Fetch data that's format with header and classes. // form to array.

        data = str(fetch[0]).split('<p class="text-lead font-caption-body wait-for-i18n-format-render">')[1].split('</p>')[0] # spliting texts for capture only data.
        data2 = str(fetch[3]).split('<p class="text-lead font-caption-body wait-for-i18n-format-render">')[1].split('</p>')[0] # same as upper one. // we put string because they have non-type
        data = data.split(',') # The data of first one return string value with "," so we need to cut it then Transfer to Integers.
        formator_data1 = int(data[0]+data[1]) # from the upper one, we have splited "," so new the list data looks like this ('num', 'num2') and now format it.
        formator_data2 = int(data2)

        print(f'\n\nPlaying : {formator_data1} (Real-time)')
        print(f'Max players : {formator_data2} (Per Room)')
        print(f'Server Total : {math.floor(formator_data1/formator_data2)} (Around the following)') # Calculate total of servers

if __name__ == '__main__':
    gets = str(input('Enter game id : ')) # insert game's id.
    url = f"https://www.roblox.com/games/{gets}/"
    web = rq.get(url) # Send Request to webpage.
    runtime = webscraping.fetch_game_status(web) # main dish
