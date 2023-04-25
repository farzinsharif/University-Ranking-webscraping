import requests as req
import json
import re
from config_webqs import *
import config_webqs as conf
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

    try :
        for i in json_data["data"]:
            if json_data["data"][conf.counter]["country"] == country_name:
                needed_data = json_data["data"][conf.counter]["title"]
                link_list.append(needed_data)
                conf.university_counter += 1
            conf.counter += 1
        university_name_list=re.findall(r'>+\w+.*?<',str(link_list))
        print(university_name_list,'\n',f"Universities count availble for {country_name} is :",conf.university_counter)
    except Exception as EX :
        print(EX.__class__.__name__)

if __name__ == '__main__' :
    data_capture()
    uni_name()

