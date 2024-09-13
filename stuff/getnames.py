import requests
from bs4 import BeautifulSoup
import time
import re

def search_and_save_titles(input_filename, output_filename, append_word):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w+', encoding='utf-8') as output_file:
        for line in input_file:
            word = line.strip()
            if word:
                search_term = f"{word} {append_word}"
                url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}"
                
                # Send a GET request to the URL
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
                response = requests.get(url, headers=headers)
                
                # Parse the HTML content
                soup = BeautifulSoup(response.text, 'html.parser')
                
                #print(soup)
                # Find all search result titles
                search_results = soup.find_all('h3')
                
                #print(search_results, type(search_results) )

                res = [  re.findall(r'>(.*?)<', str(text)) for text in search_results ]

                #print(res)
              
                output_file.write(f"Search term: {search_term}\n")
                for result in search_results:
                    title = result.get_text()
                    output_file.write(f"- {title}\n")
                output_file.write("\n")  # Add a blank line between search terms
                
                # Wait for 2 seconds before the next search to avoid overwhelming Google
                time.sleep(2)

# Replace 'input.txt' with your input file name and 'output.txt' with your desired output file name
search_and_save_titles('sampledata.txt', 'google_results.txt', ' linkedin')