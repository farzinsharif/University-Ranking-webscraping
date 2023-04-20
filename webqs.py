import requests as req
import json
import re
from config_webqs import *

def data_capture():
    response = req.get(URL_API).text
    json_data = json.loads(response)
    return json_data



#with open ("json_rank.json", "w", encoding="utf-8") as f:
#  f.write(str(json_data))
#jsut run it once so you have backup

def uni_name(json_data):
    for i in json_data["data"]:
        if json_data["data"][counter]["country"] == country_name:
            needed_data = json_data["data"][counter]["title"]
            link_list.append(needed_data)
            university_counter += 1
        counter += 1
    university_name_list=re.findall(r'>+\w+.*?<',str(link_list))
    print(university_name_list,'\n',f"Universities count availble for {country_name} is :",university_counter)

if __name__ == '__main__' :
    data_capture()
    uni_name()

