import os
import requests
from bs4 import BeautifulSoup
import time

os.makedirs('public/images', exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

print("Fetching Pexels perfume images...")
url = "https://www.pexels.com/search/perfume%20bottle/"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

imgs = soup.find_all('img')

valid_urls = []
for img in imgs:
    src = img.get('src') or img.get('data-src') or ''
    if 'images.pexels.com/photos' in src:
        # Get a high quality version
        hq_url = src.split('?')[0] + '?auto=compress&cs=tinysrgb&w=800&h=800&dpr=1'
        if hq_url not in valid_urls:
            valid_urls.append(hq_url)

print(f"Found {len(valid_urls)} unique perfume images.")

count = 1
for url in valid_urls:
    if count > 20:
        break
    try:
        print(f"Downloading image {count}...")
        img_data = requests.get(url, timeout=10).content
        with open(f"public/images/perfume-{count}.jpg", 'wb') as f:
            f.write(img_data)
        count += 1
    except Exception as e:
        print(f"Error downloading {url}: {e}")
    time.sleep(1)

print("Done downloading images.")
