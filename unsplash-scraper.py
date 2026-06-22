import os
import requests
from bs4 import BeautifulSoup

os.makedirs('public/images', exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

print("Fetching Unsplash perfume images...")
url = "https://unsplash.com/s/photos/perfume"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all image tags
imgs = soup.find_all('img')

valid_urls = []
for img in imgs:
    src = img.get('src', '')
    if 'images.unsplash.com/photo-' in src and 'w=' in src:
        # Get a high quality version
        hq_url = src.split('?')[0] + '?q=80&w=800&auto=format&fit=crop'
        if hq_url not in valid_urls:
            valid_urls.append(hq_url)

print(f"Found {len(valid_urls)} unique perfume images.")

# Download the first 20
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

print("Done downloading images.")
