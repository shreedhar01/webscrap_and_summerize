import json
import requests
from bs4 import BeautifulSoup
import re

def clean_text(text):
    # Remove citation markers
    text = re.sub(r'\[[^\]]+\]', '', text)
    
    # Remove multiple newlines
    text = re.sub(r'\n+', '\n', text)
    
    # Remove leading/trailing whitespace
    text = text.strip()
    
    # Replace Unicode characters
    text = text.replace('\xa0', ' ')
    
    return text

def scrape_wikipedia(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Remove unwanted sections
    for div in soup.find_all('div', {'class': ['toc', 'mw-jump-link', 'mw-editsection']}):
        div.decompose()

    content = soup.find('div', {'id': 'mw-content-text'})

    idx = -1  
    sections = []
    current_section = {'title': 'Introduction', 'content': '', 'idx': '0'}

    for element in content.find_all(['p', 'h2', 'h3', 'h4', 'h5', 'h6']):
        if element.name.startswith('h'):
            if current_section['content']:
                current_section['content'] = clean_text(current_section['content'])
                sections.append(current_section)
            idx += 1
            current_section = {'title': clean_text(element.text.strip()), 'content': '', 'idx': str(idx)}
        else:
            current_section['content'] += element.text + '\n'

    if current_section['content']:
        current_section['content'] = clean_text(current_section['content'])
        sections.append(current_section)

    # Specify the file path
    file_path = 'summerize_data.json'

    # Save the list to a JSON file
    with open(file_path, 'w') as file:
        json.dump(sections, file, indent=4)