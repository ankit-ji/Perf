import os
import primp
import time
from bs4 import BeautifulSoup

client = primp.Client(impersonate="chrome_120")

products = [
    ('1', 'Tom Ford Oud Wood Intense'),
    ('2', 'Armaf Club de Nuit Intense man'),
    ('3', 'Dior Sauvage Elixir'),
    ('4', 'Baccarat Rouge 540 maison francis kurkdjian'),
    ('5', 'Creed Aventus'),
    ('6', 'Lattafa Khamrah'),
    ('7', 'Bleu de Chanel parfum'),
    ('8', 'ysl y eau de parfum'),
    ('9', 'Lattafa Asad'),
    ('10', 'Kilian Angels Share'),
    ('11', 'rasasi hawas for him'),
    ('12', 'acqua di gio profumo'),
    ('13', 'tom ford tobacco vanille'),
    ('14', 'swiss arabian shaghaf oud'),
    ('15', 'spicebomb extreme'),
    ('16', 'parfums de marly layton'),
    ('17', 'afnan 9pm'),
    ('18', 'terre d hermes parfum'),
    ('19', 'xerjoff naxos'),
    ('20', 'lattafa ameer al oudh intense'),
]

os.makedirs('public/images', exist_ok=True)

for pid, query in products:
    try:
        print(f"Searching Notino for {query}...")
        url = f"https://www.notino.co.uk/search?f={query.replace(' ', '+')}"
        response = client.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for product images
        img_url = None
        for img in soup.find_all('img'):
            src = img.get('src') or ''
            if 'cdn.notinoimg.com' in src and 'detail_zoom' in src:
                img_url = src
                break
        
        if img_url:
            print(f"Found image: {img_url}")
            img_data = client.get(img_url).content
            with open(f"public/images/perfume-{pid}.jpg", 'wb') as f:
                f.write(img_data)
            print(f"Successfully saved perfume-{pid}.jpg")
        else:
            print(f"No image found for {query}")
            
    except Exception as e:
        print(f"Error searching {query}: {e}")
    time.sleep(2)
