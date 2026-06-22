import { PrismaClient } from '@prisma/client'
const prisma = new PrismaClient()

async function main() {
  // Clear existing data
  await prisma.product.deleteMany({});
  await prisma.category.deleteMany({});

  const me = await prisma.category.upsert({
    where: { name: 'Middle Eastern' },
    update: {},
    create: { name: 'Middle Eastern', slug: 'middle-eastern' },
  })

  const designer = await prisma.category.upsert({
    where: { name: 'Designer' },
    update: {},
    create: { name: 'Designer', slug: 'designer' },
  })

  const niche = await prisma.category.upsert({
    where: { name: 'Niche' },
    update: {},
    create: { name: 'Niche', slug: 'niche' },
  })

  const products = [
    { name: 'Oud Wood Intense', brand: 'Tom Ford', description: 'A rich, dark blend of oud, spices, and woods.', price: 28500, imageUrl: '/images/perfume-1.jpg', categoryId: niche.id, notes: 'Oud, Cardamom, Sandalwood', isFeatured: true },
    { name: 'Club de Nuit Intense', brand: 'Armaf', description: 'A robust and woody masculine fragrance.', price: 3500, imageUrl: '/images/perfume-2.jpg', categoryId: me.id, notes: 'Lemon, Birch, Ambergris', isFeatured: true },
    { name: 'Sauvage Elixir', brand: 'Dior', description: 'An extraordinarily concentrated fragrance steeped in the emblematic freshness.', price: 18000, imageUrl: '/images/perfume-3.jpg', categoryId: designer.id, notes: 'Grapefruit, Spices, Lavender, Woods', isFeatured: false },
    { name: 'Baccarat Rouge 540', brand: 'Maison Francis Kurkdjian', description: 'A luminous and sophisticated fragrance.', price: 32000, imageUrl: '/images/perfume-4.jpg', categoryId: niche.id, notes: 'Saffron, Jasmine, Amberwood, Fir Resin', isFeatured: true },
    { name: 'Aventus', brand: 'Creed', description: 'The bestselling men’s fragrance in the history of the House of Creed.', price: 29500, imageUrl: '/images/perfume-5.jpg', categoryId: niche.id, notes: 'Pineapple, Birch, Musk, Oakmoss', isFeatured: true },
    { name: 'Khamrah', brand: 'Lattafa', description: 'A luxurious oriental gourmand fragrance.', price: 2800, imageUrl: '/images/perfume-6.jpg', categoryId: me.id, notes: 'Cinnamon, Dates, Praline, Vanilla', isFeatured: false },
    { name: 'Bleu de Chanel', brand: 'Chanel', description: 'A woody, aromatic fragrance for the man who defies convention.', price: 14500, imageUrl: '/images/perfume-7.jpg', categoryId: designer.id, notes: 'Citrus, Grapefruit, Ginger, Cedar', isFeatured: true },
    { name: 'Y Eau de Parfum', brand: 'Yves Saint Laurent', description: 'A seductive interpretation of the iconic Y white t-shirt and black jacket.', price: 12000, imageUrl: '/images/perfume-8.jpg', categoryId: designer.id, notes: 'Apple, Sage, Vetiver, Tonka Bean', isFeatured: false },
    { name: 'Asad', brand: 'Lattafa', description: 'A signature spicy and woody fragrance.', price: 2200, imageUrl: '/images/perfume-9.jpg', categoryId: me.id, notes: 'Black Pepper, Coffee, Patchouli, Amber', isFeatured: false },
    { name: 'Angels Share', brand: 'Kilian', description: 'Contains the essence of Cognac derived from the liquor to lend it a natural caramel color.', price: 24000, imageUrl: '/images/perfume-10.jpg', categoryId: niche.id, notes: 'Cognac, Cinnamon, Tonka Bean, Oak', isFeatured: false },
    { name: 'Hawas for Him', brand: 'Rasasi', description: 'Blends cinnamon, bergamot, orange blossom, grey amber and sandalwood.', price: 4500, imageUrl: '/images/perfume-11.jpg', categoryId: me.id, notes: 'Apple, Cinnamon, Plum, Ambergris', isFeatured: true },
    { name: 'Acqua di Giò Profumo', brand: 'Giorgio Armani', description: 'An aquatic, aromatic, woody and spicy composition.', price: 11500, imageUrl: '/images/perfume-12.jpg', categoryId: designer.id, notes: 'Sea Notes, Incense, Patchouli', isFeatured: false },
    { name: 'Tobacco Vanille', brand: 'Tom Ford', description: 'Opulent, warm, iconic.', price: 29000, imageUrl: '/images/perfume-13.jpg', categoryId: niche.id, notes: 'Tobacco Leaf, Vanilla, Cacao, Sweet Wood Sap', isFeatured: false },
    { name: 'Shaghaf Oud', brand: 'Swiss Arabian', description: 'An oriental oud fragrance that surrounds your passionate heart with the peerless beauty of rich, golden oud.', price: 3800, imageUrl: '/images/perfume-14.jpg', categoryId: me.id, notes: 'Saffron, Rose, Praline, Vanilla, Oud', isFeatured: false },
    { name: 'Spicebomb Extreme', brand: 'Viktor&Rolf', description: 'An explosive composition, highlighting aromatic lavender in a unique way.', price: 10500, imageUrl: '/images/perfume-15.jpg', categoryId: designer.id, notes: 'Vanilla, Tobacco, Black Pepper, Caraway', isFeatured: false },
    { name: 'Layton', brand: 'Parfums de Marly', description: 'A seductive oriental-floral fragrance with an intense olfactory signature.', price: 26500, imageUrl: '/images/perfume-16.jpg', categoryId: niche.id, notes: 'Apple, Vanilla, Cardamom, Pepper', isFeatured: false },
    { name: '9pm', brand: 'Afnan', description: 'A perfect evening fragrance for the modern man.', price: 2900, imageUrl: '/images/perfume-17.jpg', categoryId: me.id, notes: 'Apple, Cinnamon, Vanilla, Patchouli', isFeatured: false },
    { name: 'Terre dHermès', brand: 'Hermès', description: 'A plant and mineral scent, combining heaven and earth.', price: 11000, imageUrl: '/images/perfume-18.jpg', categoryId: designer.id, notes: 'Orange, Grapefruit, Pepper, Vetiver', isFeatured: false },
    { name: 'Naxos', brand: 'Xerjoff', description: 'Celebrates the deep and sensual heart of Sicily with a rich perfume.', price: 27500, imageUrl: '/images/perfume-19.jpg', categoryId: niche.id, notes: 'Lavender, Honey, Tobacco, Vanilla', isFeatured: true },
    { name: 'Ameer Al Oudh Intense Oud', brand: 'Lattafa', description: 'A warm, oriental fragrance with a rich oud and sweet vanilla base.', price: 2100, imageUrl: '/images/perfume-20.jpg', categoryId: me.id, notes: 'Oud, Woodsy Notes, Vanilla, Sugar', isFeatured: false }
  ];

  for (const product of products) {
    await prisma.product.create({ data: product });
  }

  console.log('Seeded database with 20 products!')
}

main()
  .catch((e) => {
    console.error(e)
    process.exit(1)
  })
  .finally(async () => {
    await prisma.$disconnect()
  })
