import os
import requests
import time

os.makedirs('public/images', exist_ok=True)

# A comprehensive list of potential Unsplash perfume/beauty photo IDs to check
candidates = [
    # Proven to work in the previous run:
    "photo-1541643600914-78b084683601",  # 1. Tom Ford Oud Wood Intense Vibe
    "photo-1547887537-6158d64c35b3",  # 3. Dior Sauvage Elixir Vibe
    "photo-1608571423902-eed4a5ad8108",  # 5. Creed Aventus Vibe
    "photo-1616949755610-8c9bbc08f138",  # 6. Lattafa Khamrah Vibe
    "photo-1523293182086-7651a899d37f",  # 7. Chanel Bleu de Chanel Vibe
    "photo-1587015566802-5dc157c901cf",  # 8. YSL Y Eau de Parfum Vibe
    "photo-1615655096345-61a54750068d",  # 9. Lattafa Asad Vibe
    "photo-1594035910387-fea47794261f",  # 11. Rasasi Hawas for Him Vibe
    "photo-1557827983-012eb6ea8dc1",  # 12. Giorgio Armani Acqua di Giò Profumo Vibe
    "photo-1617897903246-719242758050",  # 16. PDM Layton Vibe
    "photo-1592945403244-b3fbafd7f539",  # 17. Afnan 9pm Vibe
    "photo-1515688594390-b649af70d282",  # 19. Xerjoff Naxos Vibe
    "photo-1584308666744-24d5c474f2ae",  # 20. Lattafa Ameer Al Oudh Vibe
    
    # Alternatives for the 7 failed ones:
    "photo-1595425970377-c9703cf48b6d",  # Minimal glass bottle
    "photo-1588405748373-122b2321bc31",  # Bottle with white flower
    "photo-1592949863410-d4700ec9a444",  # Pink perfume bottle
    "photo-1601049541289-9b1b7bbbfe19",  # Luxury cosmetic bottle
    "photo-1583483425010-c566431a7710",  # Bottle under spotlight
    "photo-1598440947619-2c35fc9aa908",  # Amber bottle
    "photo-1610475389650-705c93c4e207",  # Minimalist perfume packaging
    "photo-1578301978693-85fa9c0320b9",  # Cosmetic bottle
    "photo-1613521138378-577cf38890cf",  # Glass jar or bottle
    "photo-1615396899839-c99c121888b0",  # Perfume dropper bottle
    "photo-1608248597481-496100c80836",  # Glass spray bottle
    "photo-1619551719525-998f090c2394",  # Perfume design
    "photo-1627384113743-6bd5a479fffd",  # Beauty bottle
    "photo-1594035910387-fea47794261f",  # Mirror cosmetic bottle
    "photo-1585386959984-a4155224a1ad",  # Pink luxury bottle
    "photo-1605651260663-e5d7d91bfd6f",  # Gold oil dropper / perfume
    "photo-1618005182384-a83a8bd57fbe",  # Abstract bottle/fluid
    "photo-1592945403244-b3fbafd7f539",  # Mist spray bottle
    "photo-1616949755610-8c9bbc08f138",  # Amber glass bottle
    "photo-1541643600914-78b084683601"   # Double backup
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

working_ids = []

print("Verifying and downloading perfume photo IDs from Unsplash...")

for img_id in candidates:
    # Avoid duplicates
    if img_id in working_ids:
        continue
        
    url = f"https://images.unsplash.com/{img_id}?auto=format&fit=crop&w=800&h=800&q=80"
    try:
        # Check if URL works with a HEAD request
        response = requests.head(url, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"ID: {img_id} is VALID")
            working_ids.append(img_id)
            if len(working_ids) >= 20:
                print("Found 20 working photo IDs.")
                break
        else:
            print(f"ID: {img_id} is INVALID (HTTP {response.status_code})")
    except Exception as e:
        print(f"Error checking {img_id}: {e}")
    time.sleep(0.2)

# If we don't have 20, let's display warning
print(f"Found {len(working_ids)} working IDs total.")

# Download the working ones as perfume-1.jpg to perfume-20.jpg
for idx, img_id in enumerate(working_ids[:20]):
    count = idx + 1
    url = f"https://images.unsplash.com/{img_id}?auto=format&fit=crop&w=800&h=800&q=80"
    file_path = f"public/images/perfume-{count}.jpg"
    try:
        print(f"Downloading perfume-{count}.jpg from ID {img_id}...")
        res = requests.get(url, headers=headers, timeout=20)
        if res.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(res.content)
            print(f"  Saved to {file_path}")
        else:
            print(f"  Failed download: HTTP {res.status_code}")
    except Exception as e:
        print(f"  Failed download {img_id}: {e}")
    time.sleep(0.5)

print("Done downloading images!")
