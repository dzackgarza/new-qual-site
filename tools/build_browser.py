#!/usr/bin/env python3
"""Assemble the standalone problem-bank browser + generator (site/browser.html).

Reads the corpus directly, joins each problem with its solutions and the exam
sittings it occurred at, and emits one self-contained HTML file -- corpus data,
the KaTeX renderer, and its fonts all inlined, so it opens with no server and
no network. This is the observable, auditable view of the migrated corpus and a
modern port of make-me-a-qual's selection tool.

    uv run python tools/build_browser.py
"""
import re, json, base64, subprocess, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent

def extract_corpus():
    cards = []
    for p in (ROOT/"corpus").rglob("*.md"):
        t = p.read_text(errors="replace")
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", t, re.S)
        if not m: continue
        try: fm = yaml.safe_load(m.group(1))
        except Exception: continue
        cards.append({"id":fm.get("id"),"kind":fm.get("kind"),"title":fm.get("title",""),
            "areas":(fm.get("classification") or {}).get("areas",[]),
            "topics":(fm.get("classification") or {}).get("topics",[]),
            "relations":fm.get("relations",[]),"payload":fm.get("payload"),"body":m.group(2).strip()})
    by_id = {c["id"]:c for c in cards}
    def sitting_of(sid):
        s = by_id.get(sid)
        if not s: return None
        pl = s.get("payload") or {}; d = pl.get("date") or {}
        return {"id":sid,"institution":pl.get("institution") or (pl.get("source_kind")=="contributed-artifact" and "misc") or "?",
            "area":pl.get("area"),"term":d.get("term"),"year":d.get("year"),"label":s.get("title",""),"kind":pl.get("source_kind")}
    prob_sit, prob_sol = {}, {}
    for c in cards:
        if c["kind"]=="occurrence":
            tgt=next((r["target"] for r in c["relations"] if r["kind"]=="instance-of"),None)
            src=(c.get("payload") or {}).get("source")
            if tgt and src: prob_sit.setdefault(tgt,[]).append(src)
        elif c["kind"]=="solution":
            tgt=next((r["target"] for r in c["relations"] if r["kind"]=="solves"),None)
            if tgt: prob_sol.setdefault(tgt,[]).append(c["body"])
    recs=[]
    for c in cards:
        if c["kind"] not in ("problem","exercise"): continue
        sits=[s for s in (sitting_of(x) for x in prob_sit.get(c["id"],[])) if s]
        recs.append({"id":c["id"],"kind":c["kind"],"title":c["title"],"areas":c["areas"],
            "topics":c["topics"],"body":c["body"],"solutions":prob_sol.get(c["id"],[]),"sittings":sits})
    (ROOT/"site"/"corpus-data.json").write_text(json.dumps(recs,separators=(",",":")))
    return recs

def katex_assets():
    kd = Path(subprocess.run(["bash","-lc","dirname $(find ~/.nvm -name katex.min.js 2>/dev/null | head -1)"],
        capture_output=True,text=True).stdout.strip())
    css = kd.joinpath("katex.min.css").read_text()
    def inline(m):
        f = kd/"fonts"/m.group(1).split("/")[-1]
        if f.suffix==".woff2" and f.exists():
            return "url(data:font/woff2;base64,%s)" % base64.b64encode(f.read_bytes()).decode()
        return "url(about:blank)"
    css = re.sub(r"url\((fonts/[^)]+\.woff2)\)", inline, css)
    css = re.sub(r",\s*url\(fonts/[^)]+\.(woff|ttf)\)\s*format\(['\"](woff|truetype)['\"]\)","",css)
    return css, kd.joinpath("katex.min.js").read_text(), kd.joinpath("contrib","auto-render.min.js").read_text()

extract_corpus()
data = (ROOT/"site"/"corpus-data.json").read_text()
macros_json = (ROOT/"vocabularies"/"macros.json").read_text()
katex_css, katex_js, katex_auto = katex_assets()

