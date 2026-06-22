"use client";

import { useCart } from '../context/CartContext';

type AddToCartProps = {
  product: {
    id: string;
    name: string;
    brand: string;
    price: number;
  };
};

export default function AddToCartButton({ product }: AddToCartProps) {
  const { addToCart } = useCart();

  const handleAdd = () => {
    addToCart(product);
  };

  return (
    <button onClick={handleAdd} className="btn-primary">
      Add to Cart
    </button>
  );
}
