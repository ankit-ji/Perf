import Image from "next/image";
import Link from "next/link";
import styles from "./page.module.css";
import prisma from "@/lib/prisma";

export const dynamic = 'force-dynamic';

export default async function Home() {
  const featuredProducts = await prisma.product.findMany({
    where: { isFeatured: true },
    take: 4,
    include: { category: true }
  });

  return (
    <div className={styles.page}>
      <section className={styles.hero}>
        <div className={styles.heroContent}>
          <h1>Discover Your Signature Scent</h1>
          <p>Explore a curated collection of Middle Eastern, Designer, and Niche fragrances.</p>
          <Link href="/category/all" className="btn-primary" style={{ width: 'auto', display: 'inline-block' }}>
            Shop the Collection
          </Link>
        </div>
      </section>

      <section className={`container ${styles.featured}`}>
        <h2 className={styles.sectionTitle}>Featured Fragrances</h2>
        <div className={styles.grid}>
          {featuredProducts.map(product => (
            <div key={product.id} className={styles.card}>
              <div className={styles.imageWrapper}>
                <img 
                  src={product.imageUrl} 
                  alt={product.name}
                  style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                />
              </div>
              <div className={styles.cardBody}>
                <p className={styles.brand}>{product.brand}</p>
                <h3 className={styles.name}>{product.name}</h3>
                <p className={styles.price}>₹{product.price.toLocaleString('en-IN')}</p>
                <Link href={`/product/${product.id}`} className="btn-secondary" style={{ marginTop: '1rem', display: 'block', textAlign: 'center' }}>
                  View Details
                </Link>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className={styles.categoriesBanner}>
        <div className={`container ${styles.catGrid}`}>
          <div className={styles.catCard}>
            <h3>Middle Eastern</h3>
            <p>Oud, Amber & Spices</p>
            <Link href="/category/middle-eastern">Shop Now →</Link>
          </div>
          <div className={styles.catCard}>
            <h3>Designer</h3>
            <p>Modern Classics</p>
            <Link href="/category/designer">Shop Now →</Link>
          </div>
          <div className={styles.catCard}>
            <h3>Niche</h3>
            <p>Rare & Exclusive</p>
            <Link href="/category/niche">Shop Now →</Link>
          </div>
        </div>
      </section>
    </div>
  );
}