APP_CSS = r"""
:root{
  --paper:#f6f4ee; --card:#fffefb; --ink:#1c1b22; --ink-soft:#5b5a66; --ink-faint:#8a8895;
  --line:#e5e1d6; --line-soft:#efece3; --accent:#3d3a7a; --accent-soft:#e9e8f4;
  --alg:#b8791f; --ra:#1f8a7a; --ca:#7a5bd0; --top:#c0466e; --good:#2f8f4e;
  --chip-bg:#fff; --shadow:0 1px 2px rgba(20,18,40,.06),0 4px 14px rgba(20,18,40,.05);
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --serif:"Palatino Linotype",Palatino,"Iowan Old Style",Georgia,serif;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root{
  --paper:#141419; --card:#1d1d25; --ink:#ecebf2; --ink-soft:#a3a1b0; --ink-faint:#6d6b7a;
  --line:#2c2c37; --line-soft:#242430; --accent:#9b98e8; --accent-soft:#26243a;
  --alg:#d9a24f; --ra:#3fb6a2; --ca:#a68be8; --top:#e0708f; --good:#54c07a;
  --chip-bg:#23232d; --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 16px rgba(0,0,0,.28);
}}
:root[data-theme="light"]{
  --paper:#f6f4ee; --card:#fffefb; --ink:#1c1b22; --ink-soft:#5b5a66; --ink-faint:#8a8895;
  --line:#e5e1d6; --line-soft:#efece3; --accent:#3d3a7a; --accent-soft:#e9e8f4;
  --alg:#b8791f; --ra:#1f8a7a; --ca:#7a5bd0; --top:#c0466e; --good:#2f8f4e;
  --chip-bg:#fff; --shadow:0 1px 2px rgba(20,18,40,.06),0 4px 14px rgba(20,18,40,.05);
}
:root[data-theme="dark"]{
  --paper:#141419; --card:#1d1d25; --ink:#ecebf2; --ink-soft:#a3a1b0; --ink-faint:#6d6b7a;
  --line:#2c2c37; --line-soft:#242430; --accent:#9b98e8; --accent-soft:#26243a;
  --alg:#d9a24f; --ra:#3fb6a2; --ca:#a68be8; --top:#e0708f; --good:#54c07a;
  --chip-bg:#23232d; --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 16px rgba(0,0,0,.28);
}
*{box-sizing:border-box}
html,body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:15px;line-height:1.5}
.wrap{max-width:1200px;margin:0 auto;padding:0 20px}
a{color:var(--accent);text-decoration:none}
header{border-bottom:1px solid var(--line);background:var(--card);position:sticky;top:0;z-index:20}
.head{display:flex;align-items:center;gap:18px;padding:14px 0;flex-wrap:wrap}
.brand{font-family:var(--serif);font-size:22px;font-weight:600;letter-spacing:-.01em;margin-right:auto}
.brand small{display:block;font-family:var(--sans);font-size:11px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-faint);margin-top:2px}
.stats{display:flex;gap:20px}
.stat b{font-family:var(--serif);font-size:19px;font-variant-numeric:tabular-nums;display:block;line-height:1}
.stat span{font-size:11px;color:var(--ink-faint);letter-spacing:.04em;text-transform:uppercase}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.seg button{border:0;background:transparent;color:var(--ink-soft);padding:7px 16px;font:inherit;font-weight:600;cursor:pointer}
.seg button[aria-selected="true"]{background:var(--accent);color:#fff}
.iconbtn{border:1px solid var(--line);background:var(--card);color:var(--ink-soft);border-radius:8px;width:36px;height:34px;cursor:pointer;font-size:15px}
main{padding:22px 0 80px}
/* browse */
.browse{display:grid;grid-template-columns:230px 1fr;gap:26px;align-items:start}
.rail{position:sticky;top:78px;display:flex;flex-direction:column;gap:18px}
.field label{font-size:11px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-faint);display:block;margin-bottom:7px}
.search{width:100%;padding:9px 11px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink);font:inherit}
select{width:100%;padding:8px 10px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink);font:inherit}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chip{border:1px solid var(--line);background:var(--chip-bg);color:var(--ink-soft);border-radius:20px;padding:5px 11px;font-size:12.5px;font-weight:600;cursor:pointer;display:inline-flex;align-items:center;gap:6px}
.chip .dot{width:8px;height:8px;border-radius:50%}
.chip[aria-pressed="true"]{color:#fff;border-color:transparent}
.chip.alg[aria-pressed="true"]{background:var(--alg)} .chip.ra[aria-pressed="true"]{background:var(--ra)}
.chip.ca[aria-pressed="true"]{background:var(--ca)} .chip.top[aria-pressed="true"]{background:var(--top)}
.chk{display:flex;align-items:center;gap:8px;font-size:13.5px;color:var(--ink-soft);cursor:pointer}
.results-head{display:flex;align-items:baseline;justify-content:space-between;margin-bottom:12px}
.count{font-size:13px;color:var(--ink-faint)}
.count b{color:var(--ink);font-variant-numeric:tabular-nums}
.row{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:13px 15px;margin-bottom:9px;cursor:pointer;box-shadow:var(--shadow);transition:border-color .12s}
.row:hover{border-color:var(--accent)}
.row-top{display:flex;align-items:center;gap:10px;margin-bottom:4px}
.tag{font-family:var(--mono);font-size:11px;color:var(--ink-faint)}
.abadge{font-size:10.5px;font-weight:700;letter-spacing:.03em;text-transform:uppercase;padding:2px 7px;border-radius:5px;color:#fff}
.abadge.alg{background:var(--alg)} .abadge.ra{background:var(--ra)} .abadge.ca{background:var(--ca)} .abadge.top{background:var(--top)} .abadge.none{background:var(--ink-faint)}
.solved{margin-left:auto;font-size:11px;font-weight:700;color:var(--good);border:1px solid var(--good);border-radius:20px;padding:1px 8px}
.excerpt{color:var(--ink-soft);font-size:14px;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.row.open .excerpt{display:block;-webkit-line-clamp:unset}
.detail{margin-top:12px;padding-top:12px;border-top:1px solid var(--line-soft);display:none}
.row.open .detail{display:block}
.statement{font-size:15.5px;line-height:1.6}
.sittings{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.sit{font-size:12px;background:var(--accent-soft);color:var(--accent);border-radius:6px;padding:3px 9px;font-weight:600}
.soln{margin-top:12px;background:var(--line-soft);border-radius:8px;padding:12px 14px}
.soln h4{margin:0 0 6px;font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--good)}
.meta{margin-top:10px;font-size:12px;color:var(--ink-faint);display:flex;gap:14px;flex-wrap:wrap}
.empty{text-align:center;color:var(--ink-faint);padding:60px 20px}
/* generate */
.gen{display:grid;grid-template-columns:280px 1fr;gap:30px;align-items:start}
.panel{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px;position:sticky;top:78px;box-shadow:var(--shadow)}
.panel h3{font-family:var(--serif);margin:0 0 4px;font-size:18px}
.panel p.sub{margin:0 0 18px;font-size:13px;color:var(--ink-faint)}
.panel .field{margin-bottom:16px}
.num{width:100%;padding:9px 11px;border:1px solid var(--line);border-radius:8px;background:var(--paper);color:var(--ink);font:inherit;font-variant-numeric:tabular-nums}
.genbtn{width:100%;background:var(--accent);color:#fff;border:0;border-radius:9px;padding:12px;font:inherit;font-weight:700;cursor:pointer;font-size:15px}
.genbtn:hover{filter:brightness(1.06)}
.sheet{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:34px 40px;box-shadow:var(--shadow);min-height:300px}
.sheet-h{text-align:center;border-bottom:2px solid var(--ink);padding-bottom:16px;margin-bottom:28px}
.sheet-h h2{font-family:var(--serif);margin:0 0 6px;font-size:24px}
.sheet-h .desc{color:var(--ink-soft);font-size:13.5px}
.q{margin-bottom:26px;display:flex;gap:14px}
.qn{font-family:var(--serif);font-weight:700;font-size:18px;color:var(--accent);min-width:28px}
.qbody{flex:1;line-height:1.6}
.qsrc{font-size:11.5px;color:var(--ink-faint);margin-top:6px;font-style:italic}
.toolbar{display:flex;gap:10px;margin-bottom:14px}
.tbtn{border:1px solid var(--line);background:var(--card);color:var(--ink-soft);border-radius:8px;padding:8px 14px;font:inherit;font-weight:600;cursor:pointer}
.katex{font-size:1.02em}
@media (max-width:820px){.browse,.gen{grid-template-columns:1fr}.rail,.panel{position:static}}
@media print{header,.rail,.toolbar,.panel{display:none!important}.gen{display:block}.sheet{border:0;box-shadow:none;padding:0}body{background:#fff}}
"""

