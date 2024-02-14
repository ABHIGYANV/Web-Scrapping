import requests
from bs4 import BeautifulSoup

with open("Dashboardinfo.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.paser')

def has_class(tag):
    return not tag.has_attr("class") and not tag.has_attr("id")

def has_content(tag):
    return tag.has_sttr("content")

result = soup.find_all(has_content)
for result in results:
    print(result, "\n\n")
