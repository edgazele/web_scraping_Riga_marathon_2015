import requests
import bs4

end_page = 3
i = 1
information = []
athlete_name = []
count = 0

while i <= end_page:

    adrese = "https://rimirigamarathon.r.mikatiming.com/?page={}&event=RHM_JGDCD2S98D&event_main_group=2022&pid=startlist_list&pidp=startlist"
    visa_lapa = requests.get(adrese.format(i))
    lapas_saturs = bs4.BeautifulSoup(visa_lapa.content, 'html.parser')

    atradu_vardu = lapas_saturs.find_all(class_="col-xs-12 col-sm-12 col-md-4 list-field-wrap")
    atradu_info = lapas_saturs.find_all(class_="col-xs-12 col-sm-12 col-md-8 list-field-wrap")

    for atradu_name in lapas_saturs.select(".type-fullname"):
        athlete_name.append(atradu_name.text)
    athlete_name.pop(0)

    for info in atradu_info:
        athlete_information = []
        athlete_information.append(athlete_name[count])
        atradu_numurs = info.findChild(class_="list-field type-field").text[6:]
        athlete_information.append(atradu_numurs)
        atradu_gads = info.findChild(class_="list-field type-birthday").text[14:]
        athlete_information.append(atradu_gads)
        atradu_vecuma_grupu = info.findChild(class_="list-field type-age_class").text[2:]
        athlete_information.append(atradu_vecuma_grupu)
        atradu_komandu = info.select(".type-field")[1].text[7:]
        athlete_information.append(atradu_komandu)
        count = count + 1

        information.append(athlete_information)

    i = i+1
    
print(information)



