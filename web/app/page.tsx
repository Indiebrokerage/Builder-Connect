export default function Page(){
  return (
    <main style={{padding:'24px'}}>
      <h1 style={{color:'var(--color-primary)'}}>Real Estate Conduit</h1>
      <p>Theme tokens power this UI (brand + dark mode).</p>
      <div style={{display:'flex', gap:12, marginTop:12}}>
        <a className="btn" href="?brand=default">Default</a>
        <a className="btn" href="#" onClick={(e)=>{e.preventDefault();document.documentElement.setAttribute('data-color-scheme','light');document.cookie='rec_color_scheme=light; path=/; max-age=31536000';}}>Light</a>
        <a className="btn" href="#" onClick={(e)=>{e.preventDefault();document.documentElement.setAttribute('data-color-scheme','dark');document.cookie='rec_color_scheme=dark; path=/; max-age=31536000';}}>Dark</a>
        <a className="btn" href="#" onClick={(e)=>{e.preventDefault();document.cookie='rec_color_scheme=auto; path=/; max-age=31536000';location.reload();}}>Auto</a>
      </div>
      <div className="card" style={{marginTop:24}}>
        <h3>Sample Card</h3>
        <p>Uses CSS variables for colors and radii.</p>
        <a className="btn" href="/admin">Admin</a>
      </div>
    </main>
  );
}
