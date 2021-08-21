from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
Browser = webdriver.Chrome(executable_path="/Users/mac/Desktop/c-128/chromedriver")
Browser.get(url)
time.sleep(10)

def scrap():
    headers = ["Name", "LightYears", "PlanetMass", "Stealler_magnitude", "Discovery_Date"]
    planet_data = []
    for i in range(0,448):
        soup = BeautifulSoup(Browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs = {"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            list = []
        for index, li_tag in enumerate(li_tags):
            if index == 0:
                list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    list.append(li_tag.contents[0])
                except:
                    list.append(" ")

        planet_data.append(list)
        Browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()
        print(f"(i) page Done1")
        with open("data.csv", "w", newline="" ) as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(headers)
            csvwriter.writerows(planet_data)

scrap()