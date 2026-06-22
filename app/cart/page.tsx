"use client";

import { useState } from 'react';
import { useCart } from '../context/CartContext';
import Link from 'next/link';

export default function CartPage() {
  const [isProcessing, setIsProcessing] = useState(false);
  const { cart, removeFromCart, cartTotal } = useCart();

  const handleCheckout = () => {
    setIsProcessing(true);
    // Razorpay Checkout Simulation Template
    setTimeout(() => {
      alert("Razorpay checkout mock successful. Integration of actual API required.");
      setIsProcessing(false);
    }, 1500);
  };

  if (cart.length === 0) {
    return (
      <div className="container" style={{ padding: '4rem 2rem', textAlign: 'center' }}>
        <h1 style={{ fontSize: '2.5rem', marginBottom: '2rem', textTransform: 'uppercase' }}>Your Cart</h1>
        <p style={{ marginBottom: '2rem' }}>Your cart is currently empty.</p>
        <Link href="/category/all" className="btn-primary" style={{ display: 'inline-block', width: 'auto' }}>
          Continue Shopping
        </Link>
      </div>
    );
  }

  return (
    <div className="container" style={{ padding: '4rem 2rem' }}>
      <h1 style={{ fontSize: '2.5rem', marginBottom: '2rem', textTransform: 'uppercase' }}>Your Cart</h1>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem', marginBottom: '4rem' }}>
        {cart.map((item) => (
          <div key={item.id} style={{ display: 'flex', justifyContent: 'space-between', borderBottom: '1px solid var(--border)', paddingBottom: '1rem' }}>
            <div>
              <h3 style={{ fontSize: '1.25rem' }}>{item.name}</h3>
              <p style={{ opacity: 0.6, fontSize: '0.875rem' }}>{item.brand}</p>
              <button 
                onClick={() => removeFromCart(item.id)}
                style={{ background: 'none', border: 'none', textDecoration: 'underline', color: 'red', marginTop: '0.5rem', cursor: 'pointer', padding: 0 }}
              >
                Remove
              </button>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '2rem' }}>
              <p>Qty: {item.quantity}</p>
              <p>₹{(item.price * item.quantity).toLocaleString('en-IN')}</p>
            </div>
          </div>
        ))}
      </div>

      <div style={{ maxWidth: '400px', marginLeft: 'auto', backgroundColor: 'var(--secondary)', padding: '2rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem' }}>
          <span>Subtotal</span>
          <span>₹{cartTotal.toLocaleString('en-IN')}</span>
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '2rem', fontWeight: 'bold' }}>
          <span>Total</span>
          <span>₹{cartTotal.toLocaleString('en-IN')}</span>
        </div>
        
        <button 
          onClick={handleCheckout} 
          className="btn-primary" 
          disabled={isProcessing}
        >
          {isProcessing ? 'Processing...' : 'Checkout securely with Razorpay'}
        </button>
      </div>
    </div>
  );
}
