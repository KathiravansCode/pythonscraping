import requests
import bs4


# https://books.toscrape.com/catalogue/page-1.html

# base_url='https://books.toscrape.com/catalogue/page-1.html'
# result=requests.get(base_url)
# soup=bs4.BeautifulSoup(result.text,"lxml")
# books=soup.select(".product_pod")
# for book in books:
#     if len(book.select('.star-rating.One'))!=0:
#        print(book.select('a')[1]['title'])
        
two_star_books=[]
for i in range(1,51):
    base_url='https://books.toscrape.com/catalogue/page-{}.html'
    scrape_url=base_url.format(i)
    result=requests.get(scrape_url)
    soup=bs4.BeautifulSoup(result.text,"lxml")
    books=soup.select('.product_pod')
    for book in books:
        if len(book.select('.star-rating.Two'))!=0:
            print(book.select('a')[1]['title'])

          
