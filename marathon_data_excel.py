import pandas
import marathon_data_scraping_v2
from termcolor import colored as c

data = marathon_data_scraping_v2.web_scraping()
df = pandas.DataFrame(data)
print(type(df))

df.to_excel("marathon_data1.xls", index=False)

fails = pandas.ExcelFile('marathon_data1.xls')
lapas = [] # tukšs masīvs priekš faila lapām
for lapas_nosaukumus in fails.sheet_names:
    lapas.append(fails.parse(lapas_nosaukumus)) 
print(lapas)
print(c("Darbības", "green"))
print(lapas[0].columns)

atrast = lapas[0][2] == 1974
print(atrast)
print(lapas[0][atrast])
lapas.append(lapas[0][atrast])

lapas_nr = 1
with pandas.ExcelWriter('marathon_data2.xlsx') as fails:
    for lapa in lapas:
        lapa.to_excel(fails, sheet_name=str(lapas_nr), index=False)
        lapas_nr += 1