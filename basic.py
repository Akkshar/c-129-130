from selenium import webdriver
from bs4 import BeautifulSoup
import requests
page = requests.get("http://127.0.0.1:5500/index.html")
#print(page.content)

soup = BeautifulSoup(page.content, "html.parser")
#print(soup.find_all("p"))
print(soup.find_all("p", class_="1"))