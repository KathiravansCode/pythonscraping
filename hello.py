import requests
import bs4
result=requests.get("http://www.example.com")

soup=bs4.BeautifulSoup(result.text,"lxml")
for item in soup.select('p'):
    print(item.getText())