APP_JS = r"""
const AREA={"algebra":["alg","Algebra"],"real-analysis":["ra","Real Analysis"],"complex-analysis":["ca","Complex Analysis"],"topology":["top","Topology"]};
const root=document.documentElement;
// theme
const savedT=null; function applyT(t){if(t)root.setAttribute("data-theme",t);}
document.getElementById("theme").onclick=()=>{const cur=root.getAttribute("data-theme")|| (matchMedia("(prefers-color-scheme:dark)").matches?"dark":"light");applyT(cur==="dark"?"light":"dark");};
// math render
function renderMath(el){try{renderMathInElement(el,{delimiters:[{left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false},{left:"\\[",right:"\\]",display:true},{left:"\\(",right:"\\)",display:false}],throwOnError:false,macros:MACROS});}catch(e){}}
// strip fenced-div syntax to plain body for display
function clean(md){return md.replace(/^:::+\s*\{?[^}\n]*\}?\s*$/gm,"").replace(/^:::+.*$/gm,"").replace(/\\envlist/g,"").replace(/#\w[\w\/-]*/g,"").replace(/\^\w{6}\b/g,"").trim();}
function areaBadge(areas){if(!areas||!areas.length)return '<span class="abadge none">·</span>';return areas.filter(a=>AREA[a]).map(a=>`<span class="abadge ${AREA[a][0]}">${AREA[a][1].split(" ")[0]}</span>`).join(" ");}
function excerpt(md){let t=clean(md).replace(/\n+/g," ").replace(/\$\$?/g,"").replace(/\\[a-zA-Z]+/g," ");return t.slice(0,220);}
function sitLabel(s){let inst=(s.institution||"?").toUpperCase();let d=s.term?`${s.term[0].toUpperCase()+s.term.slice(1)} ${s.year||""}`:(s.year||(s.kind==="contributed-artifact"?"":"undated"));return `${inst} ${s.area?"":""}${d}`.trim();}

// ---- BROWSE ----
let F={q:"",areas:new Set(),inst:"",kind:"",solved:false};
const results=document.getElementById("results"), countEl=document.getElementById("count");
function match(r){
  if(F.areas.size && !r.areas.some(a=>F.areas.has(a)))return false;
  if(F.kind && r.kind!==F.kind)return false;
  if(F.solved && !r.solutions.length)return false;
  if(F.inst && !r.sittings.some(s=>s.institution===F.inst))return false;
  if(F.q){const q=F.q.toLowerCase();if(!(r.body.toLowerCase().includes(q)||(r.title||"").toLowerCase().includes(q)||r.id.toLowerCase().includes(q)))return false;}
  return true;
}
let shown=0, filtered=[];
function draw(reset){
  if(reset){filtered=CORPUS.filter(match);shown=0;results.innerHTML="";countEl.innerHTML=`<b>${filtered.length.toLocaleString()}</b> of ${CORPUS.length.toLocaleString()} problems`;}
  if(!filtered.length && reset){results.innerHTML='<div class="empty">No problems match these filters.</div>';return;}
  const slice=filtered.slice(shown,shown+40);
  const frag=document.createDocumentFragment();
  for(const r of slice){
    const div=document.createElement("div");div.className="row";
    div.innerHTML=`<div class="row-top">${areaBadge(r.areas)}<span class="tag">${r.id}</span>${r.solutions.length?'<span class="solved">solved</span>':''}</div><div class="excerpt">${escapeHtml(excerpt(r.body))}</div><div class="detail"></div>`;
    div.onclick=()=>{const open=div.classList.toggle("open");const d=div.querySelector(".detail");if(open&&!d.dataset.done){d.innerHTML=renderDetail(r);d.dataset.done="1";renderMath(d);}};
    frag.appendChild(div);
  }
  results.appendChild(frag);shown+=slice.length;
}
function renderDetail(r){
  let h=`<div class="statement">${escapeHtml(clean(r.body))}</div>`;
  if(r.sittings.length){const seen=new Set();h+=`<div class="sittings">`+r.sittings.filter(s=>{const k=sitLabel(s);if(seen.has(k))return false;seen.add(k);return true;}).map(s=>`<span class="sit">${escapeHtml(sitLabel(s))}</span>`).join("")+`</div>`;}
  for(const s of r.solutions)h+=`<div class="soln"><h4>Solution</h4><div>${escapeHtml(clean(s))}</div></div>`;
  h+=`<div class="meta"><span>${r.kind}</span>${r.topics.length?`<span>${r.topics.join(", ")}</span>`:""}<span>${r.sittings.length} sitting(s)</span></div>`;
  return h;
}
function escapeHtml(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
// filter wiring
document.getElementById("search").oninput=e=>{F.q=e.target.value;draw(true);};
document.querySelectorAll(".chip[data-area]").forEach(c=>c.onclick=()=>{const a=c.dataset.area;if(F.areas.has(a)){F.areas.delete(a);c.setAttribute("aria-pressed","false");}else{F.areas.add(a);c.setAttribute("aria-pressed","true");}draw(true);});
document.getElementById("inst").onchange=e=>{F.inst=e.target.value;draw(true);};
document.getElementById("kind").onchange=e=>{F.kind=e.target.value;draw(true);};
document.getElementById("solved").onchange=e=>{F.solved=e.target.checked;draw(true);};
window.addEventListener("scroll",()=>{if(document.getElementById("view-browse").style.display==="none")return;if(shown<filtered.length && innerHeight+scrollY>document.body.offsetHeight-600)draw(false);});

// ---- GENERATE ----
function mulberry(seed){return function(){seed|=0;seed=seed+0x6D2B79F5|0;let t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
document.getElementById("go").onclick=()=>{
  const areas=[...document.querySelectorAll('#gen-areas .chip[aria-pressed="true"]')].map(c=>c.dataset.area);
  const inst=document.getElementById("gen-inst").value;
  const n=Math.max(1,Math.min(40,+document.getElementById("gen-n").value||8));
  const needSol=document.getElementById("gen-sol").checked;
  let pool=CORPUS.filter(r=>{
    if(areas.length && !r.areas.some(a=>areas.includes(a)))return false;
    if(inst && !r.sittings.some(s=>s.institution===inst))return false;
    if(needSol && !r.solutions.length)return false;
    if(clean(r.body).length<15)return false;
    return true;});
  const seed=(Math.random()*1e9)|0;const rnd=mulberry(seed);
  for(let i=pool.length-1;i>0;i--){const j=Math.floor(rnd()*(i+1));[pool[i],pool[j]]=[pool[j],pool[i]];}
  const pick=pool.slice(0,n);
  const sheet=document.getElementById("sheet");
  if(!pick.length){sheet.innerHTML='<div class="empty">No problems match. Loosen the criteria.</div>';return;}
  const areaTxt=areas.length?areas.map(a=>AREA[a][1]).join(", "):"All areas";
  const instTxt=inst?inst.toUpperCase():"mixed sources";
  let h=`<div class="sheet-h"><h2>Practice Set</h2><div class="desc">${pick.length} problems · ${escapeHtml(areaTxt)} · ${escapeHtml(instTxt)}</div></div>`;
  pick.forEach((r,i)=>{
    const seen=new Set();const sits=r.sittings.filter(s=>{const k=sitLabel(s);if(seen.has(k))return false;seen.add(k);return true;});
    h+=`<div class="q"><div class="qn">${i+1}.</div><div class="qbody">${escapeHtml(clean(r.body))}${sits.length?`<div class="qsrc">${escapeHtml(sits.map(sitLabel).join(" · "))} · ${r.id}</div>`:`<div class="qsrc">${r.id}</div>`}</div></div>`;
  });
  sheet.innerHTML=h;renderMath(sheet);
};
document.querySelectorAll('#gen-areas .chip').forEach(c=>c.onclick=()=>c.setAttribute("aria-pressed",c.getAttribute("aria-pressed")==="true"?"false":"true"));
document.getElementById("print").onclick=()=>print();
// view switch
document.querySelectorAll(".seg button").forEach(b=>b.onclick=()=>{
  document.querySelectorAll(".seg button").forEach(x=>x.setAttribute("aria-selected","false"));
  b.setAttribute("aria-selected","true");
  document.getElementById("view-browse").style.display=b.dataset.v==="browse"?"":"none";
  document.getElementById("view-gen").style.display=b.dataset.v==="gen"?"":"none";
});
draw(true);
"""

