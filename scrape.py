from bs4 import BeautifulSoup
import requests
import pandas as pd
from csv import writer

# website="https://www.propertypro.ng/property-for-rent/in/lagos"
root="https://www.propertypro.ng/"
website='https://www.propertypro.ng/property-for-rent/in/lagos'
# website=f'{root}/property-for-rent/in/lagos'
get_website=requests.get(website)
get_website_text=get_website.text

soup=BeautifulSoup(get_website_text,'lxml')
lists=soup.find_all('div',class_="single-room-sale listings-property")

##Pagination
# pagination=soup.find('ul',class_="pagination")
# pages=pagination.find_all('li',class_="page-item")
# last_page=pages[3].text

title=[]
title2=[]
location=[]
price=[]
bed=[]
bath=[]
toilet=[]
date=[]

for list_ in lists:
    try:
        title.append(list_.find('h4',class_="listings-property-title").text)
    except:
        title.append("null")
    
    try:
        title2.append(list_.find("h3",class_="listings-property-title2").text)
    except:
        title2.append("null")
    try:    
        location.append(list_.find_all('h4')[1].get_text())
    except:
        location.append('null')
    try:
        price.append(list_.find('h3',class_="listings-price").text)
    except:
        price.append('null')
    try:
        bed.append(bed=list_.find('div',class_="fur-areea").find_all('span')[0].get_text())
    except:
        bed.append('null')
    try:
        bath.append(bath=list_.find('div',class_="fur-areea").find_all('span')[1].get_text())
    except:
        bath.append("null")
    try:
        toilet.append(toilet=list_.find('div',class_="fur-areea").find_all('span')[2].get_text())
    except:
        toilet.append("null")
    try:
        date.append(date=list_.find_all('h5')[0].get_text())
    except:
        date.append("null")


title=[]
title2=[]
location=[]
price=[]
bed=[]
bath=[]
toilet=[]
date=[]


for i in range(1,685):
    # for page in range(20):
   
    # https://www.propertypro.ng/property-for-rent/in/lagos?page=1
    # page=range(1,30)

    # webby=f'{website}/?page={page}'
    webby="https://www.propertypro.ng/property-for-rent/in/lagos?page="+str(i)+""
    get_website=requests.get(webby)
    get_website_text=get_website.text
    soup=BeautifulSoup(get_website_text,'lxml')
    lists=soup.find_all('div',class_="single-room-sale listings-property")


    
    for list_ in lists:
        try:
            title.append(list_.find('h4',class_="listings-property-title").text)
        except:
            title.append("null")
        
        try:
            title2.append(list_.find("h3",class_="listings-property-title2").text)
        except:
            title2.append("null")
        try:    
            location.append(list_.find_all('h4')[1].get_text())
        except:
            location.append('null')
        try:
            price.append(list_.find('h3',class_="listings-price").text)
        except:
            price.append('null')
        try:
            bed.append(list_.find('div',class_="fur-areea").find_all('span')[0].get_text())
        except:
            bed.append('null')
        try:
            bath.append(list_.find('div',class_="fur-areea").find_all('span')[1].get_text())
        except:
            bath.append("null")
        try:
            toilet.append(list_.find('div',class_="fur-areea").find_all('span')[2].get_text())
        except:
            toilet.append("null")
        try:
            date.append(list_.find_all('h5')[0].get_text())
        except:
            date.append("null")
        # try:
        # title.append(list.find('h4',class_="listings-property-title").text)
        
        # title.append(list.find('h4',class_="listings-property-title").text)
        # okay2=list.find("h3",class_="listings-property-title2")
        # title2.append(okay2.text)
        # location.append(list.find_all('h4')[1].get_text())
        # price.append(list.find('h3',class_="listings-price").text)
        # bed.append(bed=list.find('div',class_="fur-areea").find_all('span')[0].get_text())
        # bath.append(bath=list.find('div',class_="fur-areea").find_all('span')[1].get_text())
        # toilet.append(toilet=list.find('div',class_="fur-areea").find_all('span')[2].get_text())
        # date.append(date=list.find_all('h5')[0].get_text())
            
            
            
            # df=pd.DataFrame({"Title":title,"Second Title":title2,"Location":location,"Price":price,"Bedrooms":bed,"Toilets":toilet,"Date":date})
            # df.to_csv("Prop.csv",index=False)
        # except:
        #     pass
        #     print("---ERROR")

df=pd.DataFrame({"Title":title,"Second Title":title2,"Location":location,"Price":price,"Bedrooms":bed,"Toilets":toilet,"Date":date})
df.to_csv("Property3.csv",index=False)

 
 
 
 
 
 
 
 
 
 
 
            
    # # https://www.propertypro.ng/property-for-rent/in/lagos?page=1
    # website=f'{website}?page={page}'
    # get_website=requests.get(f'{website}?page={page}')
    # get_website_text=get_website.text
    # soup=BeautifulSoup(get_website_text,'lxml')

    # with open('property4.csv','w',newline='') as f:
    #     thewriter=writer(f)
    #     header=['First_Title','Second_Title','Location','Price','Bed','Bath','Toilet','Date']
    #     thewriter.writerow(header)
        
    #     for list in lists:
    #         try:

    #             title1=list.find('h4',class_="listings-property-title").text
    #             title2=list.find("h3",class_="listings-property-title2").text
    #             location=list.find_all('h4')[1].get_text()
    #             price=list.find('h3',class_="listings-price").text
    #             bed=list.find('div',class_="fur-areea").find_all('span')[0].get_text()
    #             bath=list.find('div',class_="fur-areea").find_all('span')[1].get_text()
    #             toilet=list.find('div',class_="fur-areea").find_all('span')[2].get_text()
    #             date=list.find_all('h5')[0].get_text()
    #             info=[title1,title2,location,price,bed,bath,toilet,date]
    #             thewriter.writerow(info)
    #         except:
    #             pass
