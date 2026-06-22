import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'
}

url = "https://www.pexels.com/search/perfume/"

try:
    response = requests.get(url, headers=headers, timeout=15)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        imgs = soup.find_all('img')
        print(f"Found {len(imgs)} img tags.")
        
        urls = []
        for img in imgs:
            src = img.get('src') or ''
            data_src = img.get('data-src') or ''
            src_set = img.get('srcset') or ''
            
            for candidate in [src, data_src] + src_set.split(','):
                candidate = candidate.strip().split(' ')[0]
                if 'images.pexels.com/photos' in candidate:
                    clean_url = candidate.split('?')[0]
                    if clean_url not in urls:
                        urls.append(clean_url)
                        
        print(f"Found {len(urls)} unique Pexels image URLs:")
        for idx, u in enumerate(urls[:40]):
            print(f"{idx+1}: {u}")
    else:
        print(f"HTTP Status {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