# institution options
recs = json.loads(data)
insts = {}
for r in recs:
    for s in r["sittings"]:
        i=s.get("institution")
        if i: insts[i]=insts.get(i,0)+1
inst_opts = "".join(f'<option value="{i}">{i.upper()} ({n})</option>' for i,n in sorted(insts.items(),key=lambda x:-x[1]) if i not in ("misc","?"))
nprob=sum(1 for r in recs)
nsit=len(set((s.get("label") for r in recs for s in r["sittings"])))
nsol=sum(1 for r in recs if r["solutions"])

area_chips='\n'.join(f'<button class="chip {c}" data-area="{k}" aria-pressed="false"><span class="dot" style="background:var(--{c})"></span>{lbl}</button>' for k,(c,lbl) in {"algebra":("alg","Algebra"),"real-analysis":("ra","Real Analysis"),"complex-analysis":("ca","Complex"),"topology":("top","Topology")}.items())

HTML = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Qual Problem Bank</title>
<style>{katex_css}</style>
<style>{APP_CSS}</style>
</head><body>
<header><div class="wrap head">
  <div class="brand">Qual Problem Bank<small>Migrated corpus · browse & generate</small></div>
  <div class="stats">
    <div class="stat"><b>{nprob:,}</b><span>problems</span></div>
    <div class="stat"><b>{nsit:,}</b><span>sittings</span></div>
    <div class="stat"><b>{nsol:,}</b><span>with solutions</span></div>
  </div>
  <div class="seg" role="tablist"><button data-v="browse" aria-selected="true">Browse</button><button data-v="gen" aria-selected="false">Generate</button></div>
  <button class="iconbtn" id="theme" title="Toggle theme">◐</button>
