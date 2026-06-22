import os
import requests
import time

os.makedirs('public/images', exist_ok=True)

# Wikimedia Commons API to get images in a category
url = "https://commons.wikimedia.org/w/api.php"
params = {
    "action": "query",
    "format": "json",
    "generator": "categorymembers",
    "gcmtitle": "Category:Perfumes",
    "gcmnamespace": "6", # 6 is for files (images)
    "gcmlimit": "30",
    "prop": "imageinfo",
    "iiprop": "url|extmetadata",
}

headers = {
    'User-Agent': 'PerfumeMarketBot/1.0 (test@example.com)'
}
response = requests.get(url, params=params, headers=headers)
try:
    data = response.json()
except Exception as e:
    print(response.text)
    raise e


products_data = []

if "query" in data and "pages" in data["query"]:
    pages = data["query"]["pages"]
    count = 1
    for page_id, page_info in pages.items():
        if count > 20:
            break
            
        title = page_info["title"].replace("File:", "").split(".")[0]
        # Clean up title
        name = title.replace("_", " ").split("(")[0].strip()
        
        imageinfo = page_info["imageinfo"][0]
        img_url = imageinfo["url"]
        
        print(f"Downloading {name}...")
        try:
            img_data = requests.get(img_url, timeout=10).content
            filepath = f"public/images/perfume-wm-{count}.jpg"
            with open(filepath, 'wb') as f:
                f.write(img_data)
                
            products_data.append({
                "name": name,
                "url": f"/images/perfume-wm-{count}.jpg"
            })
            count += 1
        except Exception as e:
            print(f"Failed to download {name}: {e}")
            
    # Write out the products data to a JSON file so we can update the seed script
    import json
    with open('wikimedia_perfumes.json', 'w') as f:
        json.dump(products_data, f, indent=2)
        
    print(f"Successfully downloaded {len(products_data)} real open-source images from Wikimedia Commons!")
else:
    print("Failed to fetch from Wikimedia Commons API.")
