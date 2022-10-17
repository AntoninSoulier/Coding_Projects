import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
items = soup.find_all("p",class_="gem-c-document-list__item-description")
print(items)