</div></header>
<main class="wrap">
  <div id="view-browse" class="browse">
    <aside class="rail">
      <div class="field"><label for="search">Search</label><input class="search" id="search" placeholder="statement, tag, keyword…"></div>
      <div class="field"><label>Area</label><div class="chips">{area_chips}</div></div>
      <div class="field"><label for="inst">Institution</label><select id="inst"><option value="">Any</option>{inst_opts}</select></div>
      <div class="field"><label for="kind">Kind</label><select id="kind"><option value="">Problems &amp; exercises</option><option value="problem">Problems</option><option value="exercise">Exercises</option></select></div>
      <label class="chk"><input type="checkbox" id="solved"> Has a solution</label>
    </aside>
    <section>
      <div class="results-head"><div class="count" id="count"></div><div class="count">click a row to expand</div></div>
      <div id="results"></div>
    </section>
  </div>
  <div id="view-gen" class="gen" style="display:none">
    <aside class="panel">
      <h3>Generate a practice set</h3><p class="sub">A modern port of make-me-a-qual: pick criteria, assemble a printable sheet.</p>
      <div class="field"><label>Areas</label><div class="chips" id="gen-areas">{area_chips}</div></div>
      <div class="field"><label for="gen-inst">Institution</label><select id="gen-inst"><option value="">Any</option>{inst_opts}</select></div>
      <div class="field"><label for="gen-n">Number of problems</label><input class="num" id="gen-n" type="number" value="8" min="1" max="40"></div>
      <label class="chk" style="margin-bottom:18px"><input type="checkbox" id="gen-sol"> Only problems with a solution</label>
      <button class="genbtn" id="go">Generate set</button>
    </aside>
    <section>
      <div class="toolbar"><button class="tbtn" id="print">Print / PDF</button></div>
      <div class="sheet" id="sheet"><div class="empty">Set your criteria and press <b>Generate set</b>.</div></div>
    </section>
  </div>
</main>
<script>const MACROS={macros_json};const CORPUS={data};</script>
<script>{katex_js}</script>
<script>{katex_auto}</script>
<script>{APP_JS}</script>
</body></html>"""

Path("site/browser.html").write_text(HTML)
sz=Path("site/browser.html").stat().st_size
print(f"wrote site/browser.html: {sz//1024} KB ({sz/1e6:.2f} MB)")
