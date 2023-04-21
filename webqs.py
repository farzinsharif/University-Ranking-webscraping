import requests as req
import json
import re
from config_webqs import *
import config_webqs as conf
def data_capture():
    global json_data
    response = req.get(URL_API).text
    json_data = json.loads(response)
    return json_data



#with open ("json_rank.json", "w", encoding="utf-8") as f:
#  f.write(str(json_data))
#jsut run it once so you have backup

def uni_name():

    for i in json_data["data"]:
        if json_data["data"][conf.counter]["country"] == country_name:
            needed_data = json_data["data"][conf.counter]["title"]
            link_list.append(needed_data)
            conf.university_counter += 1
        conf.counter += 1
    university_name_list=re.findall(r'>+\w+.*?<',str(link_list))
    print(university_name_list,'\n',f"Universities count availble for {country_name} is :",conf.university_counter)

if __name__ == '__main__' :
    data_capture()
    uni_name()

