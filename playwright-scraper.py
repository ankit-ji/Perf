import asyncio
from playwright.async_api import async_playwright
import urllib.parse
import os
import requests
import time

products = [
    ('1', 'Tom Ford Oud Wood Intense perfume bottle'),
    ('2', 'Armaf Club de Nuit Intense man perfume bottle'),
    ('3', 'Dior Sauvage Elixir perfume bottle'),
    ('4', 'Baccarat Rouge 540 maison francis kurkdjian perfume bottle'),
    ('5', 'Creed Aventus perfume bottle'),
    ('6', 'Lattafa Khamrah perfume bottle'),
    ('7', 'Bleu de Chanel parfum bottle'),
    ('8', 'ysl y eau de parfum bottle'),
    ('9', 'Lattafa Asad perfume bottle'),
    ('10', 'Kilian Angels Share perfume bottle'),
    ('11', 'rasasi hawas for him perfume bottle'),
    ('12', 'acqua di gio profumo bottle'),
    ('13', 'tom ford tobacco vanille perfume bottle'),
    ('14', 'swiss arabian shaghaf oud perfume bottle'),
    ('15', 'spicebomb extreme perfume bottle'),
    ('16', 'parfums de marly layton perfume bottle'),
    ('17', 'afnan 9pm perfume bottle'),
    ('18', 'terre d hermes parfum bottle'),
    ('19', 'xerjoff naxos perfume bottle'),
    ('20', 'lattafa ameer al oudh intense perfume bottle'),
]

os.makedirs('public/images', exist_ok=True)

async def main():
    async with async_playwright() as p:
        # Launch browser in headless mode
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        for pid, query in products:
            try:
                print(f"Searching for {query}...")
                url = f"https://duckduckgo.com/?q={urllib.parse.quote(query)}&t=h_&iax=images&ia=images"
                await page.goto(url, wait_until='networkidle')
                
                # Wait for the first image tile to load
                await page.wait_for_selector('.tile--img__img', timeout=10000)
                
                # Get the src attribute of the first image
                img_element = await page.query_selector('.tile--img__img')
                if img_element:
                    img_src = await img_element.get_attribute('src')
                    if img_src and img_src.startswith('//'):
                        img_src = 'https:' + img_src
                    
                    print(f"Found image: {img_src}")
                    img_data = requests.get(img_src, timeout=10).content
                    with open(f"public/images/perfume-{pid}.jpg", 'wb') as f:
                        f.write(img_data)
                    print(f"Successfully saved perfume-{pid}.jpg")
                else:
                    print(f"No image found for {query}")
            except Exception as e:
                print(f"Error searching {query}: {e}")
            
            await asyncio.sleep(2)
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
