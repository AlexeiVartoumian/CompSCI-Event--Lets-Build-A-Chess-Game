import sys
import os
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager




def get_fat_cat_details():

    url = "https://en.wikipedia.org/wiki/List_of_venture_capital_firms"

    chrome_options = Options()
    chrome_options.add_argument("--headless") # bastard server-side renderings

    ## haha
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
    chrome_options.add_argument("accept-language=en-US,en;q=0.9")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    driver.get(url)
    driver.implicitly_wait(30)
    page_source = driver.page_source

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    #print(soup)
    return soup

#get_fat_cat_details()

def extract_list_items(soup):
    div_col = soup.find('div', class_='div-col')
    if div_col:
        ul = div_col.find('ul')
        if ul:
            items = ul.find_all('li')
            return [item.text.strip() for item in items]
    return []

#print( extract_list_items(get_fat_cat_details()))


def clean_text(text):
    # Remove flag emoji descriptions
    text = re.sub(r'\s*<span class="flagicon">.*?</span>\s*', '', text)
    # Remove remaining HTML tags
    text = re.sub(r'<.*?>', '', text)
    return text.strip()

items = extract_list_items(get_fat_cat_details())

# # Clean and write the extracted items to a new file
with open('extracted_data.txt', 'w+', encoding='utf-8') as file:
    for item in items:
        cleaned_item = clean_text(item)
        file.write(cleaned_item + '\n')

print("Extraction complete. Data saved to 'extracted_data.txt'.")