import AddToCartButton from '@/app/components/AddToCartButton';
import prisma from '@/lib/prisma';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import styles from './page.module.css';

export const dynamic = 'force-dynamic';

export default async function ProductPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  
  const product = await prisma.product.findUnique({
    where: { id },
    include: { category: true }
  });

  if (!product) {
    notFound();
  }

  return (
    <div className={`container ${styles.page}`}>
      <div className={styles.grid}>
        <div className={styles.imageColumn}>
          <div className={styles.imagePlaceholder} style={{ overflow: 'hidden' }}>
            <img 
              src={product.imageUrl} 
              alt={product.name}
              style={{ width: '100%', height: '100%', objectFit: 'cover' }}
            />
          </div>
        </div>
        
        <div className={styles.infoColumn}>
          <div className={styles.breadcrumbs}>
            <Link href="/">Home</Link> / <Link href={`/category/${product.category.slug}`}>{product.category.name}</Link> / <span>{product.name}</span>
          </div>
          
          <h1 className={styles.title}>{product.name}</h1>
          <p className={styles.brand}>{product.brand}</p>
          <p className={styles.price}>₹{product.price.toLocaleString('en-IN')}</p>
          
          <div className={styles.description}>
            <p>{product.description}</p>
          </div>
          
          {product.notes && (
            <div className={styles.notes}>
              <strong>Fragrance Notes:</strong>
              <p>{product.notes}</p>
            </div>
          )}
          
          <div className={styles.actions}>
            <AddToCartButton product={{ id: product.id, name: product.name, brand: product.brand, price: product.price }} />
            <button className="btn-secondary">Buy Now</button>
            <button className={styles.wishlistBtn}>♡ Add to Wishlist</button>
          </div>
          
          <div className={styles.shippingInfo}>
            <p>✓ Free shipping on orders over $100</p>
            <p>✓ 30-day returns</p>
          </div>
        </div>
      </div>
    </div>
  );
}
