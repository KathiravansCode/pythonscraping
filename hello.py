# import requests
# import bs4
# result=requests.get("http://www.example.com")

# soup=bs4.BeautifulSoup(result.text,"lxml")
# for item in soup.select('p'):
#     print(item.getText())
import requests
import bs4

result=requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup=bs4.BeautifulSoup(result.text,"lxml")

computer_img=soup.select(".mw-file-element")[1]
print(computer_img['src'])