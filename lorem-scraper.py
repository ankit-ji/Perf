import os
import requests
import time

os.makedirs('public/images', exist_ok=True)

print("Fetching open-source perfume images...")

for i in range(1, 21):
    try:
        print(f"Downloading image {i}...")
        url = f"https://loremflickr.com/800/800/perfume,bottle/all?random={i}"
        response = requests.get(url, timeout=15)
        
        if response.status_code == 200:
            with open(f"public/images/perfume-{i}.jpg", 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download image {i}: HTTP {response.status_code}")
            
    except Exception as e:
        print(f"Error downloading {i}: {e}")
    time.sleep(0.5)

print("Done downloading open-source images.")
