import requests

url = "https://commons.wikimedia.org/w/api.php"
params = {
    "action": "query",
    "format": "json",
    "generator": "search",
    "gsrsearch": "filetype:bitmap perfume bottle",
    "gsrnamespace": "6",
    "gsrlimit": "30",
    "prop": "imageinfo",
    "iiprop": "url",
}
headers = {
    'User-Agent': 'PerfumeMarketBot/1.0 (test@example.com)'
}
response = requests.get(url, params=params, headers=headers)
print("Status:", response.status_code)
try:
    data = response.json()
    if "query" in data and "pages" in data["query"]:
        pages = data["query"]["pages"]
        print(f"Found {len(pages)} pages.")
        for page_id, page_info in list(pages.items())[:5]:
            title = page_info["title"]
            img_url = page_info["imageinfo"][0]["url"]
            print(f"Title: {title}, URL: {img_url}")
    else:
        print("No pages found. Data:", data)
except Exception as e:
    print("Error:", e)
    print("Response:", response.text[:500])
