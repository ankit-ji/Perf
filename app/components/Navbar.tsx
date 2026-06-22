"use client";

import Link from 'next/link';
import { useCart } from '../context/CartContext';
import styles from './Navbar.module.css';
import { useEffect, useState } from 'react';

export default function Navbar() {
  const { cartCount } = useCart();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  return (
    <nav className={styles.navbar}>
      <div className={`container ${styles.navContainer}`}>
        <div className={styles.logo}>
          <Link href="/">
            PERFUMERIE
          </Link>
        </div>
        
        <ul className={styles.navLinks}>
          <li><Link href="/category/middle-eastern">Middle Eastern</Link></li>
          <li><Link href="/category/designer">Designer</Link></li>
          <li><Link href="/category/niche">Niche</Link></li>
        </ul>

        <div className={styles.actions}>
          <Link href="/wishlist" className={styles.iconBtn}>
            Wishlist
          </Link>
          <Link href="/cart" className={styles.iconBtn}>
            Cart ({mounted ? cartCount : 0})
          </Link>
        </div>
      </div>
    </nav>
  );
}
