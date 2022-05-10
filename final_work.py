import requests
import bs4

adrese = "https://rimirigamarathon.r.mikatiming.com/?page=1&event=RM_JGDCD2S98D&event_main_group=2022&pid=startlist_list&pidp=startlist"
visa_lapa = requests.get(adrese)
lapas_saturs = bs4.BeautifulSoup(visa_lapa.content, 'html.parser')
atradu_info = lapas_saturs.find_all(class_="list-field-wrap")
#print(atradu_info[:10])
#atradu_number = lapas_saturs.find_all(class_="type-field")
#atradu_gads = lapas_saturs.find_all(class_="type-birthday")
#atradu_agegroup = lapas_saturs.find_all(class_="type-age_class")
#atradu_komanda = lapas_saturs.find_all(class_="type-age_class")

info = []
for athlete in atradu_info:
    athlete_information = []
#    print(athlete.prettify(),"\n\n")
    atradu_name = athlete.findChild("div").findChild("h4")
    if atradu_name != None:
#        print(atradu_name.string,"\n\n")
        athlete_name = atradu_name.string
#        print(athlete_name,"\n\n")
        athlete_information.append(athlete_name)
    #    print(athlete_information)
        
#    print(athlete.prettify(),"\n\n")
    atradu_numurs = athlete.findChild(class_="list-field type-field")
    if atradu_numurs != None:
        atradu_numurs = athlete.findChild(class_="list-field type-field").text
#        athlete_numurs = atradu_numurs.content
        print(atradu_numurs[6:],"\n\n")
'''
    athlete = athlete.findChild("div").findChild("div").findChild(class_="type-fullname").findChild("a")
    athlete = athlete.select(".type-fullname")
#    number = athlete.findChild(class_="list-field-wrap")#.findChild(class_="type-birthday")
#    print(athlete.prettify(),"\n\n")
    name = athlete.string
    print(name,"\n\n")
#    print(number.prettify(),"\n\n")
#for item in lapas_saturs.select(".type-birthday"):
#    print(item.text)
'''