import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.58",
    "Accept-Language": "en-US,en;q=0.9"
}

ZILLOW_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"mapBounds"%3A%7B"west"%3A-122.54199065161133%2C"east"%3A-122.32466734838867%2C"south"%3A37.70402280287864%2C"north"%3A37.846491468300066%7D%2C"mapZoom"%3A12%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"price"%3A%7B"max"%3A872627%7D%2C"beds"%3A%7B"min"%3A1%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"max"%3A3000%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%7D%2C"isListVisible"%3Atrue%7D'

response = requests.get(ZILLOW_URL, headers=header)
all_html = response.text
soup = BeautifulSoup(all_html, "html.parser")

all_properties_link = soup.select(".list-card-top a")
properties_link = []

for i in all_properties_link:
    href = i["href"]
    if "http" not in href:
        properties_link.append(f"https://www.zillow.com{href}")
    else:
        properties_link.append(href)
# print(properties_link)

all_properties_address = soup.select(".list-card-info address")
properties_address = [i.get_text().split(" | ")[-1] for i in all_properties_address]
# print(properties_address)

all_properties_price = soup.select(".list-card-heading")
properties_price = []
for i in all_properties_price:
    try:
        price = i.select(".list-card-price")[0].contents[0]
    except IndexError:
        pass
    finally:
        properties_price.append(price)
properties_price.pop()

DRIVER_PATH = "path_"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)


for i in range(len(properties_link)):
    driver.get('form_link_here')
    time.sleep(2)

    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(properties_address[i])
    price.send_keys(properties_price[i])
    link.send_keys(properties_link[i])
    submit_button.click()