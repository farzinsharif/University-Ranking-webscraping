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
    return: None
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

def writer():
    """
    create excel file on your local machine
    return: None
    """
    try:
        df = pd.DataFrame(university_name_list)
        df.to_excel('University-list.xlsx', sheet_name='University-data',index=False)
    except Exception as EX :
            print(EX.__class__.__name__)



if __name__ == '__main__' :
    data_capture()
    uni_name()
    writer()
