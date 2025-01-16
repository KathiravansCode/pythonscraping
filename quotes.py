import requests
import bs4


# https://quotes.toscrape.com/page/1/

# no=1
# base_url='https://quotes.toscrape.com/page/'
# scrape_url=base_url+str(no)+'/'
# print(scrape_url)

no=1
base_url='https://quotes.toscrape.com/page/'
scrape_url=base_url+str(no)+'/'
page_valid=True
# authors=set()
while page_valid:
 result=requests.get(scrape_url)
 soup=bs4.BeautifulSoup(result.text,"lxml")
 if 'No quotes found!' in result.text:
      page_valid=False
      break
 ans=soup.select(".author")
 for author in ans:
    print(author.getText())

 no=no+1

      