import Link from 'next/link';
import styles from './Footer.module.css';

export default function Footer() {
  return (
    <footer className={styles.footer}>
      <div className={`container ${styles.footerContainer}`}>
        <div className={styles.column}>
          <h3>Perfumerie</h3>
          <p>Elevate your presence with curated fragrances from around the world.</p>
        </div>
        
        <div className={styles.column}>
          <h3>Shop</h3>
          <ul>
            <li><Link href="/category/middle-eastern">Middle Eastern</Link></li>
            <li><Link href="/category/designer">Designer</Link></li>
            <li><Link href="/category/niche">Niche</Link></li>
          </ul>
        </div>
        
        <div className={styles.column}>
          <h3>Support</h3>
          <ul>
            <li><Link href="/faq">FAQ</Link></li>
            <li><Link href="/shipping">Shipping & Returns</Link></li>
            <li><Link href="/contact">Contact Us</Link></li>
          </ul>
        </div>
      </div>
      <div className={styles.copyright}>
        <p>&copy; {new Date().getFullYear()} Perfumerie. All rights reserved.</p>
      </div>
    </footer>
  );
}
