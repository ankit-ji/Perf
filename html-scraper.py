import os
import requests
import urllib.parse
from bs4 import BeautifulSoup
import time

products = [
    ('1', 'Tom Ford Oud Wood Intense perfume bottle'),
    ('2', 'Armaf Club de Nuit Intense man perfume bottle'),
    ('3', 'Dior Sauvage Elixir perfume bottle'),
    ('4', 'Baccarat Rouge 540 maison francis kurkdjian perfume bottle'),
    ('5', 'Creed Aventus perfume bottle'),
    ('6', 'Lattafa Khamrah perfume bottle'),
    ('7', 'Bleu de Chanel parfum bottle'),
    ('8', 'ysl y eau de parfum bottle'),
    ('9', 'Lattafa Asad perfume bottle'),
    ('10', 'Kilian Angels Share perfume bottle'),
    ('11', 'rasasi hawas for him perfume bottle'),
    ('12', 'acqua di gio profumo bottle'),
    ('13', 'tom ford tobacco vanille perfume bottle'),
    ('14', 'swiss arabian shaghaf oud perfume bottle'),
    ('15', 'spicebomb extreme perfume bottle'),
    ('16', 'parfums de marly layton perfume bottle'),
    ('17', 'afnan 9pm perfume bottle'),
    ('18', 'terre d hermes parfum bottle'),
    ('19', 'xerjoff naxos perfume bottle'),
    ('20', 'lattafa ameer al oudh intense perfume bottle'),
]

os.makedirs('public/images', exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for pid, query in products:
    try:
        print(f"Searching DDG HTML for {query}...")
        # Note: DDG HTML doesn't have an image search tab directly, but we can search Yahoo HTML
        url = f"https://search.yahoo.com/search?p={urllib.parse.quote(query)}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        img_url = None
        for img in soup.find_all('img'):
            src = img.get('src') or ''
            if src.startswith('https://tse') or src.startswith('http://tse'):
                img_url = src
                break
                
        if img_url:
            print(f"Found image: {img_url}")
            img_data = requests.get(img_url, headers=headers, timeout=10).content
            with open(f"public/images/perfume-{pid}.jpg", 'wb') as f:
                f.write(img_data)
            print(f"Successfully saved perfume-{pid}.jpg")
        else:
            print(f"No image found for {query}")
            
    except Exception as e:
        print(f"Error searching {query}: {e}")
    time.sleep(2)
