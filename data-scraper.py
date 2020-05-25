from bs4 import BeautifulSoup
import requests
import csv

#Get url and request data
url = "https://www.metacritic.com/browse/games/score/metascore/year/all/filtered"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
source = requests.get(url,headers=headers).text
soup = BeautifulSoup(source,'lxml')

#Create a csv file
csv_file = open('list2.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['list'])

#Scrape the data we are looking for
body = soup.find(class_='product_condensed')
list = body.ol.text

print(list)

#save to a csv file
csv_writer.writerow([list])

csv_file.close()
