from bs4 import BeautifulSoup
import requests
from lxml import etree
import pandas as pd

website = 'https://fbref.com/en/squads/19538871/2021-2022/Manchester-United-Stats'
result = requests.get(website)
content = result.text  # GET HTML

soup = BeautifulSoup(content, 'lxml')
dom = etree.HTML(str(soup))


#sıradaki futbolcu
big_liste = []
z=-1
while z <= 38:
    z +=1
    i = 1
    isim_ve_datalar = []

    # futbolcu ismi
    selected_elements_1 = dom.xpath(f"//*[@id='stats_standard_9']/tbody/tr[{z}]/th/a")
        

    for element in selected_elements_1:
        content = element.text
        isim_ve_datalar.append(content)
    # futbolcu dataları (satır)
    while i <= 33:

        selected_elements = dom.xpath(f"(//*[@id='stats_standard_9']/tbody/tr)[{z}]/td[{i}]")
        
        i += 1
        for element in selected_elements:
            content = element.text
            isim_ve_datalar.append(content)

    big_liste.append(isim_ve_datalar)

# print(big_liste)



df = pd.DataFrame(big_liste, columns=["Value", "Stat3", "Stat4", "Stat5", "Stat6", "Stat7", "Stat8", "Stat9", "Stat10", "Stat11", "Stat12", "Stat13", "Stat14", "Stat15","Stat", "Stat3", "Stat4", "Stat5", "Stat6", "Stat7", "Stat8", "Stat9", "Stat10", "Stat11", "Stat12", "Stat13", "Stat14", "Stat15","Stat", "Stat1as2", "Staasdt13", "Statds14", "Stat15","Stat"])

# Excel dosyasına yaz
df.to_excel("Standard_Stats.xlsx", index=False)
print('done')