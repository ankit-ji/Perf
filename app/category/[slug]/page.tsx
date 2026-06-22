import prisma from '@/lib/prisma';
import Link from 'next/link';
import styles from './page.module.css';

export default async function CategoryPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  
  let products: any[] = [];
  let title = "All Fragrances";

  if (slug === 'all') {
    products = await prisma.product.findMany({ include: { category: true } });
  } else {
    const category = await prisma.category.findUnique({ where: { slug } });
    if (category) {
      title = category.name;
      products = await prisma.product.findMany({
        where: { categoryId: category.id },
        include: { category: true }
      });
    } else {
      products = [];
    }
  }

  return (
    <div className={`container ${styles.page}`}>
      <div className={styles.header}>
        <h1 className={styles.title}>{title}</h1>
        <p className={styles.count}>{products.length} Products</p>
      </div>

      {products.length === 0 ? (
        <div className={styles.empty}>
          <p>No products found in this category.</p>
          <Link href="/category/all" className="btn-secondary" style={{ width: 'auto', display: 'inline-block', marginTop: '1rem' }}>
            View All
          </Link>
        </div>
      ) : (
        <div className={styles.grid}>
          {products.map(product => (
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
      )}
    </div>
  );
}
