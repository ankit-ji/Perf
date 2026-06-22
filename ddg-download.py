import os
import requests
import time
from duckduckgo_search import DDGS

products = [
    ('1', 'Tom Ford Oud Wood perfume bottle isolated white background'),
    ('2', 'Armaf Club de Nuit Intense man perfume bottle isolated white background'),
    ('3', 'Dior Sauvage Elixir perfume bottle isolated white background'),
    ('4', 'Baccarat Rouge 540 maison francis kurkdjian perfume bottle isolated white background'),
    ('5', 'Creed Aventus perfume bottle isolated white background'),
    ('6', 'Lattafa Khamrah perfume bottle isolated white background'),
    ('7', 'Bleu de Chanel parfum bottle isolated white background'),
    ('8', 'ysl y eau de parfum bottle isolated white background'),
    ('9', 'Lattafa Asad perfume bottle isolated white background'),
    ('10', 'Kilian Angels Share perfume bottle isolated white background'),
    ('11', 'rasasi hawas for him perfume bottle isolated white background'),
    ('12', 'acqua di gio profumo bottle isolated white background'),
    ('13', 'tom ford tobacco vanille perfume bottle isolated white background'),
    ('14', 'swiss arabian shaghaf oud perfume bottle isolated white background'),
    ('15', 'spicebomb extreme perfume bottle isolated white background'),
    ('16', 'parfums de marly layton perfume bottle isolated white background'),
    ('17', 'afnan 9pm perfume bottle isolated white background'),
    ('18', 'terre d hermes parfum bottle isolated white background'),
    ('19', 'xerjoff naxos perfume bottle isolated white background'),
    ('20', 'lattafa ameer al oudh intense perfume bottle isolated white background'),
]

os.makedirs('public/images', exist_ok=True)
ddgs = DDGS()

for pid, query in products:
    try:
        print(f"Searching DDG for {query}...")
        results = ddgs.images(query, max_results=3)
        if not results:
            print(f"No results for {query}")
            continue

        for res in results:
            img_url = res['image']
            print(f"Attempting download: {img_url}")
            try:
                img_data = requests.get(img_url, timeout=10).content
                with open(f"public/images/perfume-{pid}.jpg", 'wb') as f:
                    f.write(img_data)
                print(f"Successfully saved perfume-{pid}.jpg")
                break
            except Exception as e:
                print(f"Failed to download {img_url}: {e}")
                continue
    except Exception as e:
        print(f"Error searching {query}: {e}")
    time.sleep(2)
