import prisma from '@/lib/prisma';
import Link from 'next/link';

export default async function AdminDashboard() {
  const products = await prisma.product.findMany({
    orderBy: { createdAt: 'desc' }
  });

  return (
    <div className="container" style={{ padding: '4rem 2rem' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '3rem' }}>
        <h1 style={{ fontSize: '2.5rem', textTransform: 'uppercase' }}>Admin Dashboard</h1>
        <button className="btn-primary" style={{ width: 'auto' }}>+ Add Product</button>
      </div>

      <div style={{ backgroundColor: 'var(--secondary)', padding: '2rem', borderRadius: '0px' }}>
        <h2 style={{ marginBottom: '2rem', fontSize: '1.25rem', textTransform: 'uppercase' }}>Product Inventory</h2>
        
        <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
          <thead>
            <tr style={{ borderBottom: '1px solid var(--border)', opacity: 0.7 }}>
              <th style={{ padding: '1rem 0' }}>Name</th>
              <th>Brand</th>
              <th>Price</th>
              <th>Featured</th>
              <th style={{ textAlign: 'right' }}>Actions</th>
            </tr>
          </thead>
          <tbody>
            {products.map(product => (
              <tr key={product.id} style={{ borderBottom: '1px solid var(--border)' }}>
                <td style={{ padding: '1rem 0', fontWeight: 'bold' }}>{product.name}</td>
                <td style={{ opacity: 0.8 }}>{product.brand}</td>
                <td>₹{product.price.toLocaleString('en-IN')}</td>
                <td>{product.isFeatured ? 'Yes' : 'No'}</td>
                <td style={{ textAlign: 'right' }}>
                  <Link href={`/admin/edit/${product.id}`} style={{ textDecoration: 'underline', marginRight: '1rem', fontSize: '0.875rem' }}>Edit</Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
