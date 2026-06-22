import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = "https://unsplash.com/napi/search/photos?query=perfume&per_page=30"

try:
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        print(f"Found {len(results)} photos.")
        for idx, photo in enumerate(results):
            photo_id = photo.get('id')
            description = photo.get('alt_description') or photo.get('description') or "No description"
            print(f"{idx+1}: ID={photo_id}, Desc={description[:50]}")
    else:
        print(f"Failed to fetch: HTTP {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
