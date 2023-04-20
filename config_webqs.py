#Change the country_name according to the country name available of response
URL_API = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3740566.txt?rqisst="
country_name ="United Kingdom"
counter, last_counter, university_counter  = 0, 0, 0
needed_data = str()
link_list = list()
not_finish_list =list()
university_name_list = list()