'use client';
import { useState } from 'react';
export default function AdminPage(){
  const [brand,setBrand]=useState('default');
  const [scheme,setScheme]=useState('auto');
  return (
    <main style={{padding:'24px'}}>
      <h1 style={{color:'var(--color-primary)'}}>Admin Dashboard</h1>
      <section style={{marginTop:16}}>
        <h3>Theme & Branding</h3>
        <div style={{display:'flex', gap:12}}>
          <label>Brand:</label>
          <select value={brand} onChange={e=>setBrand(e.target.value)}>
            <option value="default">default</option>
          </select>
          <button className="btn" onClick={()=>{document.cookie=`rec_brand=${brand}; path=/`; location.reload();}}>Apply</button>
          <label>Scheme:</label>
          <select value={scheme} onChange={e=>setScheme(e.target.value)}>
            <option value="auto">auto</option><option value="light">light</option><option value="dark">dark</option>
          </select>
          <button className="btn" onClick={()=>{document.cookie=`rec_color_scheme=${scheme}; path=/`; location.reload();}}>Apply</button>
        </div>
      </section>
      <section style={{marginTop:24}}>
        <h3>Vendor Search (demo)</h3>
        <form onSubmit={async (e:any)=>{e.preventDefault();
          const q = e.target.q.value;
          const res = await fetch(`${process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000'}/v1/vendors/search?q=${encodeURIComponent(q)}`);
          const data = await res.json(); (document.getElementById('out') as any).textContent = JSON.stringify(data,null,2);
        }}>
          <input name="q" placeholder="e.g. lumber" style={{padding:8, marginRight:8}}/>
          <button className="btn" type="submit">Search</button>
        </form>
        <pre id="out" style={{marginTop:16, background:'rgba(0,0,0,0.06)', padding:12, borderRadius:'12px', maxHeight:320, overflow:'auto'}}></pre>
      </section>
      <section style={{marginTop:24}}>
        <h3>Exports</h3>
        <a className="btn" href={`${process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000'}/v1/exports/bidsheet/demo.csv`}>Download Bid Sheet CSV</a>
      </section>
    </main>
  );
}
