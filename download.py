import os
import requests
import json
from bs4 import BeautifulSoup
import time

products = [
    ('1', 'Tom Ford Oud Wood bottle white background'),
    ('2', 'Armaf Club de Nuit Intense man perfume bottle white background'),
    ('3', 'Dior Sauvage Elixir bottle white background'),
    ('4', 'Baccarat Rouge 540 maison francis kurkdjian bottle white background'),
    ('5', 'Creed Aventus bottle white background'),
    ('6', 'Lattafa Khamrah perfume bottle white background'),
    ('7', 'Bleu de Chanel parfum bottle white background'),
    ('8', 'ysl y eau de parfum bottle white background'),
    ('9', 'Lattafa Asad perfume bottle white background'),
    ('10', 'Kilian Angels Share perfume bottle white background'),
    ('11', 'rasasi hawas for him bottle white background'),
    ('12', 'acqua di gio profumo bottle white background'),
    ('13', 'tom ford tobacco vanille bottle white background'),
    ('14', 'swiss arabian shaghaf oud bottle white background'),
    ('15', 'spicebomb extreme bottle white background'),
    ('16', 'parfums de marly layton bottle white background'),
    ('17', 'afnan 9pm perfume bottle white background'),
    ('18', 'terre d hermes parfum bottle white background'),
    ('19', 'xerjoff naxos bottle white background'),
    ('20', 'lattafa ameer al oudh intense bottle white background'),
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

os.makedirs('public/images', exist_ok=True)

for pid, query in products:
    try:
        print(f"Searching for {query}...")
        url = f"https://www.bing.com/images/search?q={query.replace(' ', '+')}&form=HDRSC2"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the first image result in Bing
        a_tag = soup.find('a', class_='iusc')
        if a_tag and 'm' in a_tag.attrs:
            m = json.loads(a_tag['m'])
            img_url = m['murl']
            
            print(f"Found image: {img_url}")
            
            img_data = requests.get(img_url, headers=headers, timeout=10).content
            with open(f"public/images/perfume-{pid}.jpg", 'wb') as f:
                f.write(img_data)
            print(f"Saved perfume-{pid}.jpg")
        else:
            print(f"Failed to find image for {query}")
            
    except Exception as e:
        print(f"Error for {query}: {e}")
    
    time.sleep(1)
