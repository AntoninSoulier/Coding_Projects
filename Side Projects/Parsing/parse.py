import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-add-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
res = soup.find_all("a")
#print(res[-1])

print(soup.find_all(class_="govuk-footer__link govuk-footer__copyright-logo"))
