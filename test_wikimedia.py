import requests

url = "https://commons.wikimedia.org/w/api.php"
params = {
    "action": "query",
    "format": "json",
    "generator": "categorymembers",
    "gcmtitle": "Category:Perfumes",
    "gcmnamespace": "6",
    "gcmlimit": "10",
    "prop": "imageinfo",
    "iiprop": "url",
}
headers = {
    'User-Agent': 'PerfumeMarketBot/1.0 (test@example.com)'
}
response = requests.get(url, params=params, headers=headers)
print("Status:", response.status_code)
print("Response:", response.text[:1000])
