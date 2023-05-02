"""
If you want to save the data on any database or any other use of data
no need to use writer func , simply comment it and the code will work propery for you.
"""

import requests as req
import json
import re
from config_webqs import *
import config_webqs as conf
import pandas as pd
from bs4 import BeautifulSoup
import csv

def data_capture():
    """
    Gather data using from API
    return: json_data
    """
    
    global json_data
    try :
        response = req.get(URL_API).text
        json_data = json.loads(response)
        return json_data
    except Exception as EX :
        print(EX.__class__.__name__)



def uni_name():
    """
    print University_rank_list in terminal
    return: University_name_list
    """

    global university_name_list
    try :
        for i in json_data["data"]:
            if json_data["data"][conf.counter]["country"] == country_name:
                needed_data = json_data["data"][conf.counter]["title"]
                link_list.append(needed_data)
                conf.university_counter += 1
            conf.counter += 1
        university_name_list=re.findall(r'>+\w+.*?<',str(link_list))
        print(university_name_list,'\n',f"Universities count availble for {country_name} is :",conf.university_counter)
        return university_name_list
    except Exception as EX :
        print(EX.__class__.__name__)

def uni_link():
    """
    search for website link of the universities in google
    return : universities link list
    """
    try:
        global university_link

        url = 'https://www.google.com/search'

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
        }
        for university in university_name_list:
            search = university
            parameters = {'q': search}

            content = req.get(url, headers=headers, params=parameters).text
            soup = BeautifulSoup(content, 'html.parser')

            search = soup.find(id='search')
            first_link = search.find('a')
            output = first_link['href']
            university_link.append(output)


        print(university_link)
        return university_link
    except Exception as EX :
        print(EX.__class__.__name__)

def writer():
    """
    create csv file on your local machine
    return: None
    """
    try :
        final = zip (university_name_list, university_link)
        header = ['Name', 'Link']
        with open('University list.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(final)
    except Exception as EX :
        print(EX.__class__.__name__)

if __name__ == '__main__' :
    data_capture()
    uni_name()
    uni_link()
    writer()
