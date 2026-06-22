const fs = require('fs');
const path = require('path');
const https = require('https');

const products = [
  { id: '1', name: 'Tom Ford Oud Wood Intense', query: 'tom ford oud wood intense perfume bottle' },
  { id: '2', name: 'Armaf Club de Nuit Intense', query: 'armaf club de nuit intense man perfume bottle' },
  { id: '3', name: 'Dior Sauvage Elixir', query: 'dior sauvage elixir bottle' },
  { id: '4', name: 'Baccarat Rouge 540', query: 'baccarat rouge 540 maison francis kurkdjian bottle' },
  { id: '5', name: 'Creed Aventus', query: 'creed aventus bottle' },
  { id: '6', name: 'Lattafa Khamrah', query: 'lattafa khamrah perfume bottle' },
  { id: '7', name: 'Bleu de Chanel', query: 'bleu de chanel parfum bottle' },
  { id: '8', name: 'YSL Y Eau de Parfum', query: 'ysl y eau de parfum bottle' },
  { id: '9', name: 'Lattafa Asad', query: 'lattafa asad perfume bottle' },
  { id: '10', name: 'Kilian Angels Share', query: 'kilian angels share perfume bottle' },
  { id: '11', name: 'Rasasi Hawas', query: 'rasasi hawas for him bottle' },
  { id: '12', name: 'Acqua di Gio Profumo', query: 'acqua di gio profumo bottle' },
  { id: '13', name: 'Tom Ford Tobacco Vanille', query: 'tom ford tobacco vanille bottle' },
  { id: '14', name: 'Swiss Arabian Shaghaf Oud', query: 'swiss arabian shaghaf oud bottle' },
  { id: '15', name: 'Viktor Rolf Spicebomb Extreme', query: 'spicebomb extreme bottle' },
  { id: '16', name: 'Parfums de Marly Layton', query: 'parfums de marly layton bottle' },
  { id: '17', name: 'Afnan 9pm', query: 'afnan 9pm perfume bottle' },
  { id: '18', name: 'Terre d Hermes', query: 'terre d hermes parfum bottle' },
  { id: '19', name: 'Xerjoff Naxos', query: 'xerjoff naxos bottle' },
  { id: '20', name: 'Lattafa Ameer Al Oudh', query: 'lattafa ameer al oudh intense bottle' },
];

async function fetchImage(query, filename) {
  const url = `https://images.search.yahoo.com/search/images?p=${encodeURIComponent(query)}`;
  
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        // Extract the first image URL from Yahoo images
        const match = data.match(/imgurl=([^&]+)&/);
        if (match && match[1]) {
          const imgUrl = decodeURIComponent(match[1]);
          console.log(`Found image for ${query}: ${imgUrl}`);
          downloadImage(imgUrl, filename).then(resolve).catch(reject);
        } else {
          console.log(`No image found for ${query}`);
          resolve(false);
        }
      });
    }).on('error', reject);
  });
}

function downloadImage(url, filename) {
  return new Promise((resolve, reject) => {
    // some URLs might be http instead of https
    const client = url.startsWith('https') ? https : require('http');
    client.get(url, (res) => {
      if (res.statusCode === 301 || res.statusCode === 302) {
        return downloadImage(res.headers.location, filename).then(resolve).catch(reject);
      }
      
      const filePath = path.join(__dirname, 'public', 'images', filename);
      const file = fs.createWriteStream(filePath);
      res.pipe(file);
      file.on('finish', () => {
        file.close();
        resolve(true);
      });
    }).on('error', reject);
  });
}

async function main() {
  const dir = path.join(__dirname, 'public', 'images');
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

  for (let i = 0; i < products.length; i++) {
    const product = products[i];
    const filename = `perfume-${i+1}.jpg`;
    try {
      await fetchImage(product.query, filename);
    } catch (e) {
      console.error(`Failed to fetch for ${product.name}`, e);
    }
    // sleep a bit to avoid rate limiting
    await new Promise(r => setTimeout(r, 1000));
  }
}

main();
