import fs from 'fs'; import path from 'path'; import process from 'process';
const FIGMA_TOKEN=process.env.FIGMA_TOKEN||''; const FIGMA_FILE_ID=process.env.FIGMA_FILE_ID||'';
const BRANDS=(process.env.BRAND_LIST||'default').split(',');
const outTs=path.resolve('packages/theme/src/tokens.generated.ts');
const outCss=path.resolve('packages/theme/src/css-variables.css');

function defaults(light=true){
  return light?{color:{primary:"#28587B",onPrimary:"#FFFFFF",surface:"#F7F9FA",text:"#1F2A36",success:"#4B8158",accent:"#7B5E42"},
    radius:{md:"12px",lg:"16px",xl:"20px"},space:{sm:"8px",md:"12px",lg:"16px",xl:"24px"},font:{family:"Inter",sizeBase:"16px",lineBase:"24px"}}
  :{color:{primary:"#7CB4D6",onPrimary:"#121212",surface:"#121212",text:"#E6E6E6",success:"#7FB38D",accent:"#A98565"},
    radius:{md:"12px",lg:"16px",xl:"20px"},space:{sm:"8px",md:"12px",lg:"16px",xl:"24px"},font:{family:"Inter",sizeBase:"16px",lineBase:"24px"}};
}
async function fetchFigma(){ if(!FIGMA_TOKEN||!FIGMA_FILE_ID) return null;
  const res=await fetch(`https://api.figma.com/v1/files/${FIGMA_FILE_ID}/variables/local`,{headers:{'X-Figma-Token':FIGMA_TOKEN}});
  if(!res.ok) throw new Error('Figma API error '+res.status); return await res.json();
}
function mapTokens(fig,mode){ const base=defaults(mode==='light');
  return { color: { primary: base.color.primary, onPrimary: base.color.onPrimary, surface: base.color.surface, text: base.color.text, success: base.color.success, accent: base.color.accent },
           radius: base.radius, space: base.space, font: base.font }; }
function toCss(brand,mode,t){ const flat={}; const walk=(o,pre=[])=>{Object.entries(o).forEach(([k,v])=>{if(v&&typeof v==='object')walk(v,[...pre,k]); else flat[[...pre,k].join('-')]=String(v);});}; walk(t);
  const vars=Object.entries(flat).map(([k,v])=>`  --${k}:${v};`).join('\n'); return `:root[data-brand="${brand}"][data-color-scheme="${mode}"]{\n${vars}\n}\n`; }
function toTs(brands){ return `/* AUTO-GENERATED */\nexport const BRANDS = ${JSON.stringify(brands,null,2)} as const;\nexport default BRANDS;\n`; }

const fig = await fetchFigma().catch(()=>null);
const brands={}; for(const b of BRANDS){ brands[b]={ light: mapTokens(fig,'light'), dark: mapTokens(fig,'dark') }; }
fs.mkdirSync(path.dirname(outTs),{recursive:true}); fs.writeFileSync(outTs,toTs(brands));
let css=''; for(const [slug,t] of Object.entries(brands)){ css+=toCss(slug,'light',t.light)+toCss(slug,'dark',t.dark); }
fs.mkdirSync(path.dirname(outCss),{recursive:true}); fs.writeFileSync(outCss,css+'\n');
console.log('✅ Tokens generated for brands:', BRANDS.join(','));